t = int(input())
while t:
    n = int(input())
    w = int(input())
    v = [int(i) for i in input().split()]
    wt = [int(i) for i in input().split()]

    # dp = [[0]*(w+1)]*(n+1)
    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    # for i in range(0, n+1):
    #     for j in range(0, w+1):
    #         print(dp[i][j], end=" ")
    #     print()

    # print()

    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1] <= j:
                dp[i][j] = max(v[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]


    for i in range(0, n+1):
        for j in range(0, w+1):
            print(dp[i][j], end=" ")
        print()
    print(dp[n][w])
    t -= 1

# 1
# 5
# 7
# 1 2 5 4 6
# 3 2 8 5 1
# 0 0 0 0 0 0 0 0
# 0 0 0 1 1 1 1 1
# 0 0 2 2 2 3 3 3
# 0 0 2 2 2 3 3 3
# 0 0 2 2 2 4 4 6
# 0 6 6 8 8 8 10 10
# 10
# 58
# 41
# 57 95 13 29 1 99 34 77 61 23 24 70 73 88 33 61 43 5 41 63 8 67 20 72 98 59 46 58 64 94 97 70 46 81 42 7 1 52 20 54 81 3 73 78 81 11 41 45 18 94 24 82 9 19 59 48 2 72
# 83 84 85 76 13 87 2 23 33 82 79 100 88 85 91 78 83 44 4 50 11 68 90 88 73 83 46 16 7 35 76 31 40 49 65 2 18 47 55 38 75 58 86 77 96 94 82 92 10 86 54 49 65 44 77 22 81 52