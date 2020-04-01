class Solution:
#     Both answer are working but using regex takes more time.
    
#     def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
#         answer = []
#         lowercase = '[a-z]*'
#         regexpattern = lowercase.join(list(pattern))
#         regexpattern = '^'+lowercase+regexpattern+lowercase+'$'

#         pattern = re.compile(regexpattern)
        
#         for query in queries:
#             answer.append(pattern.match(query))
#         return answer
            
            
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        answer = []
        for query in queries:
            sol = True
            i, j = 0, 0
            while(i < len(query) and j < len(pattern)):
                ch = pattern[j]
                if ch == query[i]:
                    j += 1
                else:
                    if query[i].isupper():
                        sol = False
                        break
                i += 1
            if not sol:
                answer.append(False)
                continue
            if  i == len(query):
                answer.append(j == len(pattern))
            else:
                while(i < len(query) and query[i].islower()):
                    i += 1
                if i == len(query):
                    answer.append(True)
                else:
                    answer.append(False)
        return answer
                    
                
            
        