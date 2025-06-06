# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k

        def backtrack(index):
            nonlocal min_unfairness
            if index == len(cookies):
                current_max = max(distribution)
                if current_max < min_unfairness:
                    min_unfairness = current_max
                return
            for i in range(k):
                distribution[i] += cookies[index]
                if distribution[i] < min_unfairness: 
                    backtrack(index + 1)
                distribution[i] -= cookies[index]
                if distribution[i] == 0:  
                    break

        backtrack(0)
        return min_unfairness