def getAns(s, d):
    if s <= 1 and d <= 1:
        return 0
    if s == 0 or d == 0:
        return 0
    dp = [[0 for _ in range(d+1)] for _ in range(s+1)]

    for i in range(s+1):
        for j in range(d+1):
            if i>=2 and j>=1:
                dp[i][j] = max(dp[i][j], dp[i-2][j-1]+1)
            if i>=1 and j>=2:
                dp[i][j] = max(dp[i][j], dp[i-1][j-2]+1)
            if i>=3 and j>=3:
                dp[i][j] = max(dp[i][j], dp[i-3][j-3]+2)
    # print(dp)
    return dp[s][d]
def main():
    n = int(input())
    for _ in range(n):
        [s, d] = list(map(int, input().split()))
        print(getAns(s, d))
main()