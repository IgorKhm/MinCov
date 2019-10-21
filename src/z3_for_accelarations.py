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
import time

import numpy as np
import z3
from omega_transition import OmegaTransition


def get_accelerations_from_z3(trans: [OmegaTransition], init_marking: np.array, timeout=1):
    time_start = time.time()
    trans_var = []
    strictly_greater_constrain = []
    dim = trans[0].get_dim()
    accelerations = []
    marking = init_marking
    if init_marking is None:
        marking = [0] * dim
    solver = z3.Solver()

    for i in range(len(trans)):
        name = "t" + i.__str__()
        trans_var.append(z3.Int(name))

    first = True
    for p in range(dim):
        if marking[p] == float("inf"):
            continue

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
    solver.add(z3.Sum(trans_var) <= 15)
    n = 0

    while time.time() - time_start < timeout:

        if solver.check() != z3.sat:
            break
        sol = solver.model()
        new_acc = from_solution_to_acceleration(sol, trans_var, trans, dim)
        to_add_the_new_acc = True

        num_of_acc = len(accelerations)
        for i in range(num_of_acc):
            acc = accelerations[num_of_acc - i - 1]
            if new_acc > acc:
                accelerations.remove(acc)
            if new_acc <= acc:
                to_add_the_new_acc = False
                break
        if to_add_the_new_acc:
            accelerations.append(new_acc)
        par = z3.Int("c" + n.__str__())
        n += 1
        not_the_same_answer = ([y != par * sol[y] for y in trans_var])
        solver.add(z3.Or(not_the_same_answer))
    return accelerations


def from_solution_to_acceleration(sol, trans_var, trans: [OmegaTransition], dim):
    fired_trans = [0] * len(trans)
    for i in range(len(trans_var)):
        fired_trans[i] = sol[trans_var[i]].as_long()

    pre = np.zeros(dim)
    incidence = np.zeros(dim)
    # index_trans = []
    # for i in range(len(trans_var)):
    #     index_trans.append(i)
    # random.shuffle(index_trans)
    # for i in index_trans:
    #     tran = trans[i]
    #     for j in range(fired_trans[i]):
    #         incidence = incidence + tran.get_incidence()
    #         for p in range(dim):
    #             if pre[p] - (tran.get_incidence())[p] < (tran.get_pre())[p]:
    #                 pre[p] = (tran.get_pre())[p]
    #             else:
    #                 pre[p] = pre[p] - (tran.get_incidence())[p]
    # for p in range(dim):
    #     if incidence[p] < 0:
    #         pre[p] = float("inf")
    #     if incidence[p] > 0:
    #         incidence[p] = float("inf")
    to_fire = []
    for t in range(len(fired_trans)):
        if fired_trans[t] > 0:
            to_fire.append([t, fired_trans[t]])

    while to_fire:
        n = np.random.randint(0, len(to_fire))
        t = to_fire[n][0]
        to_fire[n][1] -= 1
        if to_fire[n][1] == 0:
            to_fire.remove(to_fire[n])
        tran = trans[t]
        incidence = incidence + tran.get_incidence()
        for p in range(dim):
            if pre[p] - (tran.get_incidence())[p] < (tran.get_pre())[p]:
                pre[p] = (tran.get_pre())[p]
            else:
                pre[p] = pre[p] - (tran.get_incidence())[p]
    for p in range(dim):
        if incidence[p] < 0:
            pre[p] = float("inf")
        if incidence[p] > 0:
            incidence[p] = float("inf")

    return OmegaTransition(pre, incidence)
