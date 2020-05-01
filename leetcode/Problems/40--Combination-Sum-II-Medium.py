class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        candidates = sorted(candidates)
        self.backtrack(candidates, target, [], 0)        
        
        return self.answer
    def backtrack(self, candidates, target, tempSoln, index):
        if target < 0:
            return
        elif target == 0:
            self.answer.append(list(tempSoln))
        else:
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                tempSoln.append(candidates[i])
                self.backtrack(candidates, target-candidates[i], tempSoln, i+1)
                tempSoln.pop()
        return