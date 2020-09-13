def getAns(skills):
    
    if len(skills) == 0:
        return 0
    answer = len(skills)
    skills = sorted(skills)
    # print(skills)
    prev = 0
    for i in range(1, len(skills)):
        if skills[i] == skills[i-1] + 1:
            continue
        else:
            length = i - prev
            # print(i, length)
            answer = min(answer, length)
            prev = i
    length = len(skills) - prev
    answer = min(answer, length)
    return answer
def main():
    n = int(input())
    for _ in range(n):
        skills = list(map(int, input().split()))
        print(getAns(skills[1:]))
main()