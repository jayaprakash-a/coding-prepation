class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dst, src = [], []
        for [s, d] in paths:
            dst.append(d)
            src.append(s)
        
        for d in dst:
            if d not in src:
                return d