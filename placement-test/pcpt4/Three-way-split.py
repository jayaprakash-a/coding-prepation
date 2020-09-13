    
def getAns(twoPow, n):

    # print('-----------')
    maxVal = twoPow[n-1]
    minVal = twoPow[n-3]
    # print(maxVal, minVal)
    sumVal = twoPow[n//3-1] - 1
    maxVal += sumVal
    minVal = minVal + sumVal*twoPow[n-n//3-2]
    # print(maxVal, minVal, sumVal, getPow(2, n-n//3-2))
    return (2*(maxVal-minVal))%(10**9+7)


def main():
    
    t = int(input().strip())
    nums = []
    for _ in range(t):
        n = int(input().strip())
        nums.append(n)
    twoPow = [1]
    prev = 1
    for i in range(max(nums)+1):
        prev = (prev*2)%(10**9+7)
        twoPow.append(prev)
    
    for n in nums:
        print(getAns(twoPow, n))
    
main()