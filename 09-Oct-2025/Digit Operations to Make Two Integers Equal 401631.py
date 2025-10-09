# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def is_prime(self, x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        limit = int(math.sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                return False
        return True

    def minOperations(self, n: int, m: int) -> int:
        if self.is_prime(n) or self.is_prime(m):
            return -1
        
        digits_n = len(str(n))
        low = 10**(digits_n - 1)
        high = 10**digits_n - 1
        
        dist = {}
        dist[n] = n
        pq = [(n, n)]  
        
        while pq:
            cost, num = heappop(pq)
            if cost > dist[num]:
                continue
            if num == m:
                return cost
            
            s = list(str(num))
            for i in range(len(s)):
                orig_digit = int(s[i])
                if orig_digit != 9:
                    s[i] = str(orig_digit + 1)
                    neighbor = int(''.join(s))
                    if low <= neighbor <= high and not self.is_prime(neighbor):
                        new_cost = cost + neighbor
                        if neighbor not in dist or new_cost < dist[neighbor]:
                            dist[neighbor] = new_cost
                            heappush(pq, (new_cost, neighbor))
                    s[i] = str(orig_digit)
                    
                if orig_digit != 0:
                    s[i] = str(orig_digit - 1)
                    neighbor = int(''.join(s))
                    if low <= neighbor <= high and not self.is_prime(neighbor):
                        new_cost = cost + neighbor
                        if neighbor not in dist or new_cost < dist[neighbor]:
                            dist[neighbor] = new_cost
                            heappush(pq, (new_cost, neighbor))
                    s[i] = str(orig_digit)
        
        return -1
            