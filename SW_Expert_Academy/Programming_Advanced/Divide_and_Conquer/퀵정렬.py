import sys
sys.stdin = open("퀵정렬_input.txt")

def QuickSort(start, end):
    if start >= end:
        return
    p, t = end, start
    for i in range(start, end):
        if arr[i] < arr[p]:
            arr[i], arr[t] = arr[t], arr[i]
            t += 1
    arr[p], arr[t] = arr[t], arr[p]
    QuickSort(start, t-1)
    QuickSort(t+1, end)

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    QuickSort(0, len(arr)-1)
    print("#{0} {1}".format(n, arr[N//2]))

