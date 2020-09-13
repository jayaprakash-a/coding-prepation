import sys
def getAns(costs, balls):
    
    [a, b, c] = costs
    if a == 0 or b == 0:
        return 0
    total = sum(balls)
    low, high = min(balls), max(balls)
    result = sys.maxsize
    for i in range(total//len(balls)-1, total//len(balls)+2):
        answer = 0
        excess = total - (i*len(balls))
        if excess >= 0:
            val = min(c, a+b)
            answer = excess*a
            for num in balls:
                if num < i:
                    answer += val*(i-num)
            result = min(result, answer)
        else:
            val = min(c, a+b)
            answer = -excess*b
            for num in balls:
                if num > i:
                    answer += val*(num-i)
            if answer > result:
                break
            result = min(result, answer)

    return result
            
            
        
def main():
    n = int(input())
    
    costs = list(map(int, input().split()))
    balls = list(map(int, input().split()))
    print(getAns(costs, balls))
main()