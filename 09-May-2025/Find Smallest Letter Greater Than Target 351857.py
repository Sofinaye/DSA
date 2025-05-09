# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        

        while l < r:
            mid = (l + r) // 2
            temp = letters[mid]
            if temp > target:                
                r = mid
            else:
                l = mid + 1

        return letters[r] if letters[r] > target else letters[0] 

        
        