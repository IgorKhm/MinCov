"""
Created on Jul 10, 2019

@author: ikhmelnitsky
"""
import datetime
import os

import numpy as np

from load_petri_net_from_file import load_petri_net_from_spec
from petri_net import PetriNet


def export_petri_to_MP(petri_net: PetriNet, filename, name):
    file = open(filename, "a")

    # file.write("samples = []")
    # file.write("omega = float('inf')")
    # file.write("def Init():")

    file.write("#======================================\n")
    file.write("#======== %s ==============\n" % name)
    file.write("#======================================\n")

    file.write("tplus = []\n")
    file.write("tmin = []\n")
    i = 0
    for tran in petri_net.get_transitions():
        file.write("#t%d\n" % i)
        i += 1
        file.write("tplus += [[")
        is_first = True
        for p2 in (tran.get_incidence() + tran.get_pre()):
            if p2 < 0:
                p2 = 0
            # p2 = int(p2*(-1))
            if is_first:
                is_first = False
                file.write("%d" % p2)
                continue
            file.write(", %d" % p2)

        file.write("]]\n")

        file.write("tmin += [[")
        is_first = True
        for p in tran.get_pre():
            if p < 0:
                p = 0
            if is_first:
                is_first = False
                file.write("%d" % p)
                continue
            file.write(", %d" % p)

        file.write("]]\n")

    file.write("t0 = [")
    is_first = True
    for p in petri_net.get_mark().get_marking():
        if not is_first:
            file.write(", ")
        else:
            is_first = False
        if p == float("inf"):
            file.write("omega")
        else:
            file.write("%d" % p)

    file.write("]\n")

    file.write("samples.append(Sample(\"%s\", tplus, tmin, t0, None)) \n" % name)

    file.write("#======================================\n")
    file.write("#================END===================\n")
    file.write("#======================================\n")

    file.close()


def export_a_folder_to_MP(origin_folder, des_folder):
    filename = des_folder + "/" + "MP_translate"
    # file = open(filename, "a")
    # file.write("samples = [] \n omega = float('inf')\n def Init():\n")
    for folder in os.walk(origin_folder):
        for file in os.listdir(folder[0]):
            if not file.endswith(".spec"):
                continue
            print("translating %s" % file)
            petri = load_petri_net_from_spec(folder[0] + "/" + file)
            export_petri_to_MP(petri, filename, file)


def export_petri_to_valmari(petri_net: PetriNet, filename):
    file = open(filename, "a")

    # file.write("samples = []")
    # file.write("omega = float('inf')")
    # file.write("def Init():")
    file.write("%d %d \n" % (petri_net.get_dim(), len(petri_net.get_transitions())))

    trun_num = 1
    for tran in petri_net.get_transitions():

        place_num = 1
        for p in (tran.get_incidence() + tran.get_pre()):
            if p <= 0:
                place_num += 1
                continue
            file.write("-%d \n" % trun_num)
            file.write("0 %d \n" % p)
            file.write("%d \n" % place_num)
            place_num += 1
        place_num = 1
        for p in tran.get_pre():
            if p <= 0:
                place_num += 1
                continue
            file.write("%d \n" % place_num)
            file.write("0 %d \n" % p)
            file.write("-%d \n" % trun_num)
            place_num += 1
        trun_num += 1

    file.write("0 \n")

    place_num = 1
    for p in petri_net.get_mark():
        if p <= 0:
            place_num += 1
            continue
        if p == float("inf"):
            file.write("-32767 \n")
            file.write("%d \n" % place_num)
        else:
            file.write("-%d \n" % p)
            file.write("%d \n" % place_num)
        place_num += 1

    file.write("0 \n")
    file.close()


def export_a_folder_to_valmari(origin_folder):
    for folder in os.walk(origin_folder):
        for file in os.listdir(folder[0]):
            if not file.endswith(".spec"):
                continue
            print("translating %s" % file)
            if file.title() == "Main.Spec":
                name = str(folder[0].rsplit('/', 1)[1])
            else:
                name = file.title()
            petri = load_petri_net_from_spec(folder[0] + "/" + file)
            export_petri_to_valmari(petri, "benchmarks/valmari2/"+name)


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

