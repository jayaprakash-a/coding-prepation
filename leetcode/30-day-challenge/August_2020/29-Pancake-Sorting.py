class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        answer = []
        for num in range(len(A), 1, -1):
            index = A.index(num)
            answer += [index+1, num]
            A = A[:index+1][::-1] + A[index+1:]
            # print(A)
            A = A[:num][::-1] + A[num:]
            # print(A)
        return answer