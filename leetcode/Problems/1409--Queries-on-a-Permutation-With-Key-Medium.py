class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = list(range(1,m+1))
        answer = []
        for query in queries:
            
            index = perm.index(query)
            # print(perm, query, index)
            answer += [index]
            perm.remove(query)
            perm.insert(0, query)
            
        return answer
        