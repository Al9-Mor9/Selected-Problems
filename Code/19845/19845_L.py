import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# -------------------------------------
# 1 ≤ N, Q ≤ 250,000
# 1 ≤ ai ≤ 10^9 (1 ≤ i ≤ N)
# a1 ≥ a2 ≥ … ≥ aN
# 1 ≤ xi ≤ 10^9, 1 ≤ yi ≤ n (1 ≤ i ≤ Q)
# -------------------------------------------
# 7, 7, 3, 2 라고하면,

# ㅁㅁ
# ㅁㅁㅁ
# ㅁㅁㅁㅁㅁㅁㅁ
# ㅁㅁㅁㅁㅁㅁㅁ

# 4, 1 은 가로 4개 위에 1개 해서 5가 출력되어야함.

n, query = map(int, input().split())
nemmo_house = list(map(int, input().split()))

def binary_search(target):
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nemmo_house[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

for q in range(query):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    nemmo_in_y = max(0, nemmo_house[y]-x)
#    print("가로 줄의 개수 ", nemmo_in_y)

    idx = binary_search(x+1) 
#    print(x+1,  "보다 작은 위치", idx)

    nemmo_in_x = max(0, idx - y)

    ans = nemmo_in_y + nemmo_in_x
    print(ans - 1) if ans else print(0)  

