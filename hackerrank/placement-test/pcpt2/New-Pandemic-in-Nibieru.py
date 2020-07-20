import math
def dist(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
def getAns(points, d):
    points = sorted(points, key=lambda x:x[0])
    for i in range(len(points)-1):
        if dist(points[i], points[i+1]) < d:
            print('NO')
            print(points[i][2], points[i+1][2])
            return 
    
    points = sorted(points, key=lambda x:x[1])
    for i in range(len(points)-1):
        if dist(points[i], points[i+1]) < d:
            print('NO')
            print(points[i][2], points[i+1][2])
            return 
    
    print('YES')
def main():
    [n, d] = list(map(int, input().split()))
    points = []
    for i in range(n):
        val = list(map(int, input().split()))
        val.append(i)
        points.append(val)
    getAns(points, d)
main()