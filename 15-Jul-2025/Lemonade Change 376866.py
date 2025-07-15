# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                if fives == 0:
                    return False
                fives -= 1
            else:
                if fives == 0:
                    return False
                elif tens == 0:
                    if fives < 3:
                        return False
                    else:
                        fives -= 3
                else:
                    tens -= 1
                    fives -= 1
        return True