import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# sys.setrecursionlimit(100000)
# n, m = map(int, input().split())
# adj = [list(map(int,input().split()))[1:] for _ in range(n)]
# match= [False] * (m + 1)
# result=0

# def dfs(cur):
#     for job in adj[cur]:      # cur 에서 할 수 있는 job
#        if not is_done[job]:    # 만약 job이 아직 안되었다면, 
#           is_done[job] = True   # 처리하고, 담당이없거나, 담당을 밀어낼 수 있다면 내꺼.
#           if not match[job] or dfs(match[job]):
#             match[job] = cur
#             return True    
#     # cur에서 할 수 있는 job이 없고,
#     # job이 있는데 다 되어 있고,
#     # job을 이미 했거나 그 일을 한 놈이 다른 일을 찾지 못한다면,
#     return False

# for i in range(n):
#    is_done = [False] * (m + 1) # 밀어내야 하기 때문에 일단 일은 안되어있다고 하자.
#    if dfs(i): result += 1

# print(result)



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
