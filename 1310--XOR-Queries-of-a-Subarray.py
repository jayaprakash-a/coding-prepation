class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorArray = [0]
        answer = 0
        answerArray = []
        for num in arr:
            answer = answer ^ num
            xorArray.append(answer)
        for entry in queries:
            print(entry)
            if entry[0] == entry[1]:
                answerArray.append(arr[entry[0]])
            else:
                answerArray.append(xorArray[entry[0]] ^ xorArray[entry[1]+1])
        return answerArray
            