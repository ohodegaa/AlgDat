__author__ = 'ohodegaa'


def print_D(D, k):
    print("D(" + str(k) + ")")
    for i in range(len(D)):
        print(D[i])


def print_path(ancestors, i, j, s):
    if i == j:
        return s + str(i)
    elif ancestors[i][j] is None:
        return "0"
    else:
        return print_path(ancestors, i, ancestors[i][j], s) + s + "-" + str(j)


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
