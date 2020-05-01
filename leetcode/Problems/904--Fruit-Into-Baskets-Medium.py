class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 1:
            return len(tree)
        typeOne, typeTwo = None, None
        typeOneInd, typeTwoInd = None, None
        answer, current = 0, 0
        for i in range(len(tree)):
            # print/('cur', current, 'ans', answer, i, tree[i])
            if tree[i] == typeOne:
                # print(i, 'c1 cur', current, 'ans', answer, tree[i], 't1', typeOne, 't2', typeTwo, 't1I', typeOneInd, 't2I', typeTwoInd)
                current += 1
                answer = max(answer, current)
                
                if typeTwoInd != None and typeOneInd < typeTwoInd:
                    typeOneInd = i
            elif tree[i] == typeTwo:
                # print(i, 'c2 cur', current, 'ans', answer, tree[i], 't1', typeOne, 't2', typeTwo, 't1I', typeOneInd, 't2I', typeTwoInd)
                current += 1
                answer = max(answer, current)
                if typeOneInd > typeTwoInd:
                    typeTwoInd = i
            else:
                # print(i, 'c3 cur', current, 'ans', answer, tree[i], 't1', typeOne, 't2', typeTwo, 't1I', typeOneInd, 't2I', typeTwoInd)
                if typeOne == None:
                    typeOne = tree[i]
                    typeOneInd = i
                    answer = 1
                    current = 1
                    continue
                elif typeTwo == None:
                    typeTwo = tree[i]
                    typeTwoInd = i
                    answer = i+1
                    current = i+1
                    continue
                t1, t1Ind = 0, 0
                if typeTwoInd > typeOneInd:
                    t1 = typeTwo
                    t1Ind = typeTwoInd
                else:
                    t1 = typeOne
                    t1Ind = typeOneInd
                typeOne, typeOneInd = t1, t1Ind
                typeTwo = tree[i]
                typeTwoInd = i
                current = i-t1Ind+1
                # print(i, 'c4 cur', current, 'ans', answer, tree[i], 't1', typeOne, 't2', typeTwo, 't1I', typeOneInd, 't2I', typeTwoInd)
            # print(i, 'c5 cur', current, 'ans', answer, tree[i], 't1', typeOne, 't2', typeTwo, 't1I', typeOneInd, 't2I', typeTwoInd)
        return answer
            