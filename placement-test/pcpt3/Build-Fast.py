def getAns(n, k, t, heights):
    def getSeq(val, k):
        prev = 0
        sumVal = 0
        count = 0
        for i in range(len(heights)): 
            sumVal += heights[i] 
            if (sumVal > val): 
                print(prev, i-1)
                count += 1
                sumVal = heights[i] 
                prev = i
        print(prev, len(heights)-1)
        count += 1
        for _ in range(k-count):
            print(-1)
    def check(mid, k):
        count = 0
        sumVal = 0
        for i in range(len(heights)): 
            if (heights[i] > mid): 
                return False
            sumVal += heights[i] 
            if (sumVal > mid): 
                count += 1
                sumVal = heights[i] 
        count += 1
        if (count <= k): 
            return True
        return False
            
    if k >= n:
        print(t*max(heights))
        for i in range(min(k, n)):
            print(i, i)
        for i in range(n - min(k, n)):
            print(-1)
        return
    for i in range(len(heights)):
        heights[i] *= t
    start = 1
    end = sum(heights)
    answer = 0
    while (start <= end): 
        mid = (start + end) // 2
        if (check(mid, k)): 
            answer = mid 
            end = mid - 1
        else: 
            start = mid + 1
    print(answer)
    getSeq(answer, k)
            
def main():
    [n, k, t] = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    getAns(n, k, t, heights)
main()