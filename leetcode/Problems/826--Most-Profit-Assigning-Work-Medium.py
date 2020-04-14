class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difProfit = sorted([[difficulty[i], profit[i]] for i in range(len(profit))])
        for i in range(1, len(profit)):
            difProfit[i][1] = max(difProfit[i][1], difProfit[i-1][1])
        # print(difProfit)
        worker = sorted(worker)
        answer, index, i = 0, 0, 0
        
        while(index < len(worker) and i < len(profit)):
            # print(difProfit[i][0], worker[index])
            if difProfit[i][0] <= worker[index]:
                if i+1 <len(profit) and worker[index] < difProfit[i+1][0]:
                    # print(worker[index], difProfit[i][0], difProfit[i][1])
                    answer += difProfit[i][1]
                    index += 1
                elif i == len(profit)-1:
                    # print(worker[index], difProfit[i][0], difProfit[i][1])
                    answer += difProfit[i][1]
                    index += 1
                else:
                    i += 1
            else:
                index += 1
        return answer