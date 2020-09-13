def getAns(nums, k):
    # print('-----------')
    preSums = {0:-1}
    preSum = 0
    for i, num in enumerate(nums):
        # print(preSums)
        preSum = (preSum+num)%k
        if preSum in preSums and i-preSums[preSum] > 1:
            return "YES"
        if preSum not in preSums:
            preSums[preSum] = i        
    return 'NO'
def main():
    t = int(input().strip())
    for _ in range(t):
        [n, k] = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        print(getAns(nums, k))
main()