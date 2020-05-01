class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.cap = capacity
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.cap > 0:
                self.cache[key] = value
                self.cap -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = [None]*capacity
#         self.lastEntry = 0
#         self.cap = capacity
    
#     def get(self, key: int) -> int:
#         index = -1
#         for i in range(self.lastEntry):
#             if self.cache[i][0] == key:
#                 index = i
#                 break
#         if index == -1:
#             # print('Get', key, self.cache)
#             return -1
#         entry = self.cache.pop(index)
#         self.cache.insert(0, entry)
#         # print('Get', key, self.cache)
#         return entry[1]
        

#     def put(self, key: int, value: int) -> None:
#         index = -1
#         for i in range(self.lastEntry):
#             if self.cache[i][0] == key:
#                 index = i
#                 break
#         if index == -1:
#             if self.lastEntry <= self.cap-1:
#                 self.cache.insert(0, [key, value] )
#                 self.cache.pop()
#                 if self.lastEntry < self.cap:
#                     self.lastEntry += 1
#             else:
#                 self.cache.insert(0, [key, value] )
#                 self.cache.pop()
#                 # self.cache.append([key, value])
#             # print('Put', key, value, self.cache, self.lastEntry)
#         else:
#             entry = self.cache.pop(index)
#             entry[1] = value
#             self.cache.insert(0, entry)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)