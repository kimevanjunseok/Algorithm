def BubbleSort(X):
    for i in reversed(range(1, len(X))):
        for j in range(i):
            if X[j] > X[j+1]: 
                X[j], X[j+1] = X[j+1], X[j]
    return X
    
L = [150, 45, 23, 2, 1, 7, 9, 100, 34, 67, 3, 7, 40, 20]
print(BubbleSort(L))