import copy

from data.csv_reader import reader
from viz import plot
from algorithms.knn import knn_brute_force
from algorithms.knn import knn_descent

# set the number of required neighbors
k = 5

# reding the csv file and genarating the graph.
graph = reader("./datasets/data.csv")

# generating brute force graph 
bf_graph = knn_brute_force.get_knn(copy.deepcopy(graph), k)

# get the knn graph and the precisions values 
knn_graph, precisions = knn_descent.get_knn(graph=graph, k=k, bf_graph=bf_graph)

# printing the k-neighbors 
knn_descent.print_knn(knn_graph)

# plotting the improvement of the precision in terms of update iterations
plot(precisions)
# print(precisions)