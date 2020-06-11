class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        # print(gas, cost)
        for i in range(len(gas)-n):
            init = 0
            flag = True
            for j in range(i, i+n+1):
                init += gas[j]
                init -= cost[j]
                if init < 0 and j != i+n:
                    flag = False
                    break
            if flag:
                return i
        return -1