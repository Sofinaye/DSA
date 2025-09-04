# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1]= arr[j]
            j -= 1
            print(*arr)
         
        arr[j+1] = key
    print(*arr)