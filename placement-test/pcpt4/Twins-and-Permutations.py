def getAns(P, Q):
    answer = 0
    Q_ind = {}
    for i in range(len(Q)):
        Q_ind[Q[i]] = i
    i = 0
    while i < len(P):
        start = Q_ind[P[i]]
        while start < len(Q) and i < len(P) and Q[start] == P[i]:
            start += 1
            i += 1
        answer += 1
    return answer-1
    
def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        P = list(map(int, input().strip().split()))
        Q = list(map(int, input().strip().split()))
        print(getAns(P, Q))
main()