#include <iostream>
using namespace std;
const long long MAXN = 1000001;

int N, M, K;
long long nums[MAXN];
long long segtree[MAXN * 4], lazy[MAXN * 4];
int a;
long long b, c, d;

long long init(long long start, long long end, long long index){
    if (start == end) return segtree[index] = nums[start];
    long long mid = (start + end) / 2;
    return segtree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1);
}

void updateLazy(int start, int end, int node){
    if (lazy[node]){//아직 업데이트되지 않은 게 있으면 업데이트
        segtree[node] += (end - start + 1) * lazy[node];
        if (start != end){//리프 노드가 아닌 경우
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
};

void updateRange(int start, int end, int left, int right, int node, long long val){
    updateLazy(start, end, node);
    if (right < start || end < left) return; 
    if (left <= start && end <= right){
        lazy[node] += val;
        updateLazy(start, end, node);
        return;
    }
    int mid = (start + end) / 2;
    updateRange(start, mid, left, right, node * 2, val);
    updateRange(mid + 1, end, left, right, node * 2 + 1, val);
    segtree[node] = segtree[node * 2] + segtree[node * 2 + 1];
}

long long query(int start, int end, int left, int right, int node){
    updateLazy(start, end, node);
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return segtree[node];
    int mid = (start + end) / 2;
    return query(start, mid, left, right, node * 2) + query(mid + 1, end, left, right, node * 2 + 1);
}

int main(){
    scanf("%d%d%d", &N, &M, &K);
    for (long long i = 1; i <= N; i++) scanf("%lld", &nums[i]);
    init(1, N, 1);

    for (long long i = 0; i < M + K; i++){
        scanf("%d", &a);
        if (a == 1){
            scanf("%lld%lld%lld", &b, &c ,&d);
            updateRange(1, N, b, c, 1, d);
        }
        else {
            scanf("%lld%lld", &b, &c);
            printf("%lld\n", query(1, N, b, c, 1));
        }
    }
}
