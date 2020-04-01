class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        # 4*x + 2*(c-x) = t
        
        x = (t-2*c)/(2)
        
        if int(x) == x and  x >= 0 and x<=c:
            return [int(x), int(c-x)]
        return []
        