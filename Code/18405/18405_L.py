import sys
sys.stdin = open("input.txt", "r")

# 문제에 이상한게 있다.
# n이 200 이라 아무리 오래걸려도 398초 안에 시험관은 꽉찬다.
# 근데 왜 s를 10000까지 주는가? 개맞을라고 진짜

from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
s, x, y = map(int, sys.stdin.readline().split())

q = deque()
for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            q.append([i, j])
            arr[i][j] = k + 1

for sec in range(1, s+1):
    n_q = deque()
    visited = [[0] * n for _ in range(n)]
    while q:
        r, c = q.popleft()
        tmp = k + 1
        for nr, nc in [[r, c + 1], [r + 1, c], 
                       [r - 1, c], [r, c - 1]]:
            if 0 <= nr < n and 0 <= nc < n and \
                not visited[nr][nc]:
                tmp = min(tmp, arr[nr][nc])

        if tmp != k + 1:
            arr[r][c] = tmp
            visited[r][c] = 1
        else:
            n_q.append([r, c])
    q = n_q 

print(arr[x-1][y-1] if arr[x-1][y-1] != k + 1 else 0)










