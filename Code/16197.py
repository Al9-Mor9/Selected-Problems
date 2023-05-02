N, M = map(int, input().split())
arr = [list (input()) for _ in range(N)]

visited = []    # 방문 확인 배열
coin = []       # 두 동전의 위치 저장 배열

answer = 11

def DFS(coin_1, coin_2, cnt):
  global answer
  x1, y1 = coin_1
  x2, y2 = coin_2

  if cnt > 10:                  # 버튼을 10번 이상 누르면 중단
      return
  if x1 == x2 and y1 == y2:     # 두 동전이 같은 곳에 위치하게 되면 중단
      return
  if (x1 < 0 or x1 >= N or y1 < 0 or y1 >= M) and (x2 < 0 or x2 >= N or y2 < 0 or y2 >= M): # 두 동전의 위치가 모두 배열 밖으로 벗어나면 중단
      return
  if (x1 < 0 or x1 >= N or y1 < 0 or y1 >= M) or (x2 < 0 or x2 >= N or y2 < 0 or y2 >= M):  # 두 동전 중 하나의 위치만 밖으로 벗어나면 cnt값과 answer 값중 작은 값 반환
      answer = min(cnt, answer)
      return

  for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):                            # 위 4조건에 모두 해당하지 않으면 for 문으로 4방향 검사
    nx1, ny1 = x1+dx, y1+dy
    nx2, ny2 = x2+dx, y2+dy
  
    if 0 <= nx1 <N and 0 <= ny1 < M and 0 <= nx2 <N and 0 <= ny2 < M:   # 만약 움직인 두 동전의 위치가 모두 배열 안에 있다면
      if (nx1, ny1, nx2, ny2) not in visited and arr[nx1][ny1] != '#' and arr[nx2][ny2] != '#': # 두 동전의 위치가 모두 벽이 아니고 두 동전 위치 모두 방문한 적이 없다면
        visited.append((nx1, ny1, nx2, ny2))
        DFS((nx1, ny1),(nx2, ny2), cnt+1)
        visited.pop()   
      elif arr[nx1][ny1] == '#' and arr[nx2][ny2] != '#':               # 1번 동전만 벽에 위치할 경우에는
          visited.append((nx1, ny1, nx2, ny2))
          DFS((x1, y1), (nx2, ny2), cnt+1)
          visited.pop()    
      elif arr[nx1][ny1] != '#' and arr[nx2][ny2] == '#':               # 2번 동전만 벽에 위치할 경우에는
          visited.append((nx1, ny1, nx2, ny2))
          DFS((nx1, ny1), (x2, y2), cnt+1)
          visited.pop()
    else:
       visited.append((nx1, ny1, nx2, ny2))
       DFS((nx1, ny1),(nx2, ny2), cnt+1)
       visited.pop()


# 입력 받은 배열에서 코인의 위치 찾고 따로 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            coin.append((i,j))

DFS(coin[0], coin[1], 0)

if answer <= 10:
    print(answer)
else:
    print(-1)