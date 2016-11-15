__author__ = 'ohodegaa'

"""
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
"""
def print_path(ancestors, i, j, s):
    if i == j:
        return s + str(i)
    elif ancestors[i][j] is None:
        return "0"
    else:
        return print_path(ancestors, i, ancestors[i][j], s) + s + "-" + str(j)




def print_D(D, k):
    print("D("+str(k)+")")
    for i in range(len(D)):
        print(D[i])

def floyd_warshall(nm):
    n = len(nm)
    D = [] + nm
    ancestors = []
    for i in range(len(nm)):
        neighbours = []
        for j in range(len(nm[i])):
            if nm[i][j] < 90:
                neighbours.append(i)
            else:
                neighbours.append(None)
        ancestors.append(neighbours)
    for k in range(n):
        print_D(D, k)
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    ancestors[i][j] = ancestors[k][j]
    print(print_path(ancestors, 0, 3, ""))


inf = 100
floyd_warshall([[0, 2, inf, inf, inf, inf],
                [inf, 0, 1, inf, 4, inf],
                [-2, inf, 0, inf, 2, inf],
                [inf, 4, inf, 0, inf, 3],
                [inf, inf, inf, 1, 0, 2],
               [inf, inf, inf, inf, inf, 0]])