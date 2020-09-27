class Solution(object):
    def maxUniqueSplit(self, s):

        seen = set()
        self.answer = 0
        def backtrack(ind):
            if ind == len(s):
                self.answer = max(self.answer, len(seen))
            word = ''
            for i in range(ind, len(s)):
                word += s[i]
                if word not in seen:
                    seen.add(word)
                    backtrack(i+1)
                    seen.remove(word)
        backtrack(0)
        return self.answer