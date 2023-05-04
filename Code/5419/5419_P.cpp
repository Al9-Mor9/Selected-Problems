#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN = 75000;

int T, n, x, y;
vector<pair<int, int>> v;
vector<int> ys;

long long tree[MAXN * 4];

bool compare(pair<int, int> &a, pair<int, int> &b){
    if (a.first == b.first) return a.second > b.second;
    return a.first < b.first;
}

void update(int start, int end, int left, int right, int node, int val){
    if (end < left || right < start) return;
    tree[node] += val;
    if (start == end) return;
    int mid = (start + end) / 2;
    update(start, mid, left, right, node * 2, val);
    update(mid + 1, end, left, right, node * 2 + 1, val); 
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long query(int start, int end, int left, int right, int node){
    if (end < left || right < start) return 0;
    if (left <= start && end <= right) return tree[node];
    int mid = (start + end) / 2;
    return query(start, mid, left, right, node * 2) + query(mid + 1, end, left, right, node * 2 + 1); 
}

int main(){
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (int i = 0; i < MAXN * 4; i++) tree[i] = 0;
        v.clear();
        ys.clear();
        for (int i = 0; i < n; i++){
            scanf("%d%d", &x, &y);
            v.emplace_back(x, y);
            ys.emplace_back(y);
        }
        //y 좌표 압축
        sort(ys.begin(), ys.end());
        for (int i = 0; i < n; i++){
            v[i].second = lower_bound(ys.begin(), ys.end(), v[i].second) - ys.begin();
        } 
        sort(v.begin(), v.end(), compare);
        long long ans = 0;
        for (int i = 0; i < n; i++){
            ans += query(0, n - 1, v[i].second, n - 1, 1);
            update(0, n - 1, v[i].second, v[i].second, 1, 1);
        }
        printf("%lld\n", ans);
    }
}
