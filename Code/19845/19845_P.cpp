#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int nemonemo[250000];

int main(){
    int N, Q, x, y;
    scanf("%d%d", &N, &Q);
    queue<int> q;

    for (int i = 1; i <= N; i++){
        scanf("%d", &nemonemo[N - i]);
    }

    while (Q--){
        scanf("%d%d", &x, &y);
        int lowerbound = lower_bound(nemonemo, nemonemo + N, x) - nemonemo;
        int ans = (N - y) - lowerbound + 1;
        ans = ans > 0? ans : 0;
        ans += nemonemo[N - y] > x ? nemonemo[N - y] - x : 0;

        q.push(ans);

    }

    while (!q.empty()){
        printf("%d\n", q.front());
        q.pop();
    }

}
