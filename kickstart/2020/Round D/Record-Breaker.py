def getAns(nums):
    maxVal = -1
    answer = 0
    for i in range(len(nums)):
        if i == 0:
            if i+1 < len(nums) and nums[i] > nums[i+1]:
                answer += 1
            elif i == len(nums) - 1:
                answer += 1
        elif i == len(nums)-1:
            if nums[i] > maxVal:
                answer += 1
        else:
            if nums[i] > maxVal and i+1 < len(nums) and nums[i] > nums[i+1]:
                answer += 1
        maxVal = max(maxVal, nums[i])
    return answer
def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        nums = list(map(int, input().split()))
        print('Case #%d: %d'%(i, getAns(nums)))
main()