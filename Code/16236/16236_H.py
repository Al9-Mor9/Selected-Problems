import sys
sys.stdin = open('input.txt', 'r')
#####
from collections import deque

def find(a, b, s):
    dist = [[0]*n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    # 거리 담는 리스트
    # bfs로 쭉 뻗어나감
    tmp = []
    while q:
        _x, _y = q.popleft()
        for dx, dy in dr:
            _nx = _x + dx
            _ny = _y + dy
            if 0 <= _nx < n and 0 <= _ny < n and not visited[_nx][_ny]:
                # 현재 사이즈보다 작거나 같으면
                if arr[_nx][_ny] <= s:
                    q.append([_nx, _ny])
                    visited[_nx][_ny] = 1
                    dist[_nx][_ny] = dist[_x][_y] + 1
                    # 해당 좌표에 먹을 수 있는 물고기가 있으면 tmp append
                    if arr[_nx][_ny] < s and arr[_nx][_ny] != 0:
                        tmp.append([_nx, _ny, dist[_nx][_ny]])
    # 1순위 : 가까운 거리, 2순위 : 위, 3순위 : 왼쪽
    return sorted(tmp, key=lambda X: (-X[2], -X[0], -X[1]))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
exp = 0     # 경험치
size = 2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j

res = 0
while True:
    shark = find(x, y, size)
    # shark가 비어있게 되면 갈 곳이 없으므로 종료
    if not shark:
        break
    nx, ny, dist = shark.pop()

    res += dist
    # 현재 위치, 갈 위치 둘 다 0으로 초기화 해야함
    arr[x][y], arr[nx][ny] = 0, 0

    x, y = nx, ny
    exp += 1
    if exp == size:
        size += 1
        exp = 0

print(res)
