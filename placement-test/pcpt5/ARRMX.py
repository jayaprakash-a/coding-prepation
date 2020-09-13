def getAns(a1, a2):
    diffArr = []
    for i in range(len(a1)):
        diffArr.append((a1[i], a2[i]))
    diffArr = sorted(diffArr, key=lambda x: (-x[1], -x[0]))
    answer = sum((diffArr[i][0] - diffArr[i][1]*(i+1)) for i in range(len(diffArr)))
    return answer
    
def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a1 = list(map(int, input().strip().split()))
        a2 = list(map(int, input().strip().split()))
        print(getAns(a1, a2))
main()