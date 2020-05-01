class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
       
        costVal = []
        
        for i in range(len(s)):
            cost = abs(ord(s[i])-ord(t[i]))
            costVal.append(cost)
        # print(costVal, len(s))
        queue = collections.deque()
        answer, sumVal = 0, 0
        i = 0
        while(i < len(s)):
            
            while(i < len(s) and sumVal <= maxCost):
                
                queue.append(costVal[i])
                sumVal += costVal[i]
                # print(i, queue, answer, sumVal)
                i += 1      
            if i == len(s) and sumVal <= maxCost:
                answer = max(answer, len(queue))
            else:
                answer = max(answer, len(queue)-1)
            sumVal -= queue.popleft()
            
        return answer
            