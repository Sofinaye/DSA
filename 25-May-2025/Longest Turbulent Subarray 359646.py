# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        max_len = 1
        current_len = 1
        prev_diff = 0
        
        for i in range(n - 1):
            current_diff = arr[i+1] - arr[i]
            if (prev_diff < 0 and current_diff > 0) or (prev_diff > 0 and current_diff < 0):
                current_len += 1
            else:
                current_len = 1 if current_diff == 0 else 2
            max_len = max(max_len, current_len)
            prev_diff = current_diff
        
        return max_len