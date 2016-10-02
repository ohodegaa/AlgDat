__author__ = 'ohodegaa'


from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict


def flexradix(A, d, i):
    sorted_list = [""]*len(A)
    while i <= d:
        for word in A:


    return A



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