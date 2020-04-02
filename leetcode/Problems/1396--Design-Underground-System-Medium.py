class UndergroundSystem:

    def __init__(self):
        self.personHistory = {}
        self.stationHistory = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.personHistory[id] = [stationName, t, 0]
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStationName = self.personHistory[id][0]
        prevTime = self.personHistory[id][1]
        self.personHistory[id] = [prevStationName, prevTime, t]
        
        if (prevStationName, stationName) not in self.stationHistory.keys():
            
            self.stationHistory[(prevStationName, stationName)] = [t-prevTime]
        else:
            self.stationHistory[(prevStationName, stationName)] += [t-prevTime]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        reqList = list(self.stationHistory[(startStation, endStation)])
        sumVal = sum(reqList)
        return sumVal/len(reqList)
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)