class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        answer = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = []
        while True:
            newSet = set()
            while answer:
                num = answer.pop()
                if len(num) == N:
                    result.append(num)
                else:
                    last = int(num[-1])
                    if last+K <= 9:
                        newSet.add(num+str(last+K))
                    if 0 <= last-K <= 9:
                        newSet.add(num+str(last-K))
            if len(newSet) == 0:
                break
            answer = list(newSet)
        
            
        return list(map(int, result))
            