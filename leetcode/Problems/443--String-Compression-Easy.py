class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 1
        prevChar = chars[0]
        loc = 1
        prevCount = 1
        for i in range(index, len(chars)):
            if chars[i] != prevChar:                
                if prevCount != 1:
                    for ch in str(prevCount):
                        chars[loc] = ch
                        loc += 1
                    prevCount = 1
                chars[loc] = chars[i]
                prevChar = chars[i]
                loc += 1
            else:
                prevCount += 1
        if prevCount != 1:
            for ch in str(prevCount):
                chars[loc] = ch
                loc += 1
        return loc
        