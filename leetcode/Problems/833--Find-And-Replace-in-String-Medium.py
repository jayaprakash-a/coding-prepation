class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        charList = list(S)
        for index in range(len(indexes)):
            ind, src, tgt = indexes[index], sources[index], targets[index]
            # print(ind, src, tgt)
            if S[ind: ind+len(src)] == src:
                charList[ind] = tgt
                for i in range(ind + 1, ind+len(src), 1):
                    charList[i] = ''
        return ''.join(charList)
        