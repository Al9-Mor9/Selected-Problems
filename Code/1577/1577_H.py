import sys
sys.stdin = open('input.txt', 'r')
#####
# ㄴ'ㅇ'ㄱ
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# true, true : x축 / y축 공사중
dp = [[[0, [True, True]] for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

c = int(input())
for _ in range(c):
    a, b, c, d = map(int, input().split())
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b
    # x축이면 d = 0, y축이면 d = 1
    if c-a > d-b:
        d = 0
    else:
        d = 1
    # 해당 지점에서 첫번째 true(x축) 또는 두 번째 true(y축)는 갈 수 없음(false)으로 바꿈
    dp[a][b][1][d] = False
# for i in dp:
#     print(i)

# 누적합...?
moves = [[1, 0], [0, 1]]
for x in range(n + 1):
    for y in range(m + 1):
        for k in range(2):
            nx = x + moves[k][0]
            ny = y + moves[k][1]
            if nx <= n and ny <= m and dp[x][y][1][k] == True:
                dp[nx][ny][0] += dp[x][y][0]
# for i in dp:
#     for j in i:
#         print(f'{j[0]}\t', end='')
#     print()
'''
1	0	0	0	0	0	0	
1	1	1	1	1	1	1	
1	2	3	4	5	6	7	
1	3	6	10	15	21	28	
1	4	10	20	35	56	84	
1	5	15	35	70	126	210	
1	6	21	56	126	252	252
'''
print(dp[n][m][0])
