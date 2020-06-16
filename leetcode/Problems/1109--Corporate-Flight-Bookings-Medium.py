# https://leetcode.com/problems/corporate-flight-bookings/discuss/328856/JavaC%2B%2BPython-Straight-Forward-Solution
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0]*(n+1)
        for [s, d, k]  in bookings:
            answer[s-1] += k
            answer[d] -= k
        for i in range(1, n):
            answer[i] += answer[i-1]
        
        return answer[:-1]