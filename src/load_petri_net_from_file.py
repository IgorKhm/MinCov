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
import re
import xml.etree.ElementTree as ET

import numpy as np
import numpy.matlib

from omega_transition import OmegaTransition
from petri_net import PetriNet


def add_transition(petri_net, places, rule):
    pos = rule.find('->')
    guards_str = rule[:pos]
    updates_str = rule[pos + 2:]
    guards = {}
    updates = {}

    # Parse guards
    for guard in guards_str.split(','):
        var, value = guard.split('>=')

        guards[var.strip()] = int(value)

    # Parse updates
    for update in updates_str.split(','):
        match = re.search('\s*(.*)\'\s*=\s*(.*)\s*(\+|-)\s*(.*)\s*',
                          update)  # xi' = xj {+,-} value

        if match is not None:
            var_in = match.group(1).strip()
            var_out = match.group(2).strip()
            value = int(match.group(3) + match.group(4))

            if var_in != var_out:
                raise ValueError('x_i\' = x_j + c illegal with i != j')

            updates[var_in] = value

    # Add transition
    pre_vec = numpy.zeros(len(places))
    incidence_vec = numpy.zeros(len(places))
    for p in range(len(places)):
        guard = guards[places[p]] if places[p] in guards else 0
        update = updates[places[p]] if places[p] in updates else 0
        pre, incidence = guard, update

        # Add value to sparse matrix if necessary
        if pre != 0:
            pre_vec[p] = pre

        if incidence != 0:
            incidence_vec[p] = incidence

    petri_net.add_transition(OmegaTransition(pre_vec, incidence_vec))


def add_constraints(data, places_indices, constraints_list):
    COMPARISONS = ['>=', '=']  # List order matters here.
    entries = data.split(',')

    # Parse constraints
    for rule in entries:
        for comparison in COMPARISONS:
            if comparison in rule:
                place, value = rule.strip().split(comparison)
                place = place.strip()
                value = int(value)

                constraints_list[places_indices[place]] = (comparison,
                                                           value)

                break  # Important, '=' appears in '>=' so would parse twice

    # Return trailing incomplete constraint
    if len([comp for comp in COMPARISONS if comp in entries[-1]]) == 0:
        return entries[-1]
    else:
        return ''


def add_initial_mark(data, places_indices, init):
    COMPARISONS = ['>=', '=']  # List order matters here.
    entries = data.split(',')

    # Parse constraints
    for rule in entries:
        for comparison in COMPARISONS:
            if comparison in rule:
                place, value = rule.strip().split(comparison)
                place = place.strip()
                value = float(value)
                if comparison == COMPARISONS[0]:
                    value = float("inf")

                init[places_indices[place]] = value

                break  # Important, '=' appears in '>=' so would parse twice

    # Return trailing incomplete constraint
    if len([comp for comp in COMPARISONS if comp in entries[-1]]) == 0:
        return entries[-1]
    else:
        return ''

def add_initial_target(data, places_indices, init):
    COMPARISONS = ['>=', '=']  # List order matters here.
    entries = data.split(',')

    # Parse constraints
    for rule in entries:
        for comparison in COMPARISONS:
            if comparison in rule:
                place, value = rule.strip().split(comparison)
                place = place.strip()
                value = float(value)
                # if comparison == COMPARISONS[0]:
                #     value = float("inf")

                init[places_indices[place]] = value

                break  # Important, '=' appears in '>=' so would parse twice

    # Return trailing incomplete constraint
    if len([comp for comp in COMPARISONS if comp in entries[-1]]) == 0:
        return entries[-1]
    else:
        return ''

def load_petri_net_from_spec(filename, withTarget = False):
    MODES = ['vars', 'rules', 'init', 'target', 'invariants']
    num_places = 0
    places = []

    with open(filename) as input_file:
        for row in input_file:
            if row.strip() == MODES[0]:
                data = (next(input_file)).strip()
                num_places = len(data.split(' '))
                break
    petri = PetriNet(num_places)

    with open(filename) as input_file:
        mode = 'none'
        rules_acc = ''
        acc = ''
        taracc = ''
        init_mark = numpy.zeros(num_places)
        target = numpy.zeros(num_places)

        for row in input_file:
            data = row.strip()

            # Ignore empty/commented lines
            if len(data) == 0 or data[0] == '#':
                continue

            if data in MODES:
                mode = data
                if mode == MODES[1]:
                    places_indices = {value: key for key, value in
                                      enumerate(places)}
            else:
                # Places
                if mode == MODES[0]:
                    places.extend(data.split(' '))
                # Rules
                elif mode == MODES[1]:
                    rules_acc += data
                    pos = rules_acc.find(';')

                    if pos >= 0:
                        add_transition(petri, places, rules_acc[:pos])
                        rules_acc = rules_acc[pos + 1:]
                # Initial values
                elif mode == MODES[2]:
                    acc = add_initial_mark(acc + data, places_indices, init_mark)
                #                     print(init_mark)
                # Target values
                elif mode == MODES[3]:
                    taracc= add_initial_target(taracc + data, places_indices, target)
                    # print("")
                    # currently don't care about the target

    petri.mark_the_petri_net(init_mark)
    if withTarget:
        return petri, target
    else:
        return petri


def load_petri_net_from_pnml(filename):
    places_names = []
    transitions_names = []
    pre_transitions = []
    incidence_transitions = []
    init_marking = []

    tree = ET.parse(filename)
    root = tree.getroot()
    net = root.find("{http://www.pnml.org/version-2009/grammar/pnml}net").find(
        "{http://www.pnml.org/version-2009/grammar/pnml}page")

    for place in net.iter('{http://www.pnml.org/version-2009/grammar/pnml}place'):
        places_names.append(place.attrib["id"])
        init = place.find("{http://www.pnml.org/version-2009/grammar/pnml}initialMarking")
        if init is None:
            init_marking.append(0)
        else:
            i = init.find("{http://www.pnml.org/version-2009/grammar/pnml}text").text
            init_marking.append(int(i))

    dim = len(places_names)

    for tran in net.iter('{http://www.pnml.org/version-2009/grammar/pnml}transition'):
        transitions_names.append(tran.attrib["id"])
        pre_transitions.append(numpy.zeros(dim))
        incidence_transitions.append(numpy.zeros(dim))

    for arc in net.iter('{http://www.pnml.org/version-2009/grammar/pnml}arc'):
        source = arc.attrib["source"]
        target = arc.attrib["target"]
        if source in places_names:
            p = places_names.index(source)
            t = transitions_names.index(target)
            pre_transitions[t][p] += 1
        else:
            p = places_names.index(target)
            t = transitions_names.index(source)
            incidence_transitions[t][p] += 1

    petri_net = PetriNet(dim)
    petri_net.mark_the_petri_net(np.array(init_marking))

    for i in range(len(transitions_names)):
        petri_net.add_transition(OmegaTransition(pre_transitions[i], incidence_transitions[i]))

    return petri_net


def load_marking_from_mp(filename):
    markings = []
    with open(filename) as input_file:
        for row in input_file:
            mark = []
            data = row.strip()
            data = data.strip('(')
            data = data.strip(')')
            data = data.strip()
            entries = data.split(',')
            for entry in entries:
                if entry == ' inf':
                    mark.append(float('inf'))
                else:
                    try:
                        mark.append(float(entry))
                    except:
                        print()
            markings.append(mark)
    return markings


def marking_of_x():
    markings = []
    markings.append([1, 2, 3])
