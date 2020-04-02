class MagicDictionary:

    def __init__(self):

        self.dictionary = {}

    def buildDict(self, dict: List[str]) -> None:

        for word in dict:
            if len(word) not in self.dictionary.keys():
                self.dictionary[len(word)] = [word]
            else:
                self.dictionary[len(word)] += [word]
        

    def search(self, word: str) -> bool:
        
        if len(word) not in self.dictionary.keys():
            return False
        for w in self.dictionary[len(word)]:
            changes = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    changes += 1
                    if changes > 1:
                        break
            if changes == 1:
                return True
        
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)