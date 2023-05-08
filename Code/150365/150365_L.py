import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# d, l, r, u 순서가 알파벳순. 
# n, m 격자
# x, y에서 r, c로
# k 번 이동. 

# 2 ≤ n, m ≤ 50
# 1 ≤ k ≤ 2,500 

# 도착 후 남은 이동가능 횟수가 짝수인지 확인해야 한다.
# 생각해보니 그럴 필요도 없네....


# e . . . .    dddd lrlr uuuu
# . . . . .
# . . e . .
# . . . . .
# . . . . .


from collections import deque

dr = [[1, 0], [0, -1], [0, 1], [-1, 0]]
dr_a = ['d', 'l', 'r', 'u']
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
 
    q = deque()
    q.append([x, y, k, ""])
    cnt = 0
    while q:
        x, y, cnt, log = q.popleft()

        if x == r and y == c:
            if cnt % 2:     return answer
            elif cnt == 0:  return log
        
        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 1 <= nx <= n and 1 <= ny <= m and cnt >= abs(nx - r) + abs(ny - c):
                q.append([nx, ny, cnt - 1, log + dr_a[i]])
                break

    return answer



# d, l, r, u 순서가 알파벳순. 

#print(solution(6, 6, 2, 6, 6, 5, 11))


# print(solution(5, 5, 3, 3, 3, 3, 8))


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))

