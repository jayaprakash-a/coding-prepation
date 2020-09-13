class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = defaultdict(dict)
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                pref[i][preferences[i][j]] = -j
        pairing = {}
        answer = 0
        for [x, y] in pairs:
            pairing[x] = y
            pairing[y] = x
        # print(pref)
        for x in range(n):
            y = pairing[x]
            flag = False
            for [u, v] in pairs:
                if (u == x and v == y) or (v == x and u == y):
                    continue
                if pref[x][u] > pref[x][y] and pref[u][x] > pref[u][v]:
                    answer += 1
                    break
                elif pref[x][v] > pref[x][y] and pref[v][x] > pref[v][u]:
                    answer += 1
                    break
        return answer
            
            