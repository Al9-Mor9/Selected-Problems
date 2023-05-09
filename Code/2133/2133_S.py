n = int(input())

dp = [0]*(n+1)

if n % 2 != 0:          # 홀수일 경우에는 성립 되지 않음
    print(0)
else:                   # 짝수일 경우
    dp[2] = 3           # 두 번째는 3
    for i in range(4, n+1, 2):  # 4번째 부터 2씩 증가
        dp[i] = dp[i-2] * 3 + 2 # 값을 저장
        print(dp)
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2
            print(dp)
    
    print(dp[n])