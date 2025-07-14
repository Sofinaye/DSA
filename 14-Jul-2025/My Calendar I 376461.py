# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append((startTime, endTime))
            return True
        
        pos = bisect.bisect_right(self.events, (startTime, endTime))
        
        if pos > 0 and self.events[pos-1][1] > startTime:
            return False
        
        if pos < len(self.events) and self.events[pos][0] < endTime:
            return False
        
        bisect.insort(self.events, (startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)