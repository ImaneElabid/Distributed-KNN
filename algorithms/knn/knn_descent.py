from random import sample

from .precision import precision
from ..similarities import similarity


def get_knn(graph, k, similarity_type=1, bf_graph=None):
    """
    Calculate the k nearest nieghbours for each node in a given graph
    using a a descent algorithm where each node defines k random neighbours
    and tries to optimize its neighbours using an update function using a
    similarity measure.
    Args:
        graph (list): a graph of nodes.
        k (int): the number of required neighbours.
        similarity_type (int): similarty type.
        bf_graph (list): the generated brute force graph used in precision calculation 

    Returns:
        list: graph where each node has k neighbours
    """

    # Taking :k random neighbour for each node
    _set_random_neighbours(graph, k)
    # precision list contains knn_descent precision for every iteration
    precisions = []

    while True:
        # reverse calculation for all the node
        _revers(graph)
        # generate  general neighbours
        for node in graph:
            node.set_general_neighbours()

        # initiating the counter for the updated neighbours
        c = 0
        for node in graph:
            # print(node.reverse)
            for node_u in node.general_neighbours:
                if node in node_u.general_neighbours:
                    node_u.general_neighbours.remove(node)
                for node_v in node_u.general_neighbours:
                    # looking for neighbours in my neighbours neighbours
                    distance = similarity(node.profil, node_v.profil, similarity_type)
                    c = c + _update_nn(node, node_v, distance)
        if bf_graph is not None:
            precisions.append(precision(bf_graph, graph))

        if c == 0:
            break

    return graph, precisions


def _set_random_neighbours(nodes, k):
    for node in nodes:
        neighbours_dict = {}
        other_nodes = [n for n in nodes if n != node]
        nb = sample(other_nodes, k)
        for n in nb:
            neighbours_dict.update({n: similarity(node.profil, n.profil)})
        node.neighbours = neighbours_dict


def _revers(nodes):
    for node in nodes:
        node.reverse = []
    for node in nodes:
        # declare my self as a revers for my neighbours
        node.set_neighbours_revers()


def _update_nn(node, node_v, distance):
    if node_v in node.neighbours:
        # :node_v is already in the neighbours no change needed
        return 0
    else:
        # getting the farthest neighbours to :node in it list of nodes
        farest_neighbour = node.get_farest_neighbour()
        # checking if :node_v is closer than the farthest neighbour
        if distance < farest_neighbour[1]:
            # if it's the case replace the farthest by the new one
            node.neighbours.pop(farest_neighbour[0])
            node.neighbours.update({node_v: distance})
            return 1
        else:
            # if it's not, no changes required.
            return 0


def print_knn(graph):
    # print knn graph along with its neighbours
    for node in graph:
        print(node)
        for k, v in node.neighbours.items():
            print(f"    {k} : {v}")
