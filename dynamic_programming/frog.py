
# カエル飛び問題

def c(i, j, footholds):
    # 足場iから足場jに移動するコスト
    return abs(footholds[i] - footholds[j])


def main(N, footholds):
    # dpテーブル。足場1からNを0からN-1として。
    dp = [0] * N
    dp[1] = c(0, 1, footholds)

    for i in range(2, N):
        # i-1から来る場合とi-2から来る場合の、コストの小さい方を選ぶ
        dp[i] = min(dp[i-1] + c(i, i-1, footholds), dp[i-2] + c(i, i-2, footholds))

    return dp[-1] # 求めたいものはdpテーブルの端


if __name__ == '__main__':
    N = 4
    footholds = [10, 30, 40, 20]
    print(main(N, footholds))
    