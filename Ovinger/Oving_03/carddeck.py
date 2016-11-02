__author__ = 'ohodegaa'


from sys import stdin
from itertools import repeat



def merge2(decks):
    result = []
    if len(decks) < 2:
        return decks[0] if len(decks) == 1 else []


    l = merge2(decks[:(len(decks)//2)])
    r = merge2(decks[(len(decks)//2):])


    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0][0] < r[0][0]:
                result.append(l.pop(0))

            else:
                result.append(r.pop(0))


        elif len(l) > 0:
            result.extend(l)
            l = []


        else:
            result.extend(r)
            r = []


    return result


def merge(decks):
    result = merge2(decks)
    word = ""

    for tuple_ in result:
        word += tuple_[1]
    return word


def main():
    # Read input.
    decks = []

    input_ = open("input_eksempel_01.txt.txt", "r+")
    for line in input_:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()