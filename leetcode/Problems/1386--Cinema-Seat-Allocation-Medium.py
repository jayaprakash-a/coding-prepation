class Solution:
    # def compare(self, x):
    #     return x[0], x[1]
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {}
        for row, seat in reservedSeats:
            if row not in seats.keys():
                seats[row] = [seat]
            else:
                seats[row] += [seat]
        
        count = (n - len(seats.keys())) * 2
        for i in seats.keys():
            
        # for i in range(1, n+1):
            if i not in seats.keys():
                count += 2
            else:
                flag = True
                if all(x not in seats[i] for x in [2, 3, 4, 5]):
                    # print(i, 2)
                    count += 1
                    flag = False
                
                
                if all(x not in seats[i] for x in [6,7, 8, 9]):
                    # print(i, 3)
                    count += 1
                    flag = False
                
                if flag and all(x not in seats[i] for x in [4,5,6,7]):
                    # print(i, 1)
                    count += 1
                    
        return count
                
            
                
        