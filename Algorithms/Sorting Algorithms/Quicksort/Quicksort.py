__author__ = 'ohodegaa'

def quicksort(A, p, r):
    if p < r:
         q = partition(A, p, r)
         quicksort(A, p, q - 1)
         quicksort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]            # setter siste element som pivot
    i = p - 1               # i = en index lavere enn første element i dellista

    for j in range(p, r):   # itererer på index fra start av delliste til slutt av delliste (-1)
        if A[j] <= pivot:   # dersom element er lavere enn pivot
            i += 1              # inkrementer i
            e = A[i]            # bytt ut element
            A[i] = A[j]         # med
            A[j] = e            # element nr i
    e = A[i + 1]            # bytt ut
    A[r] = A[i + 1]         # pivot-element
    A[r] = e                # med element nr i + 1
    return i + 1            # returner index til pivot-element. Her vil
                            # pivot-elementet ha riktig plass i lista


def main():

    A = [1,6,3,5,2,7,8,9,2,4,1,5,10,14,47,23,21,5,2,4,15,76,34]
    quicksort(A, 0, len(A) - 1)
    print(A)

if __name__ == '__main__':
    main()