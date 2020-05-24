class Solution:
    def compare(self, x):
        return x[1]
    def frequencySort(self, s: str) -> str:
        charCount = sorted(collections.Counter(s).items(), key=self.compare, reverse=True)
        # print(charCount)
        answer = ''
        for [ch, count] in charCount:
            answer += (ch*count)
        return answer