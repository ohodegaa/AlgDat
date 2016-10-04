__author__ = 'ohodegaa'


from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict



def flexradix(A, k, index):
    B = [[] for i in range(k + 1)]
    C = []
    for l in range(len(A)):
        if index >= len(A[l]):
            C.append(A[l])
            continue
        iC = ord(A[l][index]) - 97
        B[iC].append(A[l])
    for i in range(len(B)):
        if len(B[i]) > 1:
            C.extend(flexradix(B[i], k, index + 1))
        else:
            C.extend(B[i])
    return C


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, 25, 0)
    for string in A:
        print(string)


if __name__ == '__main__':
    main()