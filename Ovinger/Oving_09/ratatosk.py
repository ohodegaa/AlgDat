__author__ = 'ohodegaa'
#!/usr/bin/python3

from random import randint
from queue import deque
from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.dist = 0


def dfs(root: Node) -> int:
    q = deque([])
    if root.ratatosk:
        return 0
    root.next_child = 0
    node = root
    q.append(root)
    while len(q) > 0:
        if node.next_child < len(node.child):
            parent = node
            node = node.child[parent.next_child]
            parent.next_child += 1
            node.dist = parent.dist + 1
            if node.ratatosk:
                return node.dist
            q.append(parent)
        else:
            node = q.pop()


def bfs(root: Node) -> int:
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
    print(bfs(start_node))