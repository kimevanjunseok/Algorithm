def SelectionSort(X):
    for i in range(len(X)-1):
        min_n = i
        for j in range(i+1, len(X)):
            if X[min_n] > X[j]:
                min_n = j
        X[i], X[min_n] = X[min_n], X[i] 
    return X

L = [150, 45, 23, 2, 1, 7, 9, 100, 34, 67, 3, 7, 40, 20]
print(SelectionSort(L))