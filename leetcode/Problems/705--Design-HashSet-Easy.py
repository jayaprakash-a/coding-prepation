class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [[] for _ in range(9929)]

    def add(self, key: int) -> None:
        modVal = key%9929
        if key not in self.data[modVal]:
            self.data[modVal].append(key)   

    def remove(self, key: int) -> None:
        modVal = key%9929
        if key in self.data[modVal]:
            self.data[modVal].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        modVal = key%9929
        return key in self.data[modVal]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)