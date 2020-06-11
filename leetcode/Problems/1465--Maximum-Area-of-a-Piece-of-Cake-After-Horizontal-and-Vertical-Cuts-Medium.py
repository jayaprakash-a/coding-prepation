class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        hDiff = []
        vDiff = []
        modVal = 10**9+7
        for i in range(len(horizontalCuts)-1):
            hDiff.append(horizontalCuts[i+1]-horizontalCuts[i])
        
        for i in range(len(verticalCuts)-1):
            vDiff.append(verticalCuts[i+1]-verticalCuts[i])
        
        # print(hDiff)
        # print(vDiff)
        return ((max(hDiff)%modVal)*(max(vDiff)%modVal))%modVal