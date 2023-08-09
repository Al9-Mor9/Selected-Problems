import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            q.append([arr[i][j], 0, i, j])
q.sort()
q = deque(q)
while q:
    v, cnt, a, b = q.popleft()
    if cnt == s:
        continue
    for dx, dy in dr:
        nx, ny = a + dx, b + dy
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = v
            q.append([v, cnt + 1, nx, ny])
print(arr[x-1][y-1])