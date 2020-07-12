class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 2:
            return False
        if n == 3:
            return True
        if n == 4:
            return True
        squares = [i*i for i in range(1, floor(sqrt(n))+1)]
        
        answer = [None for _ in range(n+1)]
        answer[1] = True
        answer[2] = False
        answer[3] = True
        answer[4] = True
        
        for i in range(5, n+1):
            if i in squares:
                answer[i] = True
                continue
            ind = 1
            while ind*ind <= i:
                if answer[i-ind*ind] == False:
                    answer[i] = True
                    break
                ind += 1
            if answer[i] == None:
                answer[i] = False
        return answer[n]