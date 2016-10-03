__author__ = 'ohodegaa'


def countingsort(A, B, k):
    C = [0]*(k+1)
    for i in range(0, len(A)):  # A innholder C[A[i]] av verdi A[i]
        C[A[i]] += 1
    for j in range(1, k + 1):
        C[j] += C[j - 1]
    for k in range(len(A) - 1, -1, -1):
        B[C[A[k]] - 1] = A[k]
        C[A[k]] -= 1
    return B

def main():
    A = [1, 6, 3, 6, 3, 9, 4, 5, 8, 3, 8, 2, 7, 6, 2, 5, 3, 3, 0, 0, 3, 1, 2, 6, 5, 2, 5, 3, 6, 5, 4, 3, 3, 4, 2, 4]
    B = [None]*len(A)
    result = countingsort(A, B, max(A))
    print(result)

if __name__ == '__main__':
    main()