def getAns(num):
    answer = [1 for _ in range(num+1)]
    answer[1] = 2
    answer[2] = 4
    for i in range(3, num+1):
        answer[i] = answer[i-1] + i
    return answer
    
def main():
    n = int(input().strip())
    nums = []
    for _ in range(n):
        num = int(input().strip())
        nums.append(num)
    answer = getAns(max(nums))
    for num in nums:
        print(answer[num])
main()