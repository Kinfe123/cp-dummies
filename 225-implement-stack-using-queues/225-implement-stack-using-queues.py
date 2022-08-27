from _collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        
        
        

    def push(self, x):
        self.q1.append(x)
        for i in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        
        

    def pop(self):
        return self.q1.popleft()
    
    
        

    def top(self):
        return self.q1[0]
        

    def empty(self):
        
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()