from collections import deque


class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        posString = deque()
        posString.append('a')
        posString.append('b')
        posString.append('c')

        # valStrings = []
        while(len(posString) > 0):
            if len(posString[0]) == n:
                k -= 1
                if k == 0:
                    return posString.popleft()
                # valStrings.append(posString.popleft())
                # continue
            prevString = posString.popleft()
            s1, s2 = '', ''
            if prevString[-1] == 'a':
                s1 = prevString + 'b'
                s2 = prevString + 'c'
            elif prevString[-1] == 'b':
                s1 = prevString + 'a'
                s2 = prevString + 'c'
            elif prevString[-1] == 'c':
                s1 = prevString + 'a'
                s2 = prevString + 'b'

            if len(s1) <= n:
                posString.append(s1)
                posString.append(s2)
        # valStrings = sorted(valStrings)
        # print(len(valStrings))
        # if k <= len(valStrings):
            # return valStrings[k-1]
        return ''
