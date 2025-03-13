# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        writer = 0
        checker = 0
        
        while checker < len(chars):
            count = 0
            current_char = chars[checker]
            while checker < len(chars) and current_char == chars[checker]:
                count += 1
                checker += 1

            chars[writer] = current_char
            writer += 1
            
            if count > 1:
                for digit in str(count):
                    chars[writer] = digit
                    writer += 1
    
        return writer
        """
        :type chars: List[str]
        :rtype: int
        """
        