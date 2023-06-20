# https://atcoder.jp/contests/dp/tasks/dp_m

# なんかちがう


def main(N, K, a):

    # init
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    # 0番目のitemを入れるときと入れないとき
    for i in range(1, N+1):
        dp[i][0] = 1

    for i in range(1, N+1): # ⼦供のループ
        # 累積和の準備
        prefix_sum = [0] * (K+1)
        for k in range(K+1):
            if k > 0:
                prefix_sum[k] = dp[i-1][k] + prefix_sum[k-1]
            else:
                prefix_sum[k] = dp[i-1][k]

        print(prefix_sum)
        

        for j in range(1, K+1): # 飴の数のループ
            if j - a[i-1] - 1 >= 0:
                dp[i][j] = prefix_sum[j] - prefix_sum[j-a[i-1]-1]
            else:
                dp[i][j] = prefix_sum[j]

        print(dp)


    return dp[-1][-1]


if __name__ == '__main__':
    N, K = 3, 3 # N: ⼦供の数、K: 飴の総数
    a = [1, 2, 2]
    res = main(N, K, a)

    print(res)
