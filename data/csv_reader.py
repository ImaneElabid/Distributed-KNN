import pandas as pd

from algorithms.node import Node


def reader(file, indexes=(2, 3, 4, 5, 6)):
    """
    Reads data from a csv file and return a graph 
    """
    df = pd.read_csv(file)
    graph = []
    for index, row in df.iterrows():
        node_profile = []
        try:
            for i in indexes:
                node_profile.append(row[i])
        except:
            pass
        graph.append(Node(index, node_profile))
    return graph

if __name__ == '__main__':
    graph = reader("/home/karim/Workspace/github.com/me/iko/datasets/data.csv")
    print(graph.size())
