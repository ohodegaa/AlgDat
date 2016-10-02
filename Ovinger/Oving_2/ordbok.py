__author__ = 'ohodegaa'

from sys import stdin, stderr
import traceback
import sys

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []



def bygg(word_list):
    top_node = Node()
    for word in word_list:
        node = top_node
        for i in range(len(word[0])):
            if node.barn.get(word[0][i]) is None:
                node.barn[word[0][i]] = Node()
            node = node.barn[word[0][i]]
        node.posi.append(word[1])
    return top_node





def posisjoner(word, index, node):

    if index == len(word):
        return node.posi


    if word[index] in node.barn.keys():
        return posisjoner(word, index + 1, node.barn.get(word[index]))

    elif word[index] == "?":
        pos = []
        for child in node.barn.keys():
            pos.extend(posisjoner(word, index + 1, node.barn.get(child)))
        return pos
    else:
        return []


def main():
    global top_node
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1

        toppnode = bygg(ordliste)
        print("HALLA")
        for sokeord in stdin:
            sokeord = sokeord.strip()
            if len(sokeord) < 1:
                continue
            print("%s:" % sokeord, end = "")
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end = "")
            print()
    except:
        traceback.print_exc(file=stderr)




if __name__ == '__main__':
    main()