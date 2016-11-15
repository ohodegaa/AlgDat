__author__ = 'ohodegaa'

from sys import stdin, maxsize

inf = 100


def shortest_path(order_list, am, cities):
    """
    Greia her er at vi må finne shortest path fra order_list[0] til order_list[1],
    fra order_list[1] til order_list[2] osv. og deretter shortest path fra
    order_list[-1] til order_list[0]

    Vi finner først shortest path fra alle til alle vha. Floyd-Warshall

    :param order_list: rekkefølgen byene skal besøkes i
    :param am: nabo-matrise
    :param cities: totalt antall byer
    :return: shortest path fra order_list[0] og tilbake til order_list[0], innom hver by i order_list

    """
    ancestors = []
    for i in range(cities):
        ciblings = []
        for j in range(cities):
            if am[i][j] > 0:
                ciblings.append(i)
            else:
                ciblings.append(None)
        ancestors.append(ciblings)

    for k in range(cities):
        for i in range(cities):
            for j in range(cities):
                if am[i][k] > 0 and am[k][j] > 0:
                    if am[i][k] + am[k][j] < am[i][j]:
                        am[i][j] = am[i][k] + am[k][j]
                        ancestors[i][j] = ancestors[k][j]

    return cost(ancestors, am, order_list + [order_list[0]])


def cost(ancestors, am, order_list):
    cost = 0
    for i in range(len(order_list) - 1):
        new_way = find_path(ancestors, order_list[i], order_list[i + 1], [])
        if new_way == "umulig":
            return new_way
        cost += sum([am[new_way[j]][new_way[j + 1]] for j in range(len(new_way) - 1)])
    return cost


def find_path(ancestors, i, j, way):
    if i == j:
        way.append(j)
        return way
    elif ancestors[i][j] is None:
        return "umulig"
    else:
        new_way = find_path(ancestors, i, ancestors[i][j], way) + [j]
        return new_way


#stdin = open("input_eksempel_01.txt", "r")
testcases = int(stdin.readline())
for test in range(testcases):
    cities = int(stdin.readline())
    order_list = [int(city) for city in stdin.readline().split()]
    adjacency_matrix = []
    for city in range(cities):
        adjacency_matrix.append([int(w) for w in stdin.readline().split()])
    print(shortest_path(order_list, adjacency_matrix, cities))
