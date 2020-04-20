class Solution:
    def minNumberOfFrogs(self, frog: str) -> int:
        c,r,o,a,k = 0,0,0,0,0
        maxVal = 0
        for ch in frog:
            if ch == 'c':
                c+=1
            elif ch == 'r':
                r+=1
            elif ch == 'o':
                o+=1
            elif ch == 'a':
                a+=1
            elif ch == 'k':
                k+=1
            else:
                return -1
            maxVal = max(maxVal, c)
            if c>=r>=o>=a>=k:
                if k == 1:
                    c-=1
                    r-=1
                    o-=1
                    a-=1
                    k=0
            else:
                return -1
            
        
                
        # print(c,r,o,a,k)
        if c==r==o==a==k:
            return maxVal
        else:
            return -1