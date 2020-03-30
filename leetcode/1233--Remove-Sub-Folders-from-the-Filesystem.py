class Solution:
    def compare(self, x):
        return x.count('/')
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSorted = sorted(folder, key=self.compare)
        # print(folderSorted)
        
        prev = folderSorted[0].count('/')
        rootFolders = set()
        answer = []
        for filePath in folderSorted:
            if filePath.count('/') == prev:
                rootFolders.add(filePath)
                answer.append(filePath)
            else:
                found = False
                for rootPath in rootFolders:
                    # print(rootPath, filePath)
                    if filePath[:len(rootPath)] == rootPath:
                        found = True
                if not found:
                    answer.append(filePath)
                    rootFolders.add(filePath)
        return answer