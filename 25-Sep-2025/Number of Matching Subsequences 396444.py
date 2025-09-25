# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        que = defaultdict(deque)
        for word in words:
            que[word[0]].append(word)

        count = 0
        for char in s:
            queue = que[char]
            for i in range(len(queue)):
                wrd = queue.popleft()
                if len(wrd) == 1:
                    count += 1
                else:
                    que[wrd[1]].append(wrd[1:])
        return count