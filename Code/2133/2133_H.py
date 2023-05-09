import sys
# sys.stdin = open('input.txt')
#####

n = int(input())
if n % 2:
    print(0)
    exit(0)
arr = [0] * 31
arr[2] = 3
'''
홀수일 때는 0
짝수일 때는 [n-2] * 3 + 2 * { n-4까지 합 } + 2
'''

for i in range(4, 31, 2):
    arr[i] += arr[i-2] * 3
    for j in range(0, i-2, 2):
        arr[i] += arr[j] * 2
    arr[i] += 2

print(arr[n])
