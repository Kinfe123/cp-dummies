class MyCircularQueue:

    def __init__(self, k: int):
        #three lists two stacks and one arr
        self.list = [-1]*k
        self.length = 0
        self.ptr = 0
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.list[self.length] = value
        # print(self.list, self.length)
        self.length = (self.length + 1) % len(self.list)
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.list[self.ptr] = -1
        self.ptr = (self.ptr + 1) % len(self.list)
        # print(self.list)
        self.size -= 1
        return True
        

    def Front(self) -> int:
        return self.list[self.ptr] 
    
    def Rear(self) -> int:
        # print(self.length)
        return self.list[self.length - 1]

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == len(self.list)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()