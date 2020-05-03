class Solution:
    def removeDuplicateLetters(self, text: str) -> str:
        lastSeen = {}
        
        for i, ch in enumerate(text):
            lastSeen[ch] = i
        
        stack = []
        
        for i, ch in enumerate(text):
            if ch in stack:
                continue
#           While stack is not empty and stack top is a higher character and will occur later in the string
            while stack and stack[-1] > ch and lastSeen[stack[-1]] > i:
                stack.pop()
            stack.append(ch)
        
        return ''.join(stack)