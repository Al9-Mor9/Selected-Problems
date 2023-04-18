import sys
sys.stdin = open('input.txt', 'r')
#####
import copy

ar = [[] for _ in range(4)]
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(4):
        ar[i].append([lst[j*2], lst[j*2 + 1] - 1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

mx = 0
'''
for i in ar:
    print(i)
# [[7, 5], [2, 2], [15, 5], [9, 7]]
# [[3, 0], [1, 7], [14, 6], [10, 0]]
# [[6, 0], [13, 5], [4, 2], [11, 3]]
# [[16, 0], [8, 6], [5, 1], [12, 1]]
'''


# 이동 못하면 집간다했으니 상어 탐색 dfs 돌고나면 종료
def dfs(shark_x, shark_y, score, arr):  # 상어 위치, 현재까지 점수, arr
    global mx
    score += arr[shark_x][shark_y][0]   # 상어가 먹은 물고기 값 추가
    mx = max(mx, score)                 # max값 업데이트
    arr[shark_x][shark_y][0] = 0        # 현재 위치에 상어 둠

    # 물고기 switch
    for fish in range(1, 17):
        # flag false로 설정
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                # fish번 물고기가 있으면 flag 올림 == 값 갱신
                if arr[x][y][0] == fish:
                    f_x, f_y = x, y
                    break
        # 다 돌아도 fish번 물고기 없으면 다음
        if f_x == -1 and f_y == -1:
            continue
        fish_direction = arr[f_x][f_y][1]
        # 움직일 수 있는 물고기는 switch
        for i in range(8):
            nxt_direction = (fish_direction + i) % 8
            nx = f_x + dx[nxt_direction]
            ny = f_y + dy[nxt_direction]
            # 상어 없거나 빈칸이여도 갈 수 있음
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx != shark_x or ny != shark_y):
                # 갈 수 있는 방향으로 업데이트 후 switch
                arr[f_x][f_y][1] = nxt_direction
                arr[f_x][f_y], arr[nx][ny] = arr[nx][ny], arr[f_x][f_y]
                break

    # 상어 식사
    shark_direction = arr[shark_x][shark_y][1]
    for i in range(1, 4):
        nx = shark_x + dx[shark_direction] * i
        ny = shark_y + dy[shark_direction] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(arr))

# (0, 0)부터 시작, 현재 스코어, ar
dfs(0, 0, 0, ar)
print(mx)
