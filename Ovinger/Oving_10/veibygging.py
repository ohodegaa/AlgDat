__author__ = 'ohodegaa'


from sys import stdin

Inf = float(1e3000)

def mst(nm):
    tree = []
    node = 0
    weight = - 1
    while len(tree) < len(nm):
        nm[node] = None
        tree.append(node)
        min_w = Inf
        for r in range(len(nm)):
            if nm[r] is None:
                continue
            for c in tree:
                if nm[r][c] < min_w and nm[r][c] != Inf:
                    min_w = nm[r][c]
                    node = r
        weight = max(weight, min_w)

    return weight






lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst(neighbour_matrix))