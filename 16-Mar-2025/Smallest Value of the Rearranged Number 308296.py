# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution(object):
    def smallestNumber(self, num):

            num_str = str(num)
            if num_str[0] == '-':
                digits = list(num_str[1:]) 
                is_negative = True
            else:
                digits = list(num_str)
                is_negative = False
            
            if is_negative:
                digits.sort(reverse=True)
            else:
                digits.sort()
            
            if not is_negative:
                zero_count = digits.count('0')
                if zero_count > 0:
                    for i, digit in enumerate(digits):
                        if digit != '0':
                            digits[0], digits[i] = digits[i], digits[0]
                            break
        
            result_str = ''.join(digits)
            
            if is_negative:
                return -int(result_str)
            else:
                return int(result_str)




            

        
    