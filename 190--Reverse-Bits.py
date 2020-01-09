class Solution:
    def reverseBits(self, n: int) -> int:
        answer = "{:032b}".format(n)
        # print(answer)
        # return s)tr(n)[::-1]
        return int(answer[::-1], 2)
        