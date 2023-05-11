#include <iostream>
#include <vector>
using namespace std;
const int MAXN = 1001;	

int N, M, n, t;
vector<vector<int>> task;
bool visited[MAXN];
int by[MAXN];

bool match(int a){
	if (visited[a]) return false;
	visited[a] = true;
	for (int possibleTask : task[a]){
		if (!by[possibleTask] || match(by[possibleTask])){
			by[possibleTask] = a;
			return true;
		}
	}
	return false;
} 

int main(){
	scanf("%d%d", &N, &M);
	task.resize(N + 1);

	for (int i = 1; i <= N; i++){
		scanf("%d", &n);
		for (int j = 0; j < n; j++) {
			scanf("%d", &t);
			task[i].push_back(t);
		}
	}

	int ans = 0;
	for (int i = 1; i <= N; i++){
		for (int j = 0; j <= N; j++) visited[j] = false;
		if (match(i)) ans++;
	}
	/**
	for (int i = 1; i <= M; i++){
		printf("%d - %d\n", by[i], i);
	}
	*/	
	printf("%d", ans);
}
