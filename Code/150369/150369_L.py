import sys
sys.stdin = open("input.txt", "r")

def solution(cap, n, deliveries, pickups):
    deli = []
    pick = []
    p = n - 1

    while p > -1:
        if deliveries[p] == 0:
            p -= 1
        else:
            deli.append(p+1)
            tmp_d = 0
            while True:
                tmp_d += deliveries[p]
                if tmp_d == cap:
                    p-=1
                    break
                elif tmp_d > cap:
                    over = tmp_d - cap
                    deliveries[p] = over
                    break
                p-=1
    p = n - 1
    while p > -1:
        if pickups[p] == 0:
            p -= 1
        else:
            pick.append(p+1)
            tmp_p = 0
            while True:
                tmp_p += pickups[p]
                if tmp_p == cap:
                    p-=1
                    break
                elif tmp_p > cap:
                    over = tmp_p - cap
                    pickups[p] = over
                    break
                p-=1
    
    ans = 0
    if len(deli) >= len(pick):
        for i in range(len(pick)):
            ans += 2 * max(pick[i], deli[i])
        for i in range(len(pick), len(deli)):
            ans += 2 * deli[i]
    else:
        for i in range(len(deli)):
            ans += 2 * max(pick[i], deli[i])
        for i in range(len(deli), len(pick)):
            ans += 2 * pick[i]

    
    return ans


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30
