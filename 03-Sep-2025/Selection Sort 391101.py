# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            if (i + 1) < n:
                m = min(arr[i + 1:])
                idx = arr.index(m, i + 1)
                if m < arr[i]:
                    arr[idx], arr[i] = arr[i], m
        return arr