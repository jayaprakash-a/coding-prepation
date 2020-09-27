class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.child = defaultdict(deque)
        self.died = set()
    
    def birth(self, parentName: str, childName: str) -> None:
        self.child[parentName].append(childName)

    def death(self, name: str) -> None:
        self.died.add(name)

    def getInheritanceOrder(self) -> List[str]:
        answer = []
        # visited
        def dfs(name):
            if name not in self.died:
                answer.append(name)
            for ch in self.child[name]:                
                dfs(ch)
                
        dfs(self.king)
        return answer


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()