__author__ = 'ohodegaa'

import random

def quicksort(A, p, r):
    if p < r:
         q = partition(A, p, r)
         print(A[p:q], " --- ", A[q+1:r+1])
         quicksort(A, p, q - 1)
         quicksort(A, q + 1, r)

counter = 0

def randomized_quicksort(A, p, r):
    if p < r:
         q = randomized_partition(A, p, r)
         print(A[p:q], " --- ", A[q+1:r+1])
         quicksort(A, p, q - 1)
         quicksort(A, q + 1, r)

def randomized_partition(A, p, r):
    pivot = random.randint(p, r)
    e = A[-1]
    A[-1] = A[pivot]
    A[pivot] = e
    return partition(A, p, r)

def partition(A, p, r):
    global counter
    pivot = A[r]            # setter siste element som pivot
    i = p - 1               # i = en index lavere enn første element i dellista

    for j in range(p, r):   # itererer på index fra start av delliste til slutt av delliste (-1)
        if A[j] <= pivot:   # dersom element er lavere enn pivot
            counter += 1    # counter for running time analysis
            i += 1              # inkrementer i
            e = A[i]            # bytt ut element
            A[i] = A[j]         # med
            A[j] = e            # element nr i
                            # bytt ut
    A[r] = A[i + 1]         # pivot-element
    A[i + 1] = pivot        # med element nr i + 1
    return i + 1            # returner index til pivot-element. Her vil
                            # pivot-elementet ha riktig plass i lista


def main():
    global counter
    print("Average case: ")
    A = [1,6,3,5,7,8,9,1,10,14,47,23,21,5,2,4,15,76,34,3,4,4,5,3,2,2,4,6,4,5,3,2,2,3,2,1,3,4,5,6]
    quicksort(A, 0, len(A) - 1)
    print("sorted list:", A)
    print(counter, "comparisons")

    counter = 0
    print("Worst case: ")
    quicksort(A, 0, len(A) - 1)
    print("Sorted list:",A)
    print(counter, "comparisons = ((n-1)*n)/2")

    print("A.length = ", len(A))
if __name__ == '__main__':
    main()