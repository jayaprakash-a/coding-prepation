class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        neighBours = {}
        for [source, dest] in edges:
            source, dest = min(source, dest), max(source, dest)
            if source not in neighBours.keys():
                neighBours[source] = [dest]
            else:
                neighBours[source] += [dest]
        
        print(neighBours)
        prob = [0]*(n+1)
        vertexSet = [1]
        prob[1] = 1
        while(len(vertexSet) != 0 and t>0):
            # print(vertexSet, t)
            t -= 1
            newSet = []
            for entry in vertexSet:
                
                if entry in neighBours.keys():
                    probUpdate = (1/len(neighBours[entry]))
                    for neigh in neighBours[entry]:
                        prob[neigh] = prob[entry] * probUpdate
                        # if neigh in neighBours.keys():
                    newSet += neighBours[entry]
                    prob[entry] = 0
            
            vertexSet = newSet
            
        
        # print(prob, target, prob[target])
        return prob[target]
                
                
        
        