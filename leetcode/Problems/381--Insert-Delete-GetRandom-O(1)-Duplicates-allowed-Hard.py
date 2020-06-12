import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = defaultdict(list)
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # print('insert start', self.arr, self.pos)
        self.arr.append(val)
        retVal = False
        if len(self.pos[val]) == 0:
            retVal = True        
        self.pos[val] += [self.length]
        self.length += 1
        # print('insert end', self.arr, self.pos)
        return retVal
    
    def remove(self, val: int) -> bool:
        
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # print('remove start', self.arr, self.pos)
        if len(self.pos[val]) == 0:
            return False
        index = self.pos[val].pop()
        lastVal = self.arr[-1]
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        if self.arr[index] != self.arr[-1]:
            self.pos[lastVal].pop()
            insert_index = bisect.bisect_left(self.pos[lastVal], index)
            self.pos[lastVal].insert(insert_index, index)
        self.arr.pop()
        self.length -= 1
        # print('remove end', self.arr, self.pos)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()