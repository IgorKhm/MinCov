"""
Copyright 2019 Igor Khmelnitsky, Alain Finkel, Serge Haddad

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import csv
import datetime
import os
import smtplib
import ssl
import time
import uuid
from copy import deepcopy

import numpy as np
from omega_transition import OmegaTransition
from performance import run_benchmark, Benchmark, write_benchmark_csv
from petri_net import PetriNet
from z3 import z3


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


def export_petri_to_spec(petri_net: PetriNet, filename, write_initial_marking=False):
    file = open(filename, "a")
    place_names = []
    for p in petri_net.get_places():
        place_names.append("x" + str(p))

    file.write("vars\n\t")
    for place in place_names:
        file.write(place + " ")

    file.write("\n\nrules\n")
    for tran in petri_net.get_transitions():
        pre = tran.get_pre()
        first = True
        for p in petri_net.get_places():
            if pre[p] > 0:
                if first:
                    file.write("\t")
                else:
                    file.write(" , ")
                file.write(place_names[p] + " >= " + str(int(pre[p])))
                first = False
        file.write(" ->\n")
        first = True
        incidence = tran.get_incidence()
        for p in petri_net.get_places():
            if incidence[p] != 0:
                if not first:
                    file.write(",\n")
                if incidence[p] > 0:
                    file.write("\t\t" + place_names[p] + "' = " + place_names[p] + "+" + str(int(incidence[p])))
                else:
                    file.write("\t\t" + place_names[p] + "' = " + place_names[p] + "-" + str(int(incidence[p]) * (-1)))
                first = False
        file.write(";\n\n")
    if not write_initial_marking:
        file.close()
        return

    file.write("init\n\t")
    first = True
    init_mark = (petri_net.get_mark())
    for p in petri_net.get_places():
        if not first:
            file.write(" , ")
        if init_mark[p] == float("inf"):
            file.write(place_names[p] + " >= 1")
        else:
            file.write(place_names[p] + " = " + str(int(init_mark[p])))
        first = False
    file.close()


fieldnames = ['Name', '#transitions', '#places', '#Max vertices', '#Final vertices', '#Max acc', '#Final acc',
              '#Accs reused', 'Time']


def generate_petri_nets():
    init_time = time.time()

    num_of_petri_nets = 200
    num_of_init_markings = 5
    time_out = 900
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
        petrinet_ran = False
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

        dir_for_petri = dir_run + "/" "_p_" + str(petri.get_dim()) + "_t_" + str(
            len(petri.get_transitions())) + "_d_" + timestamp_str + "_" + str(num_of_petri_nets)
        os.makedirs(dir_for_petri)

        benchmark = Benchmark("empty")
        max_num_of_tries = 300
        current_try = 0
        benchmark.max_vertices = 0
        benchmark.timeout = False
        while benchmark.max_vertices < 50:
            current_try += 1
            marking = np.zeros(petri.get_dim())
            # max_norm = petri.get_dim() / 2
            norm_of_init_marking = np.random.randint(1, petri.get_dim() / 2)
            for p in range(norm_of_init_marking):
                marking[np.random.randint(0, int(petri.get_dim() - 1))] += 1
            init_mark = marking
            id = str(uuid.uuid1())
            petri_name = file_name_petri + id + ".spec"
            benchmark = run_benchmark(petri_name, petri, time_out, init_mark,False)
            if current_try > max_num_of_tries:
                break
        if current_try > max_num_of_tries:
            continue

        print("write")
        petri.mark_the_petri_net(init_mark)
        export_petri_to_spec(petri, dir_for_petri + petri_name, True)
        benchmark.init_mark = init_mark
        write_benchmark_csv(benchmark, file_for_benchmark, time_out, False)
        benchmarks.append(deepcopy(benchmark))
        num_of_petri_nets -= 1
    summary_of_rand_run(benchmarks, dir_run)

    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("igor.mail.servies@gmail.com", "@think1964")
        # TODO: Send email here
        server.sendmail("igor.mail.servies@gmail.com", "igor.khme@gmail.com", "Subject: Done")


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

    f.write("--------------------------------------\n")
    f.write("Summary of this random batch:\n")
    f.write("--------------------------------------\n\n")
    f.write("Num of benchmarks: %d \n" % len(benchmarks))
    f.write("Total time: %f \n" % total_time)
    f.write("Num of benchmarks timeout: %d \n" % total_time_out)
    f.write("Total num of maximum Vertices : %d \n" % total_max_vertices)
    f.write("Total num of maximum accelerations : %d \n" % total_max_accelerations)
    f.write("Total num of accelerations used : %d \n" % total_accelerations_used)
    f.write("Total num of final accelerations : %d \n" % total_final_accelerations)
    f.write("Total num of final vertices : %d \n" % total_final_vertices)
    f.close()


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
