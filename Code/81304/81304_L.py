import sys
sys.stdin = open("input.txt", "r")

# 제한 사항
# 2 <= n <= 1,000
# 1 <= roads <= 3000
# traps <= 10 

import heapq

INF = 4e6
def solution(n, start, end, roads, traps):
    dij = [[INF] * (1 << 10) for _ in range(n + 1)]
    trap_map = {v : i for i, v in enumerate(traps)}
    graph = [[] for _ in range(n + 1)]
    ans = INF

    for cur, next, cost in roads:
        graph[cur].append([next, cost, 0])
        graph[next].append([cur, cost, 1])
        
    hq = []
    heapq.heappush(hq, [0, start, 0])
    dij[start][0] = 0

    while hq:
        val, cur, state = heapq.heappop(hq)
        if cur == end:
            ans = min(ans, val)
            continue

        if val > dij[cur][state]: continue

        for next, cost, flag in graph[cur]:
            # cur와 next의 트랩이 on 되어있는지 확인, 방향까지 고려해서 가능 여부 반환
            cur_on = state & (1 << trap_map[cur]) > 0 if cur in traps else 0
            next_on = state & (1 << trap_map[next]) > 0 if next in traps else 0
            if (cur_on ^ next_on) != flag: continue

            # 상태 변환, 이동 거리 추가.
            next_state = state ^ (1 << trap_map[next]) if next in traps else state
            next_val = val + cost

            # [장소, 트랩의 상태] 있던 값보다 작을 때만 갱신
            if next_val >= dij[next][next_state]: continue
            dij[next][next_state] = next_val
            heapq.heappush(hq, [next_val, next, next_state])

    return ans


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))    # 5
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])) # 4

