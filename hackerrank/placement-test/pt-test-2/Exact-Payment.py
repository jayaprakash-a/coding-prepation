def getAns(a, b, n, S):
    val = S//n
    # print(a, b, n, S, S//n, S%n)
    if a*n+b<S:
        return 'NO'
    if a >= val and b>=(S%n):
        return 'YES'
    elif b >= (S-min(a, val)*n):
        return 'YES'
    return 'NO'
def main():
    q = int(input())
    for _ in range(q):
        [a,b,n,S] = list(map(int, input().split()))
        print(getAns(a,b,n,S))
main()