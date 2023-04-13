import sys, math
sys.stdin = open('input.txt', 'r')
#####
import math

n = int(input())
arr = list(map(int, input().split()))

pref = [0] * (n + 1)    # 0 ~ K 까지의 gcd를 저장하는 리스트
suff = [0] * (n + 1)    # K ~ (n - 1) 까지의 gcd를 저장하는 리스트

pref[0] = arr[0]
for i in range(1, n):
    pref[i] = math.gcd(pref[i-1], arr[i])

suff[n-1] = arr[n-1]
for i in range(n - 2, -1, -1):
    suff[i] = math.gcd(suff[i + 1], arr[i])

# print(pref, suff)   # [8, 4, 4, 4, 4, 0] [4, 12, 12, 12, 48, 0]

ans = []

for i in range(n):
    # left = [0, i-1]까지 gcd
    left = pref[i-1]
    # right = [i+1, n-1]까지 gcd
    right = suff[i+1]
    # res = i번째 수(K)를 제외한 나머지의 최종 gcd
    res = math.gcd(left, right)

    # 최종 gcd가 k의 약수일 때
    if arr[i] % res == 0:
        continue
    else:
        ans.append([res, arr[i]])
ans.sort()
if ans:
    print(*ans[-1])
else:
    print(-1)

'''   
질문 : 그냥 하나 빼고 다 gcd 구하면 안되나?
    - 그럼 시간초과남
        그러면 누적합은 갑자기 왜나옴?
    - gcd한 결과값을 저장해두려고
        - 앞에서 가는거랑 뒤에서 오는거랑
        그걸 어따씀
    - 저장된 값이 있으니까 K값 바로 앞까지랑 뒤에서 온 바로 다음 값들의 gcd를 구하면
    - K를 뺀 나머지의 gcd가 한번에 나옴
'''