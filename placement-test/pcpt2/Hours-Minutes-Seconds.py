# Enter your code here. Read input from STDIN. Print output to STDOUT
def getAns(h,m,s,a,b,c):
    # [h,m,s,a,b,c] = time
    # print(h,m,s,a,b,c)
    hourDegree = (360/h)*(a + b/m + c/(m*s)) 
    minDegree = (360/m)*(b + c/s) 
    # print(hourDegree, minDegree)
    return min(abs(hourDegree-minDegree), 360-abs(hourDegree-minDegree)) 
def main():
    n = int(input())
    for _ in range(n):
        [h,m,s,a,b,c] = list(map(int, input().split()))
        print(getAns(h,m,s,a,b,c))
main()