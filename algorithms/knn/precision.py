from ..node import Node


def precision(graph_bf, graph_desc):
    """
    calculate precision between the brute force generated graph and 
    the descent graph using the precision formula TP/(TP+FP)
    args:
        graph_bf (list): the knn brute force generated graph
        graph_bf (list): the knn descnet generated graph
    return:
        float: precision value
    """
    similar = 0
    size = 0
    for node in graph_desc:
        for node_a in node.neighbours.keys():
            size += 1
            bf_node = Node.get_node(graph_bf, node.id)
            if bf_node is None:
                break
            for node_b in bf_node.neighbours.keys():
                if node_b.id == node_a.id:
                    similar += 1

    return similar / size
