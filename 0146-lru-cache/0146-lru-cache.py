class Node:
    def __init__(self , keys , values):
        self.keys = keys 
        self.values = values
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.map_ = {}
        self.left , self.right = Node(-1 , -1) , Node(-1 , -1)
        self.left.next = self.right
        self.right.prev = self.left
        
        
        
    def remove(self,node):
        previous , next_ = node.prev , node.next
        previous.next = next_
        next_.prev = previous
        
    def insert(self , node):
        previous , next_ = self.right.prev , self.right
        previous.next = node
        node.next = next_
        next_.prev = node
        node.prev = previous
    def get(self, key: int) -> int:
        if key in self.map_:
            self.remove(self.map_[key])
            #removing and inserting to the right - the most recently used side 
            self.insert(self.map_[key])
            return self.map_[key].values
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map_:
            self.remove(self.map_[key])
            #For making it Most RU since we have done operation - 
        self.map_[key] = Node(key , value)
        self.insert(self.map_[key])
        if len(self.map_) > self.capacity:
            LRU = self.left.next # the left is least recently used one
            self.remove(LRU)
            del self.map_[LRU.keys]
            #since map element can be deleted using key 
            
            
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)