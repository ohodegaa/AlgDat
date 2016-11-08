__author__ = 'ohodegaa'

from sys import stdin, stderr


def best_path(nm, prob):
    ancestors = []

    for i in range(len(nm)):
        neighbours = []
        for j in range(len(nm[i])):
            if nm[i][j]:
                neighbours.append(i)
                nm[i][j] = prob[i] * prob[j]
            else:
                neighbours.append(None)
        ancestors.append(neighbours)

    for k in range(len(nm)):
        for i in range(len(nm)):
            for j in range(len(nm[i])):
                if nm[i][k] * nm[k][j] > nm[i][j]:
                    nm[i][j] = nm[i][k] * nm[k][j]
                    ancestors[i][j] = ancestors[k][j]
    return print_path(ancestors, 0, len(nm) - 1, "")


def print_path(ancestors, i, j, s):
    if i == j:
        return s + str(i)
    elif ancestors[i][j] is None:
        return "0"
    else:
        return print_path(ancestors, i, ancestors[i][j], s) + s + "-" + str(j)


n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print(best_path(neighbour_matrix, probabilities))
