class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for entry in logs:
            if '../' in entry:
                if stack:
                    stack.pop()
            elif './' in entry:
                continue
            else:
                stack.append(entry)
        return len(stack)