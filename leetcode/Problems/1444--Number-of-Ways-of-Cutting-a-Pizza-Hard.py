class Solution:
    def ways(self, pizza: List[str], cuts: int) -> int:
        if len(pizza) == 0:
            return 0
        m, n = len(pizza), len(pizza[0])
        pizza_count = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j != n-1:
                    pizza_count[i][j] = pizza_count[i][j+1]
                for k in range(i, m):
                    if pizza[k][j] == 'A':
                        pizza_count[i][j] += 1
        answer = [[[-1 for _ in range(cuts)] for _ in range(n)] for _ in range(m)]
        # print(pizza_count)
        modVal = 10**9+7
        # print(answer)
        def dp(sr, sc, cuts):
            # print(sr, sc, cuts)
            if answer[sr][sc][cuts] != -1:
                return answer[sr][sc][cuts]
            if cuts == 0:
                if pizza_count[sr][sc] == 0:
                    answer[sr][sc][cuts] = 0
                else:
                    answer[sr][sc][cuts] = 1
                return answer[sr][sc][cuts]
            answer[sr][sc][cuts] = 0
            
            for i in range(sr+1, m):
                if  pizza_count[i][sc] >= cuts and pizza_count[sr][sc] > pizza_count[i][sc]:
                    answer[sr][sc][cuts] = (answer[sr][sc][cuts]+dp(i, sc, cuts-1))%modVal
            
            for i in range(sc+1, n):
                if  pizza_count[sr][i] >= cuts and pizza_count[sr][sc] > pizza_count[sr][i]:
                    answer[sr][sc][cuts] = (answer[sr][sc][cuts]+dp(sr, i, cuts-1))%modVal
            
            return answer[sr][sc][cuts]
        return dp(0, 0, cuts-1)
            