import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



from collections import deque

ans = []
v, e = map(int, input().split())
in_degree = [0 for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]
q = deque()

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, v + 1):
    if not in_degree[i]:
        q.append(i)


while q:
    cur = q.popleft()
    print(cur, end=" ")

    for node in graph[cur]:
        in_degree[node] -= 1
        if not in_degree[node]:
            q.append(node)

