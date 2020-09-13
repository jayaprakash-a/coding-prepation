def getAns(req, gifts):
    valid = 0
    n, m = len(req), len(gifts)
    gifts = sorted(gifts)
    req = sorted(req)
    j = 0
    # print(req, gifts)
    for i in range(n):
        while j < m and req[i] > gifts[j]:
            j += 1
        if j == m:
            break
        else:
            # print(req[i], gifts[j], i, j)
            valid += 1
        j += 1
    return n-valid
    
def main():
    t = int(input().strip())
    for _ in range(t):
        [n, m] = list(map(int, input().strip().split()))
        requirements = list(map(int, input().strip().split()))
        gifts = list(map(int, input().strip().split()))
        print(getAns(requirements, gifts))
main()