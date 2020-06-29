class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = {'N': (-1, 0), 'S':(1, 0), 'E':(0, 1), 'W':(0, -1)}
        visited = {(0, 0)}
        start = [0, 0]
        for ch in path:
            start[0] += paths[ch][0]
            start[1] += paths[ch][1]
            node = tuple(start)
            # print(visited, ch, start)
            if node in visited:
                return True
            visited.add(node)
        return False