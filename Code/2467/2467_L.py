import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

p1 = 0
p2 = n - 1
diff = 2e9 + 1
left = 0
right = n - 1

while p1 < p2:
    tmp = arr[p1] + arr[p2]

    if diff > abs(tmp):
        diff = abs(tmp)
        left = p1
        right = p2

    if tmp > 0 :
        p2 -= 1
    elif tmp < 0 :
        p1 += 1
    else:
        break


print(arr[left], arr[right])

