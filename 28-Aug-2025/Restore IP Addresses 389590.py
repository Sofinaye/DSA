# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        
        def backtrack(start, parts, current):
            if len(parts) == 4:
                if start == n:
                    res.append('.'.join(parts))
                return
            
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start+length]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                parts.append(segment)
                backtrack(start + length, parts, current)
                parts.pop()
        
        backtrack(0, [], [])
        return res