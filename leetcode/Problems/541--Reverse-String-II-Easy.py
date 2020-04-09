class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = []
        for i in range(0, len(s), k):
            last = min(i+k, len(s))
            answer.append(s[i:last])
        ans = ''
        for i in range(0, len(answer), 2):
            answer[i] = answer[i][::-1]
        return ''.join(answer)
        