import pprint


# 部分和問題

def main(N, S, numbers):
    # [0...S] を 0...N のぶん。行は与えられた配列の要素（dp[0]はnone, dp[1]はnumbers[0]）、列は和をjにできることに対応する
    dp = [[False for _ in range(S+1)] for _ in range(N+1)]
    # dp = [[False]*(S+1)] * (N+1) # この書き方だと第0行の参照渡しになってしまう

    for i in range(N+1):
        # 0個の数字で和を0にできる。
        dp[i][0] = True

    for i in range(0, N):
        for j in range(1, S+1):
            # indexが負にならない
            if j-numbers[i] >= 0:
                # dp[i][j]がTrueならなにも加えずにS。または、
                # dp[i][j-numbers[i]]がTrueならnumbers[i]を加えるとS
                dp[i+1][j] = dp[i][j] or dp[i][j-numbers[i]]
            else: 
                dp[i+1][j] = dp[i][j]

    return dp[-1][-1]




if __name__ == '__main__':
    N, S = 4, 10
    numbers = [3, 3, 3, 2]
    res = main(N, S, numbers)

    pprint.pprint(res)
