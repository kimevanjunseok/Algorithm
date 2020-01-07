def combination(x, y):
    if x == 0:
        print(T)
    elif x > y:
        return
    else:
        T[x-1] = A[y-1]
        combination(x-1, y-1)
        combination(x, y-1)

A =[1, 2, 3, 4, 5]
T =[0] * 3

combination(3, len(A))