class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) <= 2:
            return True
        stack = []
        stack.append(pushed[0])
        push, pop = 1, 0
        
        while(pop != len(popped)):
            # print(stack, push, pop)
            if len(stack) == 0 and push < len(pushed):
                stack.append(pushed[push])
                push += 1
            elif len(stack) == 0 and push == len(pushed):
                return False
            elif popped[pop] != stack[-1] and push == len(pushed):
                return False
            elif popped[pop] != stack[-1]:
                stack.append(pushed[push])
                push += 1
            elif popped[pop] == stack[-1]:
                stack.pop()
                pop += 1
        return pop == len(popped) and push == len(pushed)
                