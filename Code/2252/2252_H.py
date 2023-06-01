import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

# print(graph)        # [[], [3], [3], []]
# print(in_degree)    # [0, 0, 0, 2]

for i in range(1, n + 1):
    if not in_degree[i]:
        q.append(i)

# print(graph)        # [[], [3], [3], []]
# print(in_degree)    # [0, 0, 0, 2]
# print(q)            # deque([1, 2])

ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for nxt in graph[cur]:
        in_degree[nxt] -= 1
        if not in_degree[nxt]:
            q.append(nxt)

# print(graph)        # [[], [3], [3], []]
# print(in_degree)    # [0, 0, 0, 0]
# print(q)            # deque([])
print(*ans)          # 1 2 3