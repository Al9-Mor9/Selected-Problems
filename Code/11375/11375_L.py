import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, m = map(int, input().split())
adj = [0] + [list(map(int,input().split()))[1:] for _ in range(n)]
match = [0 for _ in range(m + 1)]    

def dfs(node):
    if visited[node] == 1: return False         # 노드별로 담당은 한 번만 바꾼다.

    visited[node] = 1 
    for job in adj[node]:                       # 노드가 처리할 수 있는 모든 일
        if not match[job] or dfs(match[job]):   # 그 일을 담당이 없거나 바꿀 수 있다면,
            match[job] = node                   # 현재 노드로 담당을 바꾼다.
            return True
    return False
    
for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)] 
    dfs(i)

print(m - match.count(0) + 1)
