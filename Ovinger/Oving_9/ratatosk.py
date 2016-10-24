__author__ = 'ohodegaa'

from queue import deque
#!/usr/bin/python3

from sys import stdin





class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.dist = 0

    def __repr__(self):
        return "Dist: " + str(self.dist) + ", " + str(self.ratatosk)


def dfs(root):
    q = deque([])
    if root.ratatosk:
        return 0
    root.next_child = 0
    q.append(root)

    while len(q) > 0:
        node = q.pop()
        if node.ratatosk:
            return node.dist
        if node.next_child < len(node.child):
            node.child[node.next_child].dist = node.dist + 1
            q.append(node.child[node.next_child])





def bfs(root: Node):
    q = deque([])
    if root.ratatosk:
        return 0
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        for child in node.child:
            child.dist = node.dist + 1
            if child.ratatosk:
                return child.dist
            q.append(child)






stdin = open("input_eksempel_01.txt", "r+")
function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))

elif function == 'velg':
    # SKRIV DIN KODE HER
    pass