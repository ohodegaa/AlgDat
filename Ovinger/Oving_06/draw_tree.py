__author__ = 'ohodegaa'

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin


class Node:
    x = None
    y = None
    left = None
    right = None
    key = None

    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y


def binary_graph(A):
    x = 0
    y = 0
    top_node = Node(A[1], 0, 0)
    level = 1
    nodes = [top_node]
    for i in range(1, len(A)):
        if A[i] == "-":
            node = Node(None, -1, -1)
            continue
        parent = nodes[i//2]
        if i%2 == 1:
            parent.left = Node(A[i], x, y)
        elif i%2 == 0:
            parent.right = Node(A[i], x, y)



def draw_tree(A, i, x, y):
    node = Node(A[i], x, y)



def main():
    A = stdin.readline().strip().split(" ")
    print(binary_graph(A), end='')


if __name__ == "__main__":
    main()