class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prod = sorted(products)
        answer = []
        for i in range(len(searchWord)):
            count, ind = 0 , 0
            subAns = []
            while(count < 3 and ind < len(prod)):
                if ind >= len(prod):
                    break
                if i >= len(prod[ind]):
                    prod.pop(ind)
                    continue
                if prod[ind][i] == searchWord[i]:
                    count += 1
                    subAns.append(prod[ind])
                    ind += 1
                else:
                    prod.pop(ind)
            j = ind
            while(j < len(prod)):
                if prod[j][i]!=searchWord[i]:
                    prod.pop(j)
                else:
                    j+=1
            answer.append(subAns)
        
        return answer
                
        