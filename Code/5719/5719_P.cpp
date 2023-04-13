#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define INF 9999999

int N, M, S, D, U, V, P;
vector<vector<pair<int, int>>> edge;
vector<vector<int>> reducingEdge;
priority_queue<int, vector<int>, greater<>> q;
int dist[500];
bool isOnRoute[500][500];

bool dijk(){
	for (int i = 0; i < N; i++) dist[i] = INF;
	
	dist[S] = 0;	
	q.push(S);
	while (!q.empty()){
		int top = q.top();
		q.pop();
		for (pair<int, int> next : edge[top]){
			int nNode = next.first;
			int nCost = next.second;
			
			if (isOnRoute[nNode][top]) continue;
			if (dist[nNode] < dist[top] + nCost) continue;
			if (dist[nNode] > dist[top] + nCost) {
				reducingEdge[nNode].clear();
				dist[nNode] = dist[top] + nCost;
				q.push(nNode);
			}
			reducingEdge[nNode].push_back(top);	
		}
	}
	if (dist[D] == INF) return false;
	return true;
}

void trace(){
	queue<int> onRoute;
	onRoute.push(D);
	
	while (!onRoute.empty()){
		int front = onRoute.front();
		onRoute.pop();
		for (int prev : reducingEdge[front]) {
			if (isOnRoute[front][prev]) continue;
			isOnRoute[front][prev] = true;
			onRoute.push(prev);
		}
	}
}

int main(){
	while (true){
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) isOnRoute[i][j] = false;
		reducingEdge.clear();	
		reducingEdge.resize(N);
		edge.clear();
		edge.resize(N);

		if (!N && !M) return 0;
		scanf("%d%d", &S, &D);

		for (int i = 0; i < M; i++){
			scanf("%d%d%d", &U, &V, &P);
			edge[U].push_back({V, P});
		}

		if (!dijk()) {
			printf("-1\n");
			continue;
		}
		trace();
		if (!dijk()) printf("-1\n");
		else printf("%d\n", dist[D]);
	}
}
