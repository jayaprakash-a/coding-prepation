from collections import *
import heapq
def getAns(n, edges):
	# edges = sorted(edges, key=lambda x:(x[2]))
	maxLen = sum([edges[i][2] for i in range(len(edges))])
	edgeList = defaultdict(list)
	for [s,d,w] in edges:
		edgeList[s-1].append([d-1, w])
	# print(edgeList)
	edgeDist = [[i, maxLen+1] for i in range(n)]
	edgeDist[0][1] = 0
	distance = [[0, 0]]
	heapq.heapify(distance)
	heapEntries = set()

	for _ in range(n):
		# print(distance, end = ' ')
		node = heapq.heappop(distance)
		# print(node[1])
		for [dest, weight] in edgeList[node[1]]:
			# print(node, dest, weight)
			if edgeDist[dest][1] > edgeDist[node[1]][1] + weight:
				edgeDist[dest][1] = edgeDist[node[1]][1] + weight
				isPresent = False
				for i in range(len(distance)):
					if distance[i][1] == dest:
						distance[i][0] = edgeDist[dest][1]
						heapq.heapify(distance)
						isPresent = True
						break
				if not isPresent:
					heapq.heappush(distance, [edgeDist[dest][1], dest])
		# print(edgeDist)
	for i in range(len(edgeDist)):
		print(edgeDist[i][1], end=' ')
	print()
	# return edgeDist

def main():
	[n, m] = list(map(int, input().split()))
	edges = []
	for _ in range(m):
		edge = list(map(int, input().split()))
		edges.append(edge)
	getAns(n, edges)
main()