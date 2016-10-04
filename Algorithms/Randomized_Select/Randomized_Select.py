__author__ = 'ohodegaa'

from Sorting_algorithms.Quicksort import quicksort

def rand_select(A, p, r, i):
    if p == i:
        return A[p]
    q = quicksort.randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]

    elif i < k:
        return rand_select(A, p, q - 1, i)
    else:
        return rand_select(A, q + 1, r, k - i)

A = [0,1,2,3,4,5,6]

print(rand_select(A, 0, len(A) - 1, 4))