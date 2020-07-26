#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int n, m;
	cin >> n >> m;
	vector<vector<int>> edges(m, vector<int>(3, -1));
	for (int i = 0; i < m; ++i)	{
		for (int j = 0; j < 3; ++j){
			cin >> edges[i][j];
		}
	}
	vector<vector<pair<int,int>>> graph(n, vector<pair<int,int>>(0, 0));
	int64_t sumOfEdgeWeights = 0;
	for(auto edge: edges) {
		graph[edge[0]-1].push_back({edge[1]-1, edge[2]});
		sumOfEdgeWeights += edge[2];
	}
	vector<int64_t> minDistance(n, sumOfEdgeWeights+1);
	minDistance[0] = 0;
	priority_queue<int64_t, vector<pair<int64_t,int64_t>>, greater<pair<int64_t,int64_t>>> pq;
	pq.push({0, 0});
	for (int idx = 0; idx < n; idx++) {
		auto topOfQ = pq.top(); pq.pop();
		for (auto neighbour: graph[topOfQ.second]) {
			if (minDistance[neighbour.first] > minDistance[topOfQ.second] + neighbour.second) {
				minDistance[neighbour.first] = minDistance[topOfQ.second] + neighbour.second;
			}
		}
	}
	return 0;
}