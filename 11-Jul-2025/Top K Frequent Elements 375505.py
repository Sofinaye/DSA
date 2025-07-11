# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        arr = []
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            obj[num] = obj.get(num,0) +1
        for key, value in obj.items():
            freq[value].append(key)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                arr.append(n)
                if len(arr) == k:
                    return arr