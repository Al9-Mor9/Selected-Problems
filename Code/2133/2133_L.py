import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 월요일 12시... 매운 떡볶이 맛있겠다.

# 매우 전형적인 dp
# 부분 최적 구조를 직관적으로 발견할 수 있다.
# 다만 직사각형을 노가다하며 구하는게 매우 귀찮긴한데..


# 기본적으로 n-2에서 2x3칸을 채우는 방법은 dp[n-2] * 3 이다.
# 길이가 늘어남에 따라 생기는 고유한 블럭의 길이를 k 라고 했을 때, 
# dp[n-k] * 2 를 추가해 줘야한다. 
# 다행히 이놈들은 4부터 2개씩 생긴다.

n = int(input())
arr = [0 for _ in range(31)]
arr[0] = 1
arr[2] = 3

for i in range(4, 31, 2):
    arr[i] += arr[i-2] * 3
    for j in range(0, i - 3, 2):
        arr[i] += arr[j] * 2

print(arr)
print(arr[n])





