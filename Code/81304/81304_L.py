import sys
sys.stdin = open("input.txt", "r")

# 제한 사항
# 2 <= n <= 1,000
# 1 <= roads <= 3000
# traps <= 10
sys.setrecursionlimit(int(1e6))

answer = 0
def solution(n, start, end, roads, traps):
    adj_list = [{} for _ in range(n + 1)]
    trap = [0] * (n + 1)
    for i in traps: trap[i] = 1
    visit = [0] * (n + 1)

    for a, b, v in roads:
        if b not in adj_list[a]:
            adj_list[a][b] = v
        else:
            adj_list[a][b] = min(adj_list[a][b], v)
    
    for node in range(n + 1):
        for key in adj_list[node].keys():
            if node not in adj_list[key]:
                adj_list[key][node] = -adj_list[node][key]

    global answer
    answer = 3e6

    def dfs(cur, val):
        global answer
        if cur == end:
            answer = min(answer, val)
            return
        if val > answer: return 

        if trap[cur]:
            for key in adj_list[cur].keys():
                if adj_list[key][cur] > 0:
                    adj_list[cur][key], adj_list[key][cur] = adj_list[key][cur], adj_list[cur][key]
                else:
                    adj_list[cur][key] *= -1
                    adj_list[key][cur] *= -1
                    
        for next, v in adj_list[cur].items():
            if v > 0 and visit[next] < 2:
                visit[next] += 1
                dfs(next, val + v)
                visit[next] -= 1
        
        if trap[cur]:
            for key in adj_list[cur].keys():
                if adj_list[key][cur] > 0:
                    adj_list[cur][key], adj_list[key][cur] = adj_list[key][cur], adj_list[cur][key]
                else:
                    adj_list[cur][key] *= -1
                    adj_list[key][cur] *= -1
    
    dfs(start, 0)
    return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))    # 5
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])) # 4

    