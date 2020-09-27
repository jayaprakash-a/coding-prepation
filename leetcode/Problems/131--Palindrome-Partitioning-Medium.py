class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        palin, notpalin = set(), set()
        
        def isPalin(word):
            return word == word[::-1]
            # if word in palin:
            #     return True
            # if word in notpalin:
            #     return False
            # length = len(word)
            # for i in range(len(word)//2+1):
            #     if word[i] != word[length-i-1]:
            #         notpalin.add(word)
            #         return False
            # palin.add(word)
            # return True
        
        def backtrack(ind, s, res):
            # print('hi')
            if ind == len(s):
                # print(res)
                answer.append(list(res))
                return
            word = ''
            for i in range(ind, len(s)):
                word += s[i]
                # print(word, isPalin(word))
                if isPalin(word):
                    # print(word)
                    res.append(word)
                    backtrack(i+1, s, res)
                    res.pop()
        
        backtrack(0, s, [])
        return answer