class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        
        midIndex = (left + right)//2
        count = 0
        while(True):
            # print(left, right, midIndex)
            if (A[midIndex] > A[midIndex-1] and A[midIndex] > A[midIndex+1]):
                break
            # count += 1
            # if count == 5:
                # break
            
            if A[midIndex] > A[midIndex-1] and A[midIndex] < A[midIndex+1]:
                left = midIndex+1
            else:
                right = midIndex-1
                
            midIndex = (left + right)//2
        
        return midIndex
        