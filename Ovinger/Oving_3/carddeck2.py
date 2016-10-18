__author__ = 'ohodegaa'



from sys import stdin

from itertools import repeat


class BinHeap:

    i = 0
    def __init__(self):
        self.heapList = [(0,0)]
        self.currentSize = 0


    def percUp(self, i):
        i = 1

        while i // 2 > 0:
            if self.heapList[i][0] < self.heapList[i // 2][0]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2


    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][0] > self.heapList[mc][0]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    # finner index til minste child-node
    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2][0] < self.heapList[i*2 + 1][0]:
                return i*2
            else:
                return i*2 + 1

    def delMin(self):
        minElement = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return minElement

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)



    def buildHeap(self, myList):
        i = len(myList) // 2
        self.currentSize = len(myList)
        self.heapList += myList[:]
        while i > 0:
            self.percDown(i)
            i -= 1


    def hasNext(self):
        return self.currentSize > 0

def merge2(decks):
    result = []
    if len(decks) < 2:
        return decks[0] if len(decks) == 1 else []


    l = merge2(decks[:(len(decks)//2)])
    r = merge2(decks[(len(decks)//2):])
    i = 0
    j = 0
    print(l)
    print(r)
    while len(l) > i or len(r) > j:
        if len(l) > i and len(r) > j:
            if l[i][0] < r[j][0]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1

        elif len(l) > i:
            result.extend(l[i:len(l)])
            i = len(l)

        else:
            result.extend(r[j:len(r)])
            j = len(r)


    return result




def heap_merge(decks):
    heaper = BinHeap()
    myList = []
    for deck in decks:
        for card in deck:
            myList.append(card)
    heaper.buildHeap(myList)
    result_word = ""
    while heaper.hasNext():
        result_word += heaper.delMin()[1]
    return result_word


def merge(decks):
    result = merge2(decks)
    word = ""

    for tuple in result:
        word += tuple[1]
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