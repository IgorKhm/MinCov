"""
Created on Jul 10, 2019

@author: ikhmelnitsky
"""
import csv
import datetime
import os
import smtplib
import ssl
import time
import uuid
from copy import copy

import numpy as np
from z3 import z3

from export_petri_net import export_petri_to_spec
from omega_transition import OmegaTransition
from performance import run_benchmark, Benchmark, write_benchmark_csv
from petri_net import PetriNet


def random_petri_net():
    min_num_places = 10
    max_num_place = 50
    min_num_trans = 10
    max_num_trans = 50
    max_num_io = 10

    dim = np.random.randint(min_num_places, max_num_place)

    petri_net = PetriNet(dim)

    num_of_trans = np.random.randint(min_num_trans, max_num_trans)

    for i in range(num_of_trans):
        inputs = np.random.randint(1, max_num_io)
        outputs = np.random.randint(1, max_num_io)
        pre = np.zeros(dim)
        post = np.zeros(dim)
        for j in range(inputs):
            p = np.random.randint(0, dim - 1)
            pre[p] += int(np.random.randint(100, 200) / 99)
        for n in range(outputs):
            p = np.random.randint(0, dim - 1)
            post[p] += int(np.random.randint(100, 200) / 99)

        incidence = post - pre
        petri_net.add_transition(OmegaTransition(pre, incidence))

    return petri_net


fieldnames = ['Name', '#transitions', '#places', '#Max vertices', '#Final vertices', '#Max acc', '#Final acc',
              '#Accs reused', 'Time']


def generate_petri_nets():
    init_time = time.time()
    time_to_finish = 60 * 60 * 24

    num_of_petri_nets = 100
    num_of_init_markings = 5
    time_out = 1800
    file_name_petri = "/petri_net"
    timestamp_str = datetime.datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    dir_run = "benchmarks/random_petri_nets/run-" + timestamp_str + "/"
    benchmarks = []
    file_for_benchmark = dir_run + "results.csv"

    os.makedirs(dir_run)
    with open(file_for_benchmark, mode='a') as employee_file:
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        writer.writeheader()

    while num_of_petri_nets > 0:
        petri = PetriNet(1)
        while (petri.get_dim() < 10) | is_petri_stractually_bounded(petri):
            if is_petri_stractually_bounded(petri) & (petri.get_dim() > 10):
                print("bounded")
            petri = random_petri_net()
            biggest_connected_component = {}
            for connected_component in all_connected_components(petri):
                if len(biggest_connected_component) < len(connected_component):
                    biggest_connected_component = connected_component
            petri = projection_of_petri_on_places(petri, biggest_connected_component)

        uniq_id = str(uuid.uuid1())
        dir_for_petri = dir_run + "/" "_p_" + str(petri.get_dim()) + "_t_" + str(
            len(petri.get_transitions())) + "_d_" + timestamp_str + "_" + uniq_id
        os.makedirs(dir_for_petri)

        benchmark = Benchmark("empty")
        max_num_of_tries = 300
        current_try = 0
        benchmark.max_vertices = 0
        benchmark.timeout = False
        while (benchmark.max_vertices < 1000) & (benchmark.time < 0.8):
            current_try += 1
            marking = np.zeros(petri.get_dim())
            # max_norm = petri.get_dim() / 2
            norm_of_init_marking = np.random.randint(1, petri.get_dim() / 2)
            for p in range(norm_of_init_marking):
                marking[np.random.randint(0, int(petri.get_dim() - 1))] += 1
            init_mark = marking
            uniq_id = str(uuid.uuid1())
            petri_name = file_name_petri + uniq_id + ".spec"
            benchmark, cov = run_benchmark(petri_name, petri, time_out, init_mark, True)
            if current_try > max_num_of_tries:
                break

        if current_try > max_num_of_tries:
            if time.time() - init_time > time_to_finish:
                break
            continue

        petri.mark_the_petri_net(init_mark)
        export_petri_to_spec(petri, dir_for_petri + petri_name, True)
        benchmark.init_mark = init_mark
        write_benchmark_csv(benchmark, file_for_benchmark, time_out, False)
        benchmarks.append(copy(benchmark))
        num_of_petri_nets -= 1
        if time.time() - init_time > time_to_finish:
            break
        if len(benchmarks) % 100 == 0:
            sendEmail("Subject: partial \n\n " + " number of Petri nets done: " + str(len(benchmarks)))
    sendEmail("Subject: Done \n\n " + summary_of_rand_run(benchmarks, dir_run))


def sendEmail(summary):
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    print(summary)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("igor.mail.servies@gmail.com", "toFill")
        # TODO: Send email here
        server.sendmail("igor.mail.servies@gmail.com", "igor.khme@gmail.com", summary)


def is_petri_stractually_bounded(petri: PetriNet):
    trans_var = []
    strictly_greater_constrain = []
    dim = petri.get_dim()
    trans = petri.get_transitions()

    solver = z3.Solver()

    for i in range(len(trans)):
        name = "t" + i.__str__()
        trans_var.append(z3.Int(name))

    first = True
    for p in range(dim):
        terms = []
        for t in range(len(trans)):
            terms.append((trans[t].get_incidence())[p] * trans_var[t])

        # terms = ([c * x for (c, x) in zip(constants, trans_var)])
        sum = z3.Sum(terms)
        if first:
            temp = sum >= 0
            first = False
        else:
            temp = z3.And(temp, sum >= 0)

        strictly_greater_constrain.append(sum > 0)

    solver.add(temp)
    solver.add(z3.Or(strictly_greater_constrain))
    above_zero = [x >= 0 for x in trans_var]
    solver.add(above_zero)
    n = 0
    if solver.check() != z3.sat:
        return True
    return False


def summary_of_rand_run(benchmarks, dir_run):
    total_time = 0
    total_final_vertices = 0
    total_final_accelerations = 0
    total_max_vertices = 0
    total_max_accelerations = 0
    total_accelerations_used = 0
    total_time_out = 0
    summary = ""
    for benchmark in benchmarks:
        if not benchmark.timeout:
            total_time += benchmark.time
            total_max_vertices += benchmark.max_vertices
            total_max_accelerations += benchmark.max_accelerations
            total_accelerations_used += benchmark.used_accelerations
            total_final_accelerations += benchmark.final_accelerations
            total_final_vertices += benchmark.final_vertices
        else:
            total_time_out += 1
    f = open(dir_run + "summary", "a")

    def writeboth(file, summarytext: str, massage: str):
        file.write(massage)
        return summarytext + massage

    summary = writeboth(f, summary, "--------------------------------------\n")
    summary = writeboth(f, summary, "Summary of this random batch:\n")
    summary = writeboth(f, summary, "--------------------------------------\n\n")
    summary = writeboth(f, summary, "Num of benchmarks: %d \n" % len(benchmarks))
    summary = writeboth(f, summary, "Total time: %f \n" % total_time)
    summary = writeboth(f, summary, "Num of benchmarks timeout: %d \n" % total_time_out)
    summary = writeboth(f, summary, "Total num of maximum Vertices : %d \n" % total_max_vertices)
    summary = writeboth(f, summary, "Total num of maximum accelerations : %d \n" % total_max_accelerations)
    summary = writeboth(f, summary, "Total num of accelerations used : %d \n" % total_accelerations_used)
    summary = writeboth(f, summary, "Total num of final accelerations : %d \n" % total_final_accelerations)
    summary = writeboth(f, summary, "Total num of final vertices : %d \n" % total_final_vertices)
    f.close()

    return summary


def all_connected_components(petri: PetriNet):
    connected_components = []
    for tran in petri.get_transitions():
        tran_component = set()
        for p in range(petri.get_dim()):
            if (tran.get_pre()[p] != 0) | (tran.get_incidence()[p] != 0):
                tran_component = tran_component.union(set([p]))
                for component in connected_components:
                    if p in component:
                        tran_component = tran_component.union(component)
                        connected_components.remove(component)
        connected_components.append(tran_component)
    return connected_components


def projection_of_petri_on_places(petri: PetriNet, places: {int}):
    new_dim = len(places)
    petri_new = PetriNet(len(places))
    for tran in petri.get_transitions():
        new_pre = np.zeros(new_dim)
        new_incidence = np.zeros(new_dim)
        old_pre = tran.get_pre()
        old_incidence = tran.get_incidence()
        new_p = 0
        for old_p in places:
            new_pre[new_p] = old_pre[old_p]
            new_incidence[new_p] = old_incidence[old_p]
            new_p += 1
        petri_new.add_transition(OmegaTransition(new_pre, new_incidence))
    return petri_new
