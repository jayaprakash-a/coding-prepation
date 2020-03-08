class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        answer = []
        
        temp, depth = label, 0
        
        while(temp != 0):
            answer.append(temp)
            temp = temp//2       

        answer = answer[::-1]
        
        if len(answer)%2 == 1:
            twoMin, twoMax, start = 2, 3, 1
        else:
            twoMin, twoMax, start = 1, 1, 0
        
        for i in range(start, len(answer), 2):
            answer[i] = twoMin + twoMax - answer[i]
            twoMin *= 4
            twoMax = 2*twoMin - 1
        
        return answer