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
import time

import gc
from cover_tree_with_tests import CovTreeHashTest
from load_petri_net_from_file import load_petri_net_from_spec

fieldnames = ['Name', '#transitions', '#places', '#Max vertices', '#Final vertices', '#Max acc', '#Final acc',
              '#Accs reused', 'Time', 'Num comparisons']

fieldnamesqc = ['name', 'time', 'cover']


class Benchmark:
    def __init__(self, name):
        self.name = name
        self.max_vertices = 0
        self.max_accelerations = 0
        self.final_vertices = 0
        self.final_accelerations = 0
        self.used_accelerations = 0
        self.time = 0
        self.places = 0
        self.transitions = 0
        self.clover = None
        self.timeout = False
        self.init_mark = None
        self.num_of_comparisons = 0
        self.num_of_recheck = 0


def write_benchmark_csv(benchmark, filename, time_out, write_clover=False):
    with open(filename, mode='a') as employee_file:
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)

        # writer.writeheader()
        if benchmark.timeout:
            time = "timeout"
        else:
            time = "%.3f" % benchmark.time
        writer.writerow({'Name': benchmark.name, '#transitions': benchmark.transitions, '#places': benchmark.places,
                         '#Max vertices': benchmark.max_vertices, '#Final vertices': benchmark.final_vertices,
                         '#Max acc': benchmark.max_accelerations, '#Final acc': benchmark.final_accelerations,
                         '#Accs reused': benchmark.used_accelerations, 'Time': time,
                         'Num comparisons': benchmark.num_of_comparisons})


def run_benchmark(name, petri, time_out, init_marking=None, with_acc=True):
    benchmark = Benchmark(name)

    print("starting %s" % name)
    start_time = time.time()
    if init_marking is None:
        cov = CovTreeHashTest(petri, petri.get_mark())
    else:
        cov = CovTreeHashTest(petri, init_marking)
    cov.keep_accelerations = with_acc
    cov.type_of_graph_traversal = "DFS"
    cov.use_z3_to_guess_accelerations = False
    cov.check_for_correctness = False
    cov.verbose = True
    cov.timeout = time_out

    benchmark.clover = cov.generate_cov_tree()

    benchmark.timeout = benchmark.clover is None

    elapsed_time = time.time() - start_time
    benchmark.max_vertices = cov.max_size
    benchmark.max_accelerations = cov.max_size_of_acc
    benchmark.final_accelerations = len(cov._accelerations)
    benchmark.final_vertices = len(cov._verSet)
    benchmark.used_accelerations = cov.use_of_acc
    benchmark.time = elapsed_time
    benchmark.places = len(petri.get_places())
    benchmark.transitions = len(petri.get_transitions())
    benchmark.num_of_comparisons = cov.num_of_comparisons
    benchmark.num_of_recheck = cov.num_of_rechecks

    return benchmark, cov


def run_benchmarks(Benchfolder="../benchmarks/", withacc=True):
    bench_ran = 0
    timed_out = 0
    timed_out_list = []
    finished = []
    totaltime = 0
    timestamp_str = datetime.datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    os.makedirs("../results/" + timestamp_str)
    with open("../results/" + timestamp_str + "/results.csv", mode='a') as employee_file:
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        writer.writeheader()

    times = [900]
    for time_out in times:
        for folder in os.walk(Benchfolder):
            for file in os.listdir(folder[0]):
                if not file.endswith(".spec"):
                    continue
                if (folder[0] + file) in finished:
                    continue

                petri = load_petri_net_from_spec(folder[0] + "/" + file)

                if file.title() == "Main.Spec":
                    name = str(folder[0].rsplit('/', 1)[1])
                else:
                    name = file.title()

                benchmark, cov = run_benchmark(name, petri, time_out, None, withacc)

                filename = "../results/" + timestamp_str + "/results.csv"

                write_benchmark_csv(benchmark, filename, time_out)
                bench_ran += 1
                print("bench ran: %d" % bench_ran)
                anti = None
                cov = None
                petri = None

                gc.collect()
                file_id = folder[0] + file
                if benchmark.timeout:
                    if file_id not in timed_out_list:
                        timed_out += 1
                        timed_out_list.append(file_id)
                else:
                    totaltime += benchmark.time
                    if file_id in timed_out_list:
                        finished.append(file_id)
                        timed_out_list.remove(file_id)

                print("finished %s" % file.title())
        email_message = ""
        print("----------------------------------------")
        email_message += "----------------------------------------\n"
        print("----------------------------------------")
        email_message += "----------------------------------------\n"
        print("----------------------------------------")
        email_message += "----------------------------------------\n"
        print("Number of Done = %d" % len(finished))
        email_message += "Number of Done = %d \n" % len(finished)
        print("Total time = %f" % totaltime)
        email_message += "Total time = %f \n" % totaltime
        print("Number of Timed Out = %d \n" % timed_out)
        email_message += "Number of Timed Out: %d \n" % timed_out
        print("timeout time = %d" % time_out)
        email_message += "timeout time = %d \n" % time_out
        for file in timed_out_list:
            email_message += str(file) + "\n"
            print(file)

        print("----------------------------------------")
        email_message += "----------------------------------------\n"
        print("----------------------------------------")
        email_message += "----------------------------------------\n"
        print("----------------------------------------")
        email_message += "----------------------------------------\n"


def run_coverBenchmarks():
    finished = []
    timestamp_str = datetime.datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    os.makedirs("benchmarks/qcover/results/usandqcover/" + timestamp_str)
    with open("benchmarks/qcover/results/usandqcover/" + timestamp_str + "/results-us.csv", mode='a') as employee_file:
        writer = csv.DictWriter(employee_file, fieldnames=fieldnamesqc)
        writer.writeheader()

    times = [900]
    for time_out in times:
        for folder in os.walk("benchmarks/qcover/benchmarks"):
            for file in os.listdir(folder[0]):
                if not file.endswith(".spec"):
                    continue
                if (folder[0] + file) in finished:
                    continue

                # petri order_transitions()
                # # the names in wahl-kroening are in the folder name and not the file
                if file.title() == "Main.Spec":
                    name = str(folder[0].rsplit('/', 1)[1])
                else:
                    name = file.title()

                print("starting %s" % name)

                try:
                    petrinet, target = load_petri_net_from_spec(folder[0] + "/" + file, True)
                except:
                    print("error loading")
                    with open("benchmarks/qcover/results/usandqcover/" + timestamp_str + "/results-us.csv",
                              mode='a') as employee_file:
                        writer = csv.DictWriter(employee_file, fieldnames=fieldnamesqc)
                        writer.writerow(
                            {'name': name, 'time': "loading Problem", 'cover': "not relevant"})

                print("loaded petri net")
                start_time = time.time()
                try:
                    result = None
                    cov = CovTreeHashTest(petrinet, petrinet.get_mark())
                    cov.keep_accelerations = True
                    cov.timeout = time_out
                    result = cov.check_for_cover(target, folder[0] + "/" + file)
                except:
                    final_time = "%.3f" % (time.time() - start_time)
                    print("actual time:%s" % final_time)
                    final_time = "time_out"

                if result is None:
                    final_time = "time_out"
                    cover = ""
                else:
                    # final_time = (time.time() - start_time)
                    final_time = "%.3f" % (time.time() - start_time)
                    if result:
                        cover = "covered"
                    else:
                        cover = "not covered"

                with open("benchmarks/qcover/results/usandqcover/" + timestamp_str + "/results-us.csv",
                          mode='a') as employee_file:
                    writer = csv.DictWriter(employee_file, fieldnames=fieldnamesqc)
                    writer.writerow(
                        {'name': name, 'time': final_time, 'cover': cover})

                print(cover)
                print("time : %s" % str(final_time))
                print("finished %s" % name)
                # benchmark = run_benchmark(name, petri, time_out, None)

