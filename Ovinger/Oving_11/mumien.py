__author__ = 'ohodegaa'

from sys import stdin, stderr

def best_path(nm, prob):
    return dijkstra(nm, prob)

def dijkstra(nm, prob):
    n = len(nm)
    visited = [False]*n
    ancestors = [-1]*n
    k_prob = [prob[0]] + [0.0]*(n-1)
    next_node = 0
    for i in range(n):
        node = next_node
        visited[node] = True
        maxi_prob = -1.0
        for adj in range(n):
            if not visited[adj]:
                if nm[node][adj]*k_prob[node]*prob[adj] > k_prob[adj]:
                    k_prob[adj] = k_prob[node]*prob[adj]
                    ancestors[adj] = node
                    if k_prob[adj] > maxi_prob:
                        next_node = adj
                        maxi_prob = k_prob[adj]

        if next_node == n - 1:
            break
    anc = n - 1
    s = str(n - 1)
    while ancestors[anc] != -1:
        s = str(ancestors[anc]) + "-" + s
        anc = ancestors[anc]
    return s

def floyd_warshall(nm, prob):
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

#stdin = open("input_eksempel_01.txt")
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
