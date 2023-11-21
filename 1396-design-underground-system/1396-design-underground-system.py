class UndergroundSystem:

    def __init__(self):
        self.mapper = [[0 , 0]] * (10 ** 6 + 1)
        self.value = defaultdict(int)
        self.wrapper = defaultdict(int)
        

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.mapper[id] = (stationName , t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        curr_st , curr_time = self.mapper[id]
        p = (curr_st , stationName)
        if p not in self.value:
            self.value[p]= [0 , 0]
        self.value[p][1]+=(t - curr_time)
        self.value[p][0]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        num_of_p , time_taken = self.value[(startStation , endStation)]
        return time_taken / num_of_p
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)