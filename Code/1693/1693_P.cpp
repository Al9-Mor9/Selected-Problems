#include <iostream>
#include <vector>
#define MAXCOLOR 18
using namespace std;

int n, a, b;
vector<vector<int>> adj;
vector<vector<int>> child;
int parent[100001];
int dp[100001][18];

void makeTree(int cur){
    for (int next : adj[cur]){
        if (parent[next]) continue;
        parent[next] = cur;
        child[cur].push_back(next);
        makeTree(next);
    }
}

int min(int a, int b){
    return a < b ? a : b;
}

int paint(int nodeNum, int color){
    if (dp[nodeNum][color] != 0) return dp[nodeNum][color];
    
    int subtree = 0;
    for (int next : child[nodeNum]){
        int tmp = 2147483647;
        for (int i = 1; i <= MAXCOLOR; i++) {
            if (i == color) continue;
            tmp = min(tmp, paint(next, i));
        }
        subtree += tmp;
    }    

    return dp[nodeNum][color] = subtree + color;
}

int main(){
    scanf("%d", &n);
    adj.resize(n + 1);
    child.resize(n + 1); 
    for (int i = 0; i < n - 1; i++){
        scanf("%d%d", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    parent[1] = 1;
    makeTree(1);//1을 root로 가지는 트리 만들기
    //i번째가 

    int ans = INT32_MAX; 
    for (int i = 1; i <= MAXCOLOR; i++){
        ans = min(ans, paint(1, i));
    }

    printf("%d", ans);
}
