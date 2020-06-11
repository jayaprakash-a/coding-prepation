# n-1 pairs already fixed. first element of nth pair has 2n-1 possible places. Second element 2n places. Since the order is pickup->delivery. only (2n-1*n)
class Solution:
    def countOrders(self, n: int) -> int:
        answer = 1
        modVal = 10 ** 9 + 7
        
        for i in range(2, n+1):
            answer *= ((2*i-1)*(i)) % modVal
        
        return answer % modVal