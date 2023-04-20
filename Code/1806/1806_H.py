import sys
sys.stdin = open('input.txt', 'r')
#####
n, s = map(int, input().split())
arr = list(map(int, input().split()))
l, h = 0, 1     # low, high 투 포인터

sm = [0] * n    # 누적 합 리스트 생성
sm[0] = arr[0]  # 초기값 설정
for i in range(1, n):
    sm[i] = sm[i-1] + arr[i]
sm = [0] + sm

# print(arr)      # [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
# print(sm)       # [0, 5, 6, 9, 14, 24, 31, 35, 44, 46, 54]

ans = []
while 0 <= l < n+1 and 0 <= h < n+1:
    tmp = sm[h] - sm[l]
    if tmp < s:
        h += 1
    else:
        ans.append(h-l)
        l += 1
if ans:
    print(min(ans))
else:
    print(0)
