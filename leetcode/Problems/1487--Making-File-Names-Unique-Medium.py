class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        namesSet = set()
        namesDict = {}
        
        for i in range(len(names)):
            # print(i)
            name = names[i]
            if name not in namesSet:
                namesSet.add(name)
                namesDict[name] = 1
                continue
            else:
                num = namesDict[name]
                while name + '(' + str(num) + ')' in namesSet:
                    num += 1
                namesDict[name] = num
                namesDict[name + '(' + str(num) + ')'] = 1
                names[i] = name + '(' + str(num) + ')'
                namesSet.add(name + '(' + str(num) + ')')
        return names
            