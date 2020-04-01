class Solution:
    def compare(self, x):
        return x[0], -x[1]
        
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) == 0:
            return []
        people = sorted(people, key=self.compare, reverse=True)
        i = 0
        answer = []
        while(len(answer) != len(people)):
            prev = people[i][0]
            mySet = []

            while(i < len(people) and people[i][0] == prev):
                mySet.append(people[i])
                i += 1
            for j in range(len(mySet)):
                answer.insert(mySet[j][1], mySet[j])
        
        return answer