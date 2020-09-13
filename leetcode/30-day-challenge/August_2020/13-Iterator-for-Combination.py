class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.word = characters
        self.len = combinationLength
        self.combinations = []
        self.genCombinations('', 0)
        self.curr = 0
    
    def genCombinations(self, s, start):
        if len(s) == self.len:
            self.combinations.append(s)
            return
        for i in range(start, len(self.word)):
            self.genCombinations(s + self.word[i], i + 1)
    

    def next(self) -> str:
        self.curr += 1
        return self.combinations[self.curr-1]


    def hasNext(self) -> bool:
        return self.curr < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()