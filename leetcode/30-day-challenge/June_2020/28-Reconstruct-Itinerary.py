class Solution:
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     def helper(x):
    #         return x[0], x[1]
    #     tickets = sorted(tickets, key=helper)
    #     travel = defaultdict(deque)
    #     for [s, d] in tickets:
    #         travel[s].append(d)
    #     answer = []
    #     start = 'JFK'
    #     while True:
    #         answer.append(start)
    #         if len(travel[start]) > 0:
    #             start = travel[start].popleft()
    #         else:
    #             break
    #     return answer
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]