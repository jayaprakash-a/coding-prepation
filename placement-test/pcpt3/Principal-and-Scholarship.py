import bisect
def getVal(marks, cutoff, minMarks):
    # print(marks, cutoff)
    low, high = 0, len(marks)-1
    count = 0
    while low <= high:
        mid = (low+high)//2
        if marks[mid][0] >= cutoff:
            count = len(marks)-mid
            high = mid - 1
        else:
            low = mid + 1
    low, high = 0, len(marks)-1
    answer = len(marks) + 10 
    while low <= high:
        mid = (low+high)//2
        if marks[mid][0] >= cutoff:            
            high = mid - 1
        else:
            answer = marks[mid][0]
            low = mid + 1
    if answer == len(marks) + 10 :
        answer = -1
    else:
        answer = minMarks[answer]
    return str(count) + ' ' + str(answer)
def main():
    [n, m] = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    marks = [(marks[i], i+1) for i in range(len(marks))]
    minMarks = {}
    for entry in marks:
        if entry[0] not in minMarks:
            minMarks[entry[0]] = entry[1]
    marks = sorted(marks, key=lambda x:(x[0], -x[1]))
    
    for _ in range(m):
        cutoff = int(input())        
        print(getVal(marks, cutoff, minMarks))
main()