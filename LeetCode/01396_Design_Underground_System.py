from collections import defaultdict

# Time Complexity O(n) 256 ms
# Space Complexity O(n) 25.3 MB
class UndergroundSystem:

    def __init__(self):
        self.on_going = {}
        self.history = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.on_going[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.on_going[id]
        self.history[(start_station, stationName)].append(t - start_time)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.history[(startStation, endStation)]) / len(self.history[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)