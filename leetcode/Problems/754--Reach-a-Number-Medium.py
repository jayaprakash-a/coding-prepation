class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = math.floor(-1+math.sqrt(1+8*target))//2
        
        sumVal = (i*(i+1))//2
        i += 1
        while(sumVal < target):
            sumVal += i
            i += 1
        while((sumVal-target)%2==1):
            sumVal += i
            i += 1
        return i-1
        