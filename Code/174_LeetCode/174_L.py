from collections import deque


# ------------------------------------------------------------
# MinHp : 해당 지점까지 HP를 0이상으로 유지하며 가기위한 최소 Hp
# tmp : 해당 지점에서의 HP 값
# MinHp은 낮고 tmp는 높으면 좋다.

# cur -> next 일 때, 
# 이동 후, cur의 MinHp가 더 낮고, tmp가 더 높으면 무조건 가는게 좋다.
# MinHp가 더 높고, tmp가 더 낮으면 갈 필요가 없다.

# 반면 MinHp, tmp가 둘 다 높거나 낮은경우는 일단 넣어둬야한다....?
# MinHp가 더 높고, tmp의 차이가 MinHp 차이보다 낮은 경우 넣을 필요가 없다.
# 즉 queue에 넣기 위해서는...


# ------------------------------------------------------------
# 다시.. 이 문제는 부분 최적 구조를 가지고 있기 때문에...?
# 부분 최적 구조가 맞는가?
# 특정 지점까지 최소 필요한 MinHp를 구할 수는 있다.
# 다만 최소 MinHp는 더 높은데 그 지점에 도착했을 때 tmp가 압도적으로 높으면 
# 그게 차후에 좋을 수 있다. 예를 들면 ,,
# 
# 0 -9 999
# 1  1  1
# 1  1  1
#
# (MinHp, tmp) -> (1, 4) 에서 1가 정답이 될 것이다.
# 하지만 (10, 992) 를 살려두는 것이 유리하다. 

# 다음 경우로 확장된다면..
#
# 0 -9 999 1
# 1  1  1  1
# 1  1  1 -20
# 1  1 -20 1
#
# 3, 3 에서 4, 4로 가면
# (1, 4)    -> (17, -16) -> (17, -15)
# (10, 992) -> (10, 972) -> (10, 973)
# 
# 아래 경로가 채택된다..


# ------------------------------------------------------------
# 아니지 아니지..
# 
# 4, 4에서의 정답을 k라고 생각하면, 
# 위, 왼쪽에서의 값을 역으로 추적할 수 있다.
# 마치 뒤로 가는 DP 전기버스 문제를 2차원으로 만든 꼴이다.

def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
    m, n = len(dungeon), len(dungeon[0])
    DP = [[0 for _ in range(n)] for _ in range(m)]
    DP[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

    # 열을 n-1 로 고정하고 행들을 채운다.
    for i in range(m-2, -1, -1):
        DP[i][n-1] = max(1, DP[i+1][n-1] - dungeon[i][n-1])
	
	# 행을 m-1 로 고정하고 열들을 채운다.
    for j in range(n-2, -1, -1):
        DP[m-1][j] = max(1, DP[m-1][j+1] - dungeon[m-1][j])

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            next = min(DP[i+1][j], DP[i][j+1]) # 어디에서 올지 정한다.
            DP[i][j] = max(1, next - dungeon[i][j]) # 갱신하여 저장.

    return DP[0][0]


test = [[-2,-3,3],
        [-5,-10,1],
        [10,30,-5]]
answer = calculateMinimumHP(test)
print(answer)




# 다음은 정답 예시
# 84번 째 줄에서 해당 값을 사용해고 지우면서 간다.
#

def calculateMinimumHP(self, grid: list[list[int]]) -> int:
	m, n = len(grid), len(grid[0])
	for i in range(m-1, -1, -1):
		for j in range(n-1, -1, -1):
			if i==m-1 and j==n-1:
				grid[i][j] = max(1, 1-grid[i][j])
			elif i==m-1:
				grid[i][j] = max(1, grid[i][j+1] - grid[i][j])
			elif j==n-1:
				grid[i][j] = max(1, grid[i+1][j] - grid[i][j])
			else:
				grid[i][j] = max(1, min(grid[i+1][j], grid[i][j+1])-grid[i][j])
	return grid[0][0]