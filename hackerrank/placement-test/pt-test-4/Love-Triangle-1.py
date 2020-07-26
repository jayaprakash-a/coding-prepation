def getAns(likes):
    for i in range(len(likes)):
        if likes[likes[likes[i] - 1]-1] == i +1:
            return 'YES'
    return 'NO'
def main():
    n = int(input())
    likes = list(map(int, input().split()))
    print(getAns(likes))
main()