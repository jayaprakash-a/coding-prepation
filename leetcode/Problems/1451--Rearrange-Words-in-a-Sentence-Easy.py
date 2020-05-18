class Solution:
    def compare(self, x):
        return len(x)
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        answer = ''
        words = sorted(words, key=self.compare)
        answer = words[0][0].upper() + words[0][1:].lower() + ' '
        for word in words[1:]:
            answer += word.lower()
            answer += ' '
        return answer[:-1]