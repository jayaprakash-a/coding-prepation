class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        secCount = Counter()
        #secs = list(range(1, n+1)) + list(range(1, n+1))
        start = rounds[0]
        maxCount = 1
        for entry in rounds[1:]:
            if start < entry:
                while start <= entry:
                    secCount[start] += 1
                    maxCount = max(maxCount, secCount[start])
                    start += 1
            else:
                while start <= n:
                    secCount[start] += 1
                    maxCount = max(maxCount, secCount[start])
                    start += 1
                start = 1
                while start <= entry:
                    secCount[start] += 1
                    maxCount = max(maxCount, secCount[start])
                    start += 1
        # print(secCount)
        answer = []
        for key in secCount:
            if secCount[key] == maxCount:
                answer.append(key)
        
        return sorted(answer)