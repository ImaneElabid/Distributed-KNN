class Node(object):
    """
    Creation of Node object defining its list of neighbors and behaviour
    """
    id = 0
    neighbours = {}
    reverse = []
    profil = []
    general_neighbours = []

    def __init__(self, id, profil):
        self.id = id
        self.profil = profil

    def __str__(self):
        return f"Node[{self.id}]"

    def add_neighbours(self, node, d):
        self.neighbours.update({node: d})

    def set_neighbours_revers(self):
        for n in self.neighbours.keys():
            n.add_revers(self)

    def add_revers(self, revers_node):
        self.reverse.append(revers_node)

    def set_general_neighbours(self):
        self.general_neighbours = list(set(list(self.neighbours.keys()) + self.reverse))

    def get_farest_neighbour(self):
        # dict(sorted(words.items(), key=lambda x: x[1]))
        # sorted(stats, key=(lambda key: stats[key]), reverse=True)
        # max(stats.items(), key=lambda x: x[1])
        # return dict([max(self.neighbours.items(), key=lambda x: x[1])]) # dict(Node: distance)
        return max(self.neighbours.items(), key=lambda x: x[1]) # tuple(Node, distance)

    @classmethod
    def get_node(cls, graph, id):
        for node in graph:
            if node.id == id:
                return node
        return Node


if __name__ == '__main__':
    # node = Node()
    print(__name__)

    # Node.get_node(graph, id)
