class Solution:
    def simplifyPath(self, path: str) -> str:
        folderSplit = path.split('/')
        # print(folderSplit)
        folderStack = []
        
        for i in range(len(folderSplit)):
            if len(folderSplit[i]) == 0:
                continue
            elif folderSplit[i] == '.':
                continue
            elif folderSplit[i] == '..':
                if len(folderStack) > 0:
                    folderStack.pop()
            else:
                folderStack.append(folderSplit[i])
        
        answer = '/'.join(folderStack)
        return '/'+answer