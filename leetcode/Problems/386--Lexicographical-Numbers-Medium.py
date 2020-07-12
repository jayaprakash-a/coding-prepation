class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=str)
        answer = []
        def dfs(num, n):
            if num <= n:
                answer.append(num)
                for i in range(10):
                    if 10*num+i > n:
                        return
                    dfs(10*num+i, n)
        for i in range(1, 10):
            dfs(i, n)
        return answer