class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        for i in range(2, n+1):
            factorial *= i
        arr = [str(i) for i in range(1, n+1)]
        answer = ''
        k -= 1
        while n > 0:
            factorial //= n          
            n -= 1            
            index, k = divmod(k, factorial)
            answer += arr[index]
            arr.pop(index)
        return answer