from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

move = 0                            # 이동 가능 여부

def bfs(x,y,visited,arr):
    global move
    people_sum = arr[x][y]          # 이동할 사람들의 합계
    cnt = 1                         # 이동이 일어난 횟수
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    tmp_lst = []                    # 이동하는 사람들의 배열을 갱신해주기 위해 기록
    tmp_lst.append((x,y))

    while queue:
        p_x, p_y = queue.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상 하 좌 우
            m_x, m_y = p_x + dx , p_y + dy

            if m_x < 0 or m_x > N-1 or m_y < 0 or m_y > N-1:    # 범위 밖이면 다시
                continue
            if visited[m_x][m_y] == 1:                          # 이미 방문했다면 다시
                continue
            if L <= abs(arr[p_x][p_y] - arr[m_x][m_y]) <= R:    # 문제 조건에 만족한다면
                visited[m_x][m_y] = 1                           # 방문 처리
                queue.append((m_x,m_y))
                cnt += 1                                        # 이동 횟수 증가
                people_sum += arr[m_x][m_y]                     # 이동 인구 추가
                tmp_lst.append((m_x, m_y))                      
    average_people = people_sum // cnt                          # 이동한 사람들의 평균 수

    if cnt > 1:                             # 이동 횟수가 한번이라도 있으면
        move = 1                            # 이동 가능 여부 1
        for a, b in tmp_lst:
            arr[a][b] = average_people      # 이동한 곳의 인구 수를 평균으로 갱신


cnt_days = 0                                # 이동이 있었던 날 
while True:
    visited = [[0] * N for _ in range(N)]
    move = 0                                # 이동 가능 여부
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i,j, visited, arr)

    if move:                           # 이동이 가능하다면
        cnt_days += 1                  # 이동이 있는 날 += 1 
    else:
        break

print(cnt_days)