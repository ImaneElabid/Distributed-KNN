from itertools import islice

from collections import OrderedDict

from ..similarities import similarity


def get_knn(graph, k, similarity_type=1):
    """
    Calculate the k nearest nieghbours for each node in a given graph
    using a brute force algorithm to explore all possibilities.
    Args:
        graph (list): a graph of nodes.
        k (int): the number of required neighbours.
        similarity_type (int): similarty type.

    Returns:
        list: graph where each node has k optimal neighbours
    """
    for current_node in graph:
        neighbours = {}
        for node in graph:
            if current_node.id != node.id:
                neighbours.update({node: similarity(current_node.profil, node.profil, similarity_type)})
                neighbours = dict(islice(OrderedDict(sorted(neighbours.items(), key=(lambda x: x[1]))).items(), k))
                current_node.neighbours = neighbours

    return graph


def print_knn(graph):
    # print knn graph along with its neighbours
    for node in graph:
        print(node)
        for k, v in node.neighbours.items():
            print(f"    {k} : {v}")
