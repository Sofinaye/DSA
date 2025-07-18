# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(''.join(current_combination))
                return
            current_digit = digits[index]
            for letter in digit_to_letters[current_digit]:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
        
        backtrack(0, [])
        return result