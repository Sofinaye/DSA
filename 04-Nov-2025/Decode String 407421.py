# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        curr_string = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                count_stack.append(curr_num)
                string_stack.append(curr_string)
                curr_string = ""
                curr_num = 0
            elif char == ']':
                count = count_stack.pop()
                prev_string = string_stack.pop()
                curr_string = prev_string + curr_string * count
            else:  
                curr_string += char
        
        return curr_string