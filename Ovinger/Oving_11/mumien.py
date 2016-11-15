__author__ = 'ohodegaa'

from sys import stdin, stderr


def best_path(nm, prob):
    return dijkstra(nm, prob)


def dijkstra(nm, prob):
    n = len(nm)             # nm er en n x n -matirse
    visited = [False] * n   # ei liste som holder styr på hvilke noder som er besøkt
    ancestors = [-1] * n    # for å finne veien som er mest sannsynlig trenger vi ei liste som holder styr
                            # på ancestor til enhver node (ancestor[i] angir noden som er forelder til node i
    k_prob = [0.0] * n      # den kummulative sannsynligheten for at veien går fra node 0 til node i
    k_prob[0] = prob[0]     # det er prob[0] sannsynlig het for å komme til startnoden
    next_node = 0
    for i in range(n):
        node = next_node
        visited[node] = True    # vi har nå besøkt node
        maxi_prob = -1.0
        for adj in range(n):    # vi ønsker her å finne naboen til node som vi mest sannsynlig vil besøke neste
            if not visited[adj]:    # som vi ikke har besøkt før
                if nm[node][adj] * k_prob[node] * prob[adj] > k_prob[adj]:
                    k_prob[adj] = k_prob[node] * prob[adj]          # oppdaterer sannssynlighet for å komme seg til
                    ancestors[adj] = node                           # denn naboen
                if k_prob[adj] > maxi_prob:
                    next_node = adj
                    maxi_prob = k_prob[adj]
        if next_node == n - 1:
            break
    return print_path(ancestors, 0, n - 1)


def print_path(ancestors, i, j, s=""):
    if i == j:
        return s + str(j)
    elif ancestors[j] == -1:
        return "0"
    else:
        return print_path(ancestors, i, ancestors[j], s) + "-" + str(j)

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
