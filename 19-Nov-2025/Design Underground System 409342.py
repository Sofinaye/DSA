# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins[id]
        
        travel_time = t - check_in_time
        route = (start_station, stationName)
        if route not in self.travel_times:
            self.travel_times[route] = [0, 0]  
        
        self.travel_times[route][0] += travel_time
        self.travel_times[route][1] += 1
        
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.travel_times[route]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)