import matplotlib
import matplotlib.pyplot as plt


def plot(precisions):
    x = list(range(1, len(precisions)+1))
    y = precisions
    plt.plot(x, y, color='orange')
    plt.xlabel('iterations')
    plt.ylabel('precision')
    plt.title('Precision plot')
    plt.show()
