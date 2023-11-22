class RandomizedSet:

    def __init__(self):
        self.array = []
        self.mapper = defaultdict(int)
        

    def insert(self, val: int) -> bool:
        if val in self.mapper:
            return False
        else:
            self.mapper[val] = len(self.array)
            #adjusting the indexing issue
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.mapper:
            return False
        else:
            last_ele = self.array[-1]
            rem_idx = self.mapper[val]
            last_idx = self.mapper[self.array[-1]]
            self.mapper[self.array[-1]] = rem_idx
            self.mapper[val] = last_idx
            self.array[rem_idx] = last_ele
            self.array[last_idx] = val
            self.array.pop()
            self.mapper.pop(val)
            
            
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()