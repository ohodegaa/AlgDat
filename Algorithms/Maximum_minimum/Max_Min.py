__author__ = 'ohodegaa'


def max_min(A):
    comparisons = 0
    if not len(A)%2:
        if A[0] > A[1]:
            _max = A[0]
            _min = A[1]
        else:
            _max = A[1]
            _min = A[0]
    else:
        _max = _min = A[0]

    for i in range(2 - len(A)%2, len(A), 2):
        comparisons += 1
        if A[i] > A[i + 1]:
            comparisons += 2
            if A[i] > _max:
                _max = A[i]
            if A[i + 1] < _min:
                _min = A[i + 1]
        else:
            comparisons += 2
            if A[i + 1] > _max:
                _max = A[i]
            if A[i] < _min:
                _min = A[i + 1]

    print("Number of comparisons: ", comparisons)
    return _max, _min


A = [1,3,6,5,3,5,6,4,3,5,3,5,2,1,12,23,42,12,45,4,2,56,67,2,0]
print("len(list) = ", len(A))
print(max_min(A))