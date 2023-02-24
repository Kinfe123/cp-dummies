class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [-1] * k
        self.k = k
        self.size = 0
        self.front = 0
        self.back = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.front] = value
        self.front +=1
        self.front %= self.k
        self.size+=1
        return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.back] = -1
        self.back+=1
        self.back %= self.k
        self.size -= 1
        
        return True
        

    def Front(self) -> int:
        return self.data[self.back]
        

    def Rear(self) -> int:
        #since we shift one for making the another enqueing then , we have
        #to trace back to the one behind to return the value 
        return self.data[self.front-1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.k == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()