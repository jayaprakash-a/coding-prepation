import collections
def getAns(nums):
    # print(nums)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    primeDict = collections.Counter()
    for num in nums:
        primeCount = collections.Counter()
        for prime in primes:
            if num == 1:
                break
            while num%prime == 0:
                primeCount[prime] += 1
                num //= prime
        # print(num, primeCount)
        primeDict |= primeCount
    # print(primeDict)
            
    answer = 1
    for num in primeDict:
        answer *= (num**(primeDict[num]))
    return answer
    
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(getAns(nums))
main()