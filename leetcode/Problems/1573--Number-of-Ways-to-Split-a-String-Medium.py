class Solution:
    def numWays(self, s: str) -> int:
        count = s.count('1')
        if count % 3 != 0:
            return 0
        if count == 0:
            return ((len(s)-1)*(len(s)-2)//2)%(10**9+7)
        s1, e1, s2, e2 = -1, -1, -1, -1
        counter = 0
        for i in range(len(s)):
            if s[i] == '1':
                counter += 1
            if counter == count//3:
                e1 = i
                if s1 == -1:
                    s1 = i
            if counter == 2*(count//3):
                e2 = i
                if s2 == -1:
                    s2 = i
        answer = (e1-s1+1)*(e2-s2+1)%(10**9+7)
        # print(s1, e1, s2, e2)
        return answer