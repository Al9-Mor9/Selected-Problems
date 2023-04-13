# import sys
# sys.stdin = open("input.txt", "r")

# 1. 이모티콘 플러스 서비스 가입자 최대
# 2. 이모티콘 판매액 최대.
# n 명의 사용자, 이모티콘 m개를 할인 판매
# 할인율은 10, 20, 30, 40 %

# 사용자는 이모티콘을 사거나, 서비스 가입함
# 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매함
# 근데 사다가 구매 비용합이 일정 가격 이상이 되면, 이모티콘 서비스 가입함.

# 1 <= n <= 100
# 1 <= m <= 7
# 가격은 100 <= p <= 1,000,000 근데 100단위라

# P1 ---------------------------------------------------------------
# 흠... 4의 7승이면 얼마지 
# 2의 14승... 
# 10   11   12   13   14
# 1024 2048 4096 8192 16384

# 16,384,000 이거 해도 되나..? 파이썬은 초당 20,000,000 이니까...

# P2 ---------------------------------------------------------------
# 시간 복잡도를 줄일 수 있는가?
# ...그냥 돌려보자..

sale = [0.9, 0.8, 0.7, 0.6]
def solution(users, emoticons):
    ans = [0, 0]
    n, m = len(users), len(emoticons)
    sales = [0] * m
    user = [[] for _ in range(4)]
    for s, b in users: user[int((s-1)/10)].append(b)

    def comb(idx):
        if idx == m: cal(); return
        for i in range(4): sales[idx] = i; comb(idx + 1)

    def cal():
        tmp = [0] * 4
        tmp_c, tmp_v = 0, 0
        for i in range(m):
            cur = emoticons[i] * sale[sales[i]]
            for j in range(sales[i] + 1): tmp[j] += cur
        for i in range(4):
            for budget in user[i]:
                if budget > tmp[i]:
                    tmp_v += tmp[i]
                else:
                    tmp_c += 1
        if ans[0] * 1e6 + ans[1] / 1e3 < tmp_c * 1e6 + tmp_v / 1e3: ans[0], ans[1] = tmp_c, int(tmp_v)
    comb(0)
    return ans



print(solution([[40, 10000], [25, 10000]], [7000, 9000])) #[1, 5400]
print(solution([[40, 2900], [23, 10000], [11, 5200],
                [5, 5900], [40, 3100], [27, 9200],
                [32, 6900]], [1300, 1500, 1600, 4900])) #[4, 13860]

