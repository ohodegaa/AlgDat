__author__ = 'ohodegaa'


from sys import stdin

Inf = float(1e3000)

def mst(nm):
    current_node = 0
    weights = []
    tree = [current_node]
    while len(tree) < len(nm):
        min_w = Inf
        for r in range(len(nm)):
            if r in tree:
                continue
            for c in tree:
                if nm[r][c] < min_w and nm[r][c] != Inf:
                    min_w = nm[r][c]
                    current_node = r
        weights.append(min_w)
        tree.append(current_node)
    return max(weights)






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