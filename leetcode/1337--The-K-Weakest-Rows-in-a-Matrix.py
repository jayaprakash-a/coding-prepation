class Solution:
    def comparator(self, x):
        return x[1], x[0]
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        
        for i in range(len(mat)):
            count = 0
            for entry in mat[i]:
                if entry == 0:
                    break
                count += 1
            soldiers.append((i, count))
            
        sortedSoldiers = sorted(soldiers, key=self.comparator)
        print(sortedSoldiers)
        answer = []
        for i in range(k):
            answer.append(sortedSoldiers[i][0])
            
        return answer
            
            
                