class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        a = [ord(ch)-ord('a') for ch in s1]
        b = [ord(ch)-ord('a') for ch in s2]
        # print(a)
        # print(b)
        # print('-------')
        if len(s1)>len(s2):
            return False
        aCh = [0]*26
        for ascii in a:
            aCh[ascii] += 1
        
        bWindow = [0]*26
        for ascii in b[:len(s1)]:
            bWindow[ascii] += 1
        
        for i in range(len(s1)-1, len(s2)):
            
            # print(aCh)
            # print(bWindow)
            # print('--', i, '---')
            if aCh == bWindow:
                return True
            # print(i-len(s1), b[i-len(s1)])
            bWindow[b[i-len(s1)+1]] -= 1
            if i+1 <= len(s2)-1:
                # print('voila', b[i+1], b[i-len(s1)])
                bWindow[b[i+1]] += 1
        
        return False