def getAns(target, coins):
    dp = [target+1]*(target+1)
    dp[0] = 0
    coins = sorted(coins)
    for i in range(1, target+1):
        for entry in coins:
            if i>=entry:
                dp[i] = min(dp[i], dp[i-entry]+1)
            else:
                break
    return dp[-1] if dp[-1] != (target+1) else -1
 
 
def main():
    [n, x] = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    print(getAns(x, coins))
main()

