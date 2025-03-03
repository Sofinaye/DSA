# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet(object):

    def __init__(self):
        self.data = {} 
        self.values = []

    def insert(self, val):
        if val in self.data:
            return False

        self.data[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.data:
            return False

        index = self.data[val]
        last_value = self.values[-1]
        self.values[index] = last_value
        self.data[last_value] = index
        self.values.pop()
        del self.data[val]
        return True

    def getRandom(self):
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()