
K, N = map(int, input().split())            # K는 라인의 수, N은 각 라인의 작업장 수

line_arr = []
move_time = []

for i in range(N-1):
    line_with_time = list(map(int, input().split()))
    line_arr.append(line_with_time[:K])               
    move_time.append(line_with_time[-1])              # 작업장 사이의 이동시간

line_arr.append(list(map(int, input().split())))      # 마지막 작업장은 이동 시간이 따로 주어지지 않음

for i in range(N-1):
    tmp = min(line_arr[i])
    for j in range(K):
        line_arr[i+1][j] += min(line_arr[i][j], tmp + move_time[i])

print(min(line_arr[-1]))