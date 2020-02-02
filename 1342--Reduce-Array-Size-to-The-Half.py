class Solution:
    def comparator(self, x):
        return x[1], x[0]
    def minSetSize(self, arr: List[int]) -> int:
        originalLength = len(arr)
        newArr = []
        arr = sorted(arr)
        num = arr[0]
        count = 1
        for i in range(1,len(arr)):
            if arr[i] != num:
                newArr.append((num, count))
                count = 1
                num = arr[i]
            else:
                count +=1
        newArr.append((arr[-1], count))        
        sortedArr = sorted(newArr, key=self.comparator ,reverse=True)
        count, sumval = 0, 0
        # print('sorted', sortedArr)
        while(sumval < (originalLength+1)//2):
            
            sumval += sortedArr[count][1]
            count += 1
        
        return count
        
        