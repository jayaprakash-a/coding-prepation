class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                snew += ch
        return snew.lower() == snew.lower()[::-1]
#         sprime = list(filter(lambda x: x.isalpha() or x.isdigit(), s) )

        
#         str1 = ''.join([str(elem) for elem in sprime]) 

#         return str1.lower() == str1.lower()[::-1]
        