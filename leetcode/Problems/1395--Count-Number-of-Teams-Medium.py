class Solution:
    def calValue(self, rating):
        left = [0]*len(rating)
        right = [0]*len(rating)
        
        
        for i in range(len(rating)):
            for j in range(i):
                if rating[j]>rating[i]:
                    left[i] += 1
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j]<rating[i]:
                    right[i] += 1
                    
        sumProd = 0
        
        for i in range(len(left)):
            sumProd += (left[i]*right[i])
            
        return sumProd
    
    def numTeams(self, rating: List[int]) -> int:
        
        sum1 = self.calValue(rating)
        sum2 = self.calValue(rating[::-1])
        
        return sum1+sum2
        
        
        