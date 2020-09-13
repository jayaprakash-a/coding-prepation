def isValid(skills):
    for i in range(1, len(skills)):
        valid = False
        for j in range(3):
            if skills[i][j] >= skills[i-1][j]:
                if skills[i][j] > skills[i-1][j]:
                    valid = True
            else:
                return False
        if not valid:
            return False
    return True
def getAns(skills):
    skills = sorted(skills, key=lambda x: (x[0], x[1], x[2]))
    if isValid(skills):
        return 'Yes'
    skills = sorted(skills, key=lambda x: (x[0], x[2], x[1]))
    if isValid(skills):
        return 'Yes'
    skills = sorted(skills, key=lambda x: (x[1], x[0], x[2]))
    if isValid(skills):
        return 'Yes'
    skills = sorted(skills, key=lambda x: (x[1], x[2], x[0]))
    if isValid(skills):
        return 'Yes'
    skills = sorted(skills, key=lambda x: (x[2], x[1], x[0]))
    if isValid(skills):
        return 'Yes'
    skills = sorted(skills, key=lambda x: (x[2], x[0], x[1]))
    if isValid(skills):
        return 'Yes'
    return 'No'

def main():
    n = int(input())
    skills = []
    for _ in range(n):
        skills.append(list(map(int, input().split())))
    print(getAns(skills))
main()