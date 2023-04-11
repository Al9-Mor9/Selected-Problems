import sys
sys.stdin = open("input.txt", "r")

# 어떤 두 샘플의 무게의 차이를 물어봄
# 어떤 두 샘플의 무게차를 구할 수 있는지 여부...
# 샘플의 개수:          2 <= n <= 100,000
# 측정 수 + 쿼리 수:    1 <= m <= 100,000

# 신장 트리와도 같다.
# w가 1,000,000 이하의 정수
# 그렇다면 어느 두 샘플은 최대
# 100,000 x 1,000,000 만큼 차이가 날 수 있다.
# 일관성을 유지하기 때문에 짧은 경로를 찾는 등
# 업데이트 되는 경우가 없다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def find(x):
    if x == p[x]:
        return x
    else:
        r = find(p[x])
        d[x] += d[p[x]]
        p[x] = r
        return p[x]
    
def union(x, y, w):
    px, py = p[x], p[y]
    if px != py:
        p[py] = px
        d[py] = d[x] + w - d[y]

while True:
    n, m = map(int, input().split())
    p = [i for i in range(n + 1)]
    d = [0 for _ in range(n + 1)]
    if not n and not m: break

    for _ in range(m):
        q = list(input().split())
        find(int(q[1]))
        find(int(q[2]))
        if q[0] == "!":
            union(int(q[1]), int(q[2]), int(q[3]))
        else:
            print(d[int(q[2])] - d[int(q[1])] if find(int(q[1])) == find(int(q[2])) else "UNKNOWN")
    print(p) 
    print(d)

# 4 7
# ! 1 2 100
# ? 2 3
# ! 2 3 100
# ? 2 3
# ? 1 3
# ! 4 3 150
# ? 4 1


# UNKNOWN
# 100
# 200
# -50
# [0, 4, 1, 1, 4]
# [0, -50, 100, 200, 0]

# memory out
'''
while True:
    n, m = map(int, input().split())
    if not n and not m: sys.exit()

    arr = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(m):
        query = list(input().split())
        a, b = int(query[1]), int(query[2])

        if query[0] == '!':
            w = int(query[3])
            arr[a][b] = w
            arr[b][a] = -w
            for i in range(1, n + 1):
                if arr[a][i] != False and arr[b][i] == False:
                    arr[b][i] = arr[b][a] + arr[a][i]
                    arr[i][b] = - arr[b][i]
                if arr[a][i] == False and arr[b][i] != False:
                    arr[a][i] = arr[a][b] + arr[b][i]
                    arr[i][a] = - arr[a][i]
        else:
            print(arr[a][b] if arr[a][b] != False else "UNKNOWN")
'''


