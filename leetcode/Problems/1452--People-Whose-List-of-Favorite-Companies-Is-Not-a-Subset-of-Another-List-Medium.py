class Solution:
    def setBit(self, x, ind):
        return x|(1<<ind)
    def unsetBit(self, x, ind):
        return x&(~(1<<ind))
    def getBit(self, x, ind):
        return x&(1<<ind)
    def getSetBitCount(self, n):
        count = 0
        while (n):
            n &= (n - 1)
            count += 1 
        return count
    def peopleIndexes(self, favComp: List[List[str]]) -> List[int]:
        companies = set()
        for entry in favComp:
            for comp in entry:
                companies.add(comp)
        index = 0
        companies = list(companies)
        compDict= {}
        for index in range(len(companies)):
            compDict[companies[index]] = index+1
        
        favList = []
        for entry in favComp:
            val = 0
            for comp in entry:
                val = self.setBit(val, compDict[comp])
            favList.append(val)
            # print(bin(val), end = ' ')
        # print()
        answer = []
        for i in range(len(favList)):
            flag = True
            for j in range(len(favList)):
                if j != i:
                    if favList[i] & favList[j] == favList[i]:
                        flag = False
            if flag:
                answer.append(i)
        return answer