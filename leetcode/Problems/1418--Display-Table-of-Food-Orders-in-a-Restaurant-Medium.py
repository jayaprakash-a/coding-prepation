class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = {}
        foods = []
        ta = []
        for [_, t, f] in orders:
            if int(t) not in ta:
                ta.append(int(t))
            if f not in foods:
                foods.append(f)
            if t not in table.keys():
                table[t] = {}
            if f not in table[t].keys():
                table[t][f] = 1
            else:
                table[t][f] += 1
        foods = sorted(foods)
        ta = sorted(ta)
        answer = [['Table']+foods]
        for t in ta:
            newArr = [str(t)]
            for f in foods:
                if f in table[str(t)].keys():
                    newArr.append(str(table[str(t)][f]))
                else:
                    newArr.append('0')
            answer.append(newArr)
        return answer