"""
Created on Jul 9, 2019

@author: ikhmelnitsky
"""

from graphviz import Digraph

from node_cover_tree import CovNode


def vis_tree_to_pdf(vertices: [CovNode], filename,current, max_depth=200):
    graph = Digraph('G', filename=filename)
    # graph.subgraph()
    graph.node('', shape="plain", pos="200,200!")
    if len(vertices) == 1:
        graph.node(' ', shape="plain")
        if len(vertices[0].get_transitions()) > 1:
            graph.edge(" ", vertices[0].name, color="blue", label=str(len(vertices[0].get_transitions())),
                       fontsize="20",
                       fontcolor="blue")
        else:
            graph.edge(" ", str(vertices[0].marking))
    else:
        add_ver_and_children(vertices, graph, max_depth,current)
    graph.view()


def vis_trees(vertices: [CovNode], filename, max_depth=200, graph=None):
    if graph is None:
        graph = Digraph('G', filename=filename)
        add_ver_and_children(vertices, graph, max_depth)
    # graph.view()
    return graph


def add_ver_and_children(vertices: [CovNode], graph, max_depth,current):
    for node in vertices:
        if node._depth > max_depth:
            continue
        if node.get_parent() is None:
            graph.node(' ', shape="plain")
            if len(node.get_transitions()) > 1:
                graph.edge(" ", str(node.marking), color="blue", label=str(len(node.get_transitions())), fontsize="20",
                           fontcolor="blue")
            else:
                graph.edge(" ", str(node.marking))
        for child in node.get_children():
            # graph.edge(str(node.marking), str(child.marking))
            # graph.edge(node.short_marking(), child.short_marking())
            if current is not None:
                if all(child.marking == current.marking):
                    graph.node(str(child.marking), fontcolor="blue")
            if len(child.get_transitions()) > 1:
                print("asd")
                graph.edge(str(node.marking), str(child.marking), color="blue", label=str(len(child.get_transitions())), fontsize="20",
                           fontcolor="blue")
            else:
                graph.edge(str(node.marking), str(child.marking))
