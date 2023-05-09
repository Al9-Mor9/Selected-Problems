import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dAlpha = ['d', 'l', 'r', 'u']
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
answer = 'z'


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer

    if k < cnt + abs(x - r) + abs(y - c):
        return
    # 종료조건
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and prev_s < answer:
            dfs(n, m, nx, ny, r, c, prev_s+dAlpha[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    # 거리부터 확인 - 거리 짧거나 진동하면 불가능
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    x-=1
    y-=1
    r-=1
    c-=1
    dfs(n, m, x, y, r, c, '', 0, k)
    return answer
