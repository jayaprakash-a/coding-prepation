import collections
import sys
def getAns(cities, costs):
    costLoc = {}
    city = {}
    maxCost = max(costs)+1
    for i in range(len(costs)):
        city[tuple(cities[i])] = min(costs[i], city.get(tuple(cities[i]), maxCost))
    for i in range(len(cities)):
        cities[i].append(sys.maxsize)
    answer = 0
    def filFunc(x):
        # print('comp', x[:2], minCity)
        return x[:2] != minCity
    while cities:
        minDist = sys.maxsize
        minCity = []
        for entry in cities:
            if entry[2] < minDist:
                minDist = entry[2]
                minCity = entry[:2]
            if city[tuple(entry[:2])] < minDist:
                minDist = city[tuple(entry[:2])]
                minCity = entry[:2]
        answer += minDist
        # print(minCity, cities)
        cities = list(filter(filFunc, cities) )
        # print(cities)
        for i in range(len(cities)):
            cities[i][2] = min(cities[i][2], abs(minCity[0]-cities[i][0])+abs(minCity[1]-cities[i][1]))
    return answer
def main():
    n = int(input().strip())
    cities = []
    for _ in range(n):
        [x, y] = list(map(int, input().split()))
        cities.append([x, y])
    costs = list(map(int, input().split()))
    print(getAns(cities, costs))
main()