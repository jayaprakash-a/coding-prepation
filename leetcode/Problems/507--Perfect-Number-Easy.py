class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        answer = 0
        for i in range(1, 1+math.ceil(math.sqrt(num))):
            if num%i == 0 and i <= num//i and i!=num:
                # print(i)
                answer += i
                if i!= num//i and num//i != num:
                    # print(num//i)
                    answer += (num//i)
        return answer==num
        