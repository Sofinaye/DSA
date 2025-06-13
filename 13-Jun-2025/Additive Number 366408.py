# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        def backtrack(index, sequence):
            if index == n and len(sequence) >= 3:
                return True
            for i in range(index + 1, n + 1):
                current_str = num[index:i]
                if len(current_str) > 1 and current_str[0] == '0':
                    continue
                current_num = int(current_str)
                if len(sequence) < 2:
                    if backtrack(i, sequence + [current_num]):
                        return True
                else:
                    if current_num == sequence[-1] + sequence[-2]:
                        if backtrack(i, sequence + [current_num]):
                            return True
            return False
        
        return backtrack(0, [])
        