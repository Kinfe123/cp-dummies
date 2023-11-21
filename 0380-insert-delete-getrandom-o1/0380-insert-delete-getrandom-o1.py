class RandomizedSet:

    def __init__(self):
        self.array = []
        self.map = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.array)
            self.array.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            removed_idx = self.map[val]
            lst_ele = self.array[-1]
            self.array[removed_idx] = lst_ele
            self.map[lst_ele] = removed_idx
            # self.map[val]
            self.array[-1] = val
            self.array.pop()
            self.map.pop(val)
            
            return True
            

    def getRandom(self) -> int:
        return random.choice(self.array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()