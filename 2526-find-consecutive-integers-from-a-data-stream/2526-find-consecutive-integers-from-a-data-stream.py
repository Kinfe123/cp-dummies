class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k 
        self.counter = 0
        self.lastOne = -1

    def consec(self, num: int) -> bool:
        if num == self.lastOne:
            self.counter+=1
        else:
            self.counter = 1
            self.lastOne = num
        return (self.counter >= self.k) and (self.lastOne == self.value)
            
       
      

        
        
        
        
        
  
    
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)