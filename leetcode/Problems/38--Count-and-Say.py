class Solution:
    def countAndSay(self, n: int) -> str:
        number = 1
        for i in range(n-1):
            new, count = '', 0
            prev = ''
            for ch in str(number):
                if not prev:
                    prev = ch
                    count += 1
                    continue
                if prev == ch:
                    count += 1
                else:
                    new  += str(count) + prev
                    count = 1
                    prev = ch
            new += str(count) + prev
            number = int(new)
        
        return str(number)
                