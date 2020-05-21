class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileContent = collections.defaultdict(list)
        
        for entry in paths:
            splitVal = entry.split(' ')
            path = splitVal[0]
            for entries in splitVal[1:]:
                div = entries.split('(')
                fileContent[div[1][:-1]] += [path + '/' + div[0]]
        
        answer = [entry for entry in fileContent.values()  if len(entry) > 1]

        return answer
        
                                   