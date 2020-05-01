class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        count = list(collections.Counter(deck).items())
        # print(count)
        minVal = len(deck)
        for i in range(len(count)):
            minVal = min(minVal, count[i][1])
        
        if minVal < 2:
            return False
        
        flag = True
        for i in range(2, minVal+1):
            flag = True
            for j in range(len(count)):
                if count[j][1]%i != 0:
                    flag = False
                    break
            if flag:
                return True
        return False
        
        