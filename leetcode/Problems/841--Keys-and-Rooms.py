class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRoom = set([0])
        startSet = [0]
        while(True):
            newSet = set()
            for entry in startSet:
                visitedRoom.add(entry)
                newSet = newSet.union(set(rooms[entry]))
            # print(list(newSet))
            startSet = newSet.difference(visitedRoom)
            
            if len(startSet) == 0:
                break
        
        if len(visitedRoom) == len(rooms):
            return True
        else:
            return False
            
                
                
            