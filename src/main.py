"""
Created on Jul 2, 2019

@author: ikhmelnitsky
"""
from cover_tree import CovTree
from load_petri_net_from_file import load_petri_net_from_spec
from performance import run_benchmarks
from tree_old import CovTreeHashTest

if __name__ == '__main__':
    pass

petri_file = "/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/mincover/mist/PN/mesh3x2.spec"
petri, target = load_petri_net_from_spec(petri_file, True)

cov = CovTreeHashTest(petri, petri.get_mark())
cov.keep_accelerations = True
cov.verbose = True
# cov.check_for_correctness = False
cov.timeout = 900
cov.type_of_graph_traversal = 'DFS'
# # cov.use_z3_to_guess_accelerations = True
# # cov.z3_timeout = 15
# # # cProfile.run('cov.generate_cov_tree()')
# # cProfile.run('cov.generate_cov_tree()')
# # anti_chain = cov.generate_cov_tree()
# # cov.check_for_cover(target, petri_file)
cov.generate_cov_tree()

quit()
petri_file = "/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/mincover/mist/PN/mesh3x2.spec"
petri, target = load_petri_net_from_spec(petri_file, True)

cov = CovTree(petri, petri.get_mark())
cov.keep_accelerations = True
cov.verbose = True
# cov.check_for_correctness = False
cov.timeout = 900
cov.type_of_graph_traversal = 'DFS'
# # cov.use_z3_to_guess_accelerations = True
# # cov.z3_timeout = 15
# # # cProfile.run('cov.generate_cov_tree()')
# # cProfile.run('cov.generate_cov_tree()')
# # anti_chain = cov.generate_cov_tree()
# # cov.check_for_cover(target, petri_file)
cov.generate_cov_tree()


run_benchmarks("/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/big_coverabillty","/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/big_coverabillty/results")
#
# n = PetriNet('First net')
# n.add_place(Place('p', [0]))
# n.add_transition(Transition('t', Expression('x<5')))
# n.add_input('p', 't', Variable('x'))
# n.add_output('p', 't', Expression('x+1'))
# print(n)


#
# #
# for i in range(5):
#     generate_petri_nets()
# export_a_folder_to_valmari("/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/random_petri_nets")





#
# for  node in cov._vertices:
#     print(node.marking)

# acc = cov._accelerations
# cov2 = CovTreeHashTest(petri, petri.get_mark())
# cov2.keep_accelerations = True
# cov2.verbose = True
# cov2.check_for_correctness = False
# cov2.verbose = True
# cov2.timeout = 900
# cov2.type_of_graph_traversal = 'MOST_TOKEN_FIRST'
# cov2._accelerations=cov._accelerations
# cov.use_z3_to_guess_accelerations = True
# cov.z3_timeout = 15
# # cProfile.run('cov.generate_cov_tree()')
# cProfile.run('cov.generate_cov_tree()')
# anti_chain = cov.generate_cov_tree()
# cov.check_for_cover(target, petri_file)
# cov2.generate_cov_tree()

# vis_tree_to_pdf(cov._vertices,"hello.gv",1000)
# g = Digraph('G', filename='hello.gv')
#
# sys.setrecursionlimit(1000000)
# def add_ver_and_children(node: CovNode, i=0):
#     if (i > 100):
#         print("too long")
#         return
#     for child in node.get_children():
#         # g.edge(str(node.marking), str(child.marking))
#         # g.edge(node.short_marking(), child.short_marking())
#         g.edge(node.name, child.name)
#         add_ver_and_children(child, i + 1)
#
#
# for v in cov._vertices:
#     if v.get_parent() is None:
#         root = v
#
# g.edge("root", root.name)
# add_ver_and_children(root)

#
#
# g.edge('Hello', 'World')
# g.edge('e1', 'e2')
# g.edge('e2', 'e3')
# g.edge('e3', 'e4')
# g.edge('e4', 'e5')
# g.edge('e1', 'e22')
# g.edge('e1', 'e23')
# g.edge('e1', 'e24')
# g.edge('e1', 'e25')


# print("-------------------------------------------------")

#
# cov1 = CovTreeHashTest(petri, petri.get_mark())
# cov1.keep_accelerations = False
# cov1.check_for_correctness = False
# anti_chain1 = cov1.generate_cov_tree()

#
# for node in anti_chain:
#     ok = False
#     for mark in markings:
#         if all(node.marking == mark):
#             ok = True
#     if not ok:
#         print("problem")


# # # #
# # print("with")
# # cov = CovTreeHash(petri, petri.get_mark().get_marking())
# # cov.keep_accelerations = True
# # cov.check_for_correctness = False
# # anti_chain = cov.generate_cov_tree()
# cov = CovTreeHashOld(petri_new, marking)
# cov.keep_accelerations = True
# cov.check_for_correctness = False
# anti_chain = cov.generate_cov_tree()
#
# arr1 = []
# arr2 = []
# arrU1 = []
# arrU2 = []
# for i in range(100000):
#     vec1 = np.random.randint(2, size=500)
#     vec2 = np.random.randint(2, size=500)
#
#     arr1.append(vec1.astype(float))
#     arr2.append(vec2.astype(float))
#     arrU1.append(vec1.astype(np.uint8))
#     arrU2.append(vec2.astype(np.uint8))

#
# repet = 100000000
#
# mysetup = '''
# import numpy as np
# vec1 = np.random.randint(2, size=500)
# vec2 = np.random.randint(2, size=500)
# vec1 = vec1.astype(np.uint8)
# vec2 = vec2.astype(np.uint8)
# less = np.less
#     '''
#
# # code snippet whose execution time is to be measured
# mycode = '''
# all(less(vec1, vec2))
#     '''
#
# # timeit statement
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#
# mycode = '''
# all(vec1 < vec2)
#     '''
#
# # timeit statement
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#
#
#
# mysetup = '''
# import numpy as np
# vec1 = np.random.randint(2, size=500)
# vec2 = np.random.randint(2, size=500)
# vec1 = vec1.astype(np.float64)
# vec2 = vec2.astype(np.float64)
# less = np.less
# '''
#
# mycode = '''
# all(less(vec1, vec2))
#     '''
#
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#
#
#
# mycode = '''
# all(vec1 < vec2)
# '''
#
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#
#
#
#
# mysetup = '''
# import numpy as np
# vec1 = np.random.randint(2, size=500)
# vec2 = np.random.randint(2, size=500)
# vec1 = vec1.astype(np.float)
# vec2 = vec2.astype(np.float)
# less = np.less
# '''
#
# mycode = '''
# all(less(vec1, vec2))
#     '''
#
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#
#
#
# mycode = '''
# all(vec1 < vec2)
# '''
#
# print(timeit.timeit(setup=mysetup,
#                     stmt=mycode, number=repet))
#

# initime = time.time()
# a = 0
# timeit.timeit("","3+4")
# for i in range(100000):
#     timeit.timeit("all(np.less(arr1[i], arr2[i]))")
#
# # print("time for float %f" % (time.time() - initime))
# print(a)
#
# a = 0
# initime = time.time()
# for i in range(100000):
#     a+= timeit.timeit(all(np.less(arrU1[i], arrU2[i])))
#     # if all(arrU1[i] < arrU2[i]):
# # print("time for uint %f" % (time.time() - initime))
# print(a)


# initime = time.time()
# a = 0
# for i in range(100000):
#     if all(np.less(arr1[i], arr2[i])):
#         a += 1
# print("time for float %f" % (time.time() - initime))
# print(a)
#
#
# b = np.array(arr1)
# c = np.array(arr2)
# initime = time.time()
# for i in range(100000):
#     a = np.apply_along_axis(np.positive(), 1, b-c)
#     if all(np.less(b[i], c[i])):
#         a += 1
# # a = np.apply_along_axis(my_func, 1, b)
# print("time for try %f" % (time.time() - initime))

# export_a_folder_to_MP("benchmarks/bug_tracking/", "benchmarks/")


# cProfile.run('cov.generate_cov_tree()')
#
# # # #
# petri = load_petri_net_from_spec(
#     "benchmarks/random_petri_nets_old/run-13-Aug-2019_18-08-01/_p_95_t_84_d_13-Aug-2019_18-08-01/petri_net.spec")
# # marking = np.array([0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
# #                     0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0,
# #                     0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# #                     1, 1, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 0, 2, 2, 0, 0, 0, 0])
# # #
# marking = np.array([0, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1,
#                     0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 0, 1, 0,
#                     1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 2,
#                     1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
# # #
# petri.mark_the_petri_net(OmegaMarking(marking))
# # # #
# # #
# # # covold = CovTreeHashOld(petri, petri.get_mark().get_marking())
# # # covold.use_z3_to_guess_accelerations = False
# # # covold.z3_timeout = 0.1
# # # covold.keep_accelerations = True
# # # # anti2 = covold.generate_cov_tree()
# # #
# # #
# cov = CovTreeHash(petri, petri.get_mark().get_marking())
# cov.use_z3_to_guess_accelerations = False
# cov.z3_timeout = 0.1
# cov.keep_accelerations = True
# anti2 = cov.generate_cov_tree()
#


# #
# #
# # cov = CovTreeHashOmega(petri, petri.get_mark().get_marking())
# # cov.use_z3_to_guess_accelerations = False
# # cov.z3_timeout = 0.1
# # cov.keep_accelerations = True
# # anti2 = cov.generate_cov_tree()
# # anti1 = cov.generate_cov_tree(False,False,OmegaMarking(marking))
# #
# # ini_in = False
# # for node1 in anti1:
# #     if all(marking <= node1.marking):
# #         print("true")
#
#
# # len_of_anti1 = len(anti1)
# # for node1 in anti1:
# #     antinew = cov.generate_cov_tree(False,False,node1.get_mark())
# #     for i in range(len_of_anti1):
# #         node3 = anti1[i]
# #         for node2 in antinew:
# #             if node3.get_mark() < node2.get_mark():
# #                 print("this1")
# #                 print(node1.get_mark().get_marking())
# #                 print(node2.get_mark().get_marking())
#
# #
# # for node1 in anti1:
# #     for node2 in anti2:
# #         if node1.get_mark() < node2.get_mark():
# #             print("this1")
# #             print(node1.get_mark().get_marking())
# #             print(node2.get_mark().get_marking())
# #
# # for node1 in anti2:
# #     for node2 in anti1:
# #         if node1.get_mark() < node2.get_mark():
# #             print("this2")
# #             print(node1.get_mark().get_marking())
# #             print(node2.get_mark().get_marking())
# #
# #
#
#
# # pref = Performance("benchmarks/
# # generate_Petri_nets()
# a = np.array([1, 2, 3, 4, float("inf")])
# print(a)
#
# # petri = load_petri_net_from_spec("benchmarks/mesh2x2.spec")
# cov = CovTreeHash(petri, petri.get_mark().get_marking())
# cov.timeout = 100
# cov.use_of_acc = True
# anti = cov.generate_cov_tree()
#
# # CS = [[1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
# #       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
# #       [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
# #       [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
# #       [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
# #       [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
# #       [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
# #       [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
# #       [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
# #       [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]]
# #
# # for a in CS:
# #     ok = False
# #     for b in anti:
# #         if all(a == b.marking):
# #             ok = True
# #     if not ok:
# #         print(a)
#
# export_petri_to_MP(petri, "testigoe", "rand2")
# run_coverBenchmarks()

# run_coverBenchmarks()
# rks("/home/ikhmelnitsky/Desktop/svn/min cover/min_cover_code/benchmarks/random", False)
# run_qcoverBenchmarks()
# cProfile.run('run_benchmarks()')

# cProfile.run('pref.run_benchmarks()')

#
# petri = load_petri_net_from_spec("benchmarks/x0_AA_q1.spec")
# cov = CovTreeHashOmegas(petri, petri.get_mark())
#
# anti_chain = cov.generate_cov_tree(True, petri.get_mark())
