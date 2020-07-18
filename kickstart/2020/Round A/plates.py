def getAns(n, k, p, stacks):
    for i in range(len(stacks)):
        for j in range(k-1):
            stacks[i][j+1] += stacks[i][j]
    dp = [[0 for _ in range(p+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(p, (i+1)*k)+1):
            dp[i][j] = dp[i-1][j]               
            for ind in range(min(j, k)):
                dp[i][j] = max(dp[i][j], dp[i-1][j-ind-1] + stacks[i-1][ind])
    return dp[n][p]
def main():
    t = int(input())
    for i in range(1, t+1):
        [n, k, p] = list(map(int, input().split()))
        stacks = []
        for _ in range(n):
            stacks.append(list(map(int, input().split())))
        print('Case #%d: %d'%(i, getAns(n, k, p, stacks)))
main()