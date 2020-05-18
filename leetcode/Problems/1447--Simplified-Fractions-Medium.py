class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        def check_co_prime(x, y):
            for i in range(2, x+1):
                if x%i == 0 and y%i == 0:
                    return True
            return False
        answer = []
        for denom in range(2, n+1):
            for num in range(1, denom):
                # print
                if not check_co_prime(num, denom):
                    answer.append(str(num)+'/'+str(denom))
        return answer