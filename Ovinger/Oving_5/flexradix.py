__author__ = 'ohodegaa'


from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d, i):



    return A

def sort_by_index(A, start, end, i):
    sorted_list = []
    partitions = {}
    for word in A[start:end+1]:
        if i >= len(word):
            sorted_list.append(word)
        elif partitions.get(word[i]) is None:
            partitions[word[i]] = [word]
        else:
            partitions[word[i]].append(word)
    for i in range(ord('a'), ord('z') + 1):
        try:
            sorted_list.extend(partitions[chr(i)])
        except:
            pass

    A[start:end+1] = sorted_list

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