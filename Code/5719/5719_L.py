import sys
sys.stdin = open("input.txt", "r")



# 최단 거리 다음으로 최단 경로를 출력해라..
# 최단 값이 3, 3, 4, 5, ... 라면 4를 출력
# 만약 3, 3 만 있으면 거의 최단경로는 없다.

# 그나마 시작점 끝점 한 쌍을 처음에 먼저 주니까
# 다익스트라를 어떻게 뭐 개조 할 거 같은데..

# 2 <= n <= 500
# 1 <= m <= 10,000


from collections import deque
import sys
import heapq

# formal한 우선순위 큐를 쓰는 다익스트라이다.
def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0 
    while q:  
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in g[now]:
            cost = dist + g[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

# 최단거리를 만드는 노선을 없앤다..
def bfs():
    q = deque()
    q.append(d)
    while q:
        v = q.popleft()
        if v == s: continue  
        for pre_v, pre_c in r[v]:
            if distance[pre_v] + g[pre_v][v] == distance[v]:
                if (pre_v, v) not in remove_List:
                    remove_List.append((pre_v, v))
                    q.append(pre_v)


# 구현
inf = 50000
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0: break
    s, d = map(int, sys.stdin.readline().split())
    g = [dict() for _ in range(n)]
    r = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        g[u][v] = p
        r[v].append((u, p))

    distance = [inf] * n
    dijkstra()

    remove_List = []
    bfs()
    print(remove_List)

    for u, v in remove_List: del g[u][v]

    distance = [inf] * n
    dijkstra()
    
    print(-1 if distance[d] == inf else distance[d])