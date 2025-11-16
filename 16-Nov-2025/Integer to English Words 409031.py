# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Word mappings
        under_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
            "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def convert_chunk(n):
            # Convert a number less than 1000 to words
            if n == 0:
                return ""
            elif n < 20:
                return under_twenty[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + convert_chunk(n % 10)
            else:
                return under_twenty[n // 100] + " Hundred " + convert_chunk(n % 100)
        
        result = ""
        chunk_index = 0
        
        while num > 0:
            if num % 1000 != 0:
                result = convert_chunk(num % 1000).strip() + " " + thousands[chunk_index] + " " + result
            num //= 1000
            chunk_index += 1
        
        return result.strip()
