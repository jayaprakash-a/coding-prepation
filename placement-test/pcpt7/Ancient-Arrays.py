def getAns(num, maxNum):
    # print('----------')
    maxLen = len(str(maxNum))
    dp = [0 for _ in range(len(num))]
    
    for i in range(len(num)):
        if i+1 <= maxLen and 1 <= int(num[:(i+1)]) <= maxNum:
            dp[i] = 1
        for j in range(i, -1, -1):
            if num[j] == '0':
                continue
            if 1 <= int(num[j:i+1]) <= maxNum:
                if j == 0:
                    continue
                dp[i] += dp[j-1]
            if i-j+1 > maxLen:
                break
        dp[i] %= (10**9+7)
            
    return dp[len(num)-1]%(10**9+7)

def main():
    n = int(input())
    for _ in range(n):
        num = input()
        maxNum = int(input())
        print(getAns(num, maxNum))
main()      