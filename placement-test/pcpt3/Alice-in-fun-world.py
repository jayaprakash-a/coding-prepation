def addDigits(num):
    answer = 0
    for digit in str(num):
        answer = answer + int(digit)
    if answer and answer % 9:
        return answer % 9
    elif answer and answer % 9 == 0:
        return 9
    else:
        return 0
def getAns(num):
    dp = {1: 2, 2: 12}
    for i in range(3, num+1):
        # print('------')
        start = addDigits(i+1)
        rem = i
        # val = dp[i-1]
        if rem <= 9-start:            
            val = 2*(rem*start  + ((rem*(rem-1))//2 ))
            val -= addDigits(2*i)
        else:
            
            val = (45-((start*(start-1))//2))
            # print(i, rem, start, val)
            rem -= (9-start+1)
            val += (45)*(rem//9)
            # print(i, rem, start, val)
            rem = rem%9
            val += (rem*(rem+1))//2
            # print(i, rem, start, val)
            val = 2*val - addDigits(2*i)
        dp[i] = val + dp[i-1]
    return dp
            
def main():
    n = int(input())
    nums = []
    for _ in range(n):
        num = int(input())
        nums.append(num)
    dp = getAns(max(nums))
    for num in nums:
        print(dp[num])
main()