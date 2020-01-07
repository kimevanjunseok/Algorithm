def permutation(x, y):
    if x == y:
        print(A)
    else:
        for i in range(x, y):
            A[i], A[x] = A[x], A[i]
            permutation(x+1, y)
            A[i], A[x] = A[x], A[i]

A = [1, 2, 3, 4, 5]
permutation(0, len(A))