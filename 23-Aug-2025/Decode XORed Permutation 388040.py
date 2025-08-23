# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total_xor = 0
        for i in range(1, n+1):
            total_xor ^= i
        
        xor_encoded_alternate = 0
        for i in range(1, len(encoded), 2):
            xor_encoded_alternate ^= encoded[i]
        
        first_element = total_xor ^ xor_encoded_alternate
        perm = [first_element]
        for i in range(len(encoded)):
            next_element = perm[-1] ^ encoded[i]
            perm.append(next_element)
        return perm