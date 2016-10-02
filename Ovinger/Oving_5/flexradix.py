__author__ = 'ohodegaa'


from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d, i):



    return A

def sort_by_index(A, i):
    sorted_list = []
    partitions = {}
    for word in A:
        if i >= len(word):
            sorted_list.append(word)
        elif partitions.get(word[i]) is None:
            partitions[word[i]] = [word]
        else:
            partitions[word[i]].append(word)

    return [words for words in partitions.values()]

def main():
    stdin = open("input_eksempel_01.txt", "r+")
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()