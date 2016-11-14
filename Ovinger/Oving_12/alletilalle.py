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