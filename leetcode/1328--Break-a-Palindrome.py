class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        arr = list(palindrome)
        # print(arr)
        
        # halfIndex= len(arr)//2
        for i in range(len(arr)):
            if i == len(arr)//2:
                continue
            if arr[i] != 'a':
                arr[i] = 'a'
                return ''.join(arr)
        arr[-1] = 'b'
        return ''.join(arr)
        
        
        