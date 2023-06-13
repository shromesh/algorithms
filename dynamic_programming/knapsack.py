
# 重さの値が価値に比べてとても大きいので、重さの上限を列としてとる。
# dp[i][sum_v] = min_w として解く。
# 価値の合計がsum_vのとき、min_wはそれを実現する重さの最小値。


def main(N, W, w_list, v_list):
    V = sum(v_list) # 価値の合計としてありうる最大値
    inf = 10**12 # 十分大きな値

    # init
    dp = [[inf for _ in range(V+1)] for _ in range(N)]
    # 0番目のitemを入れるときと入れないとき
    dp[0][0] = 0
    dp[0][v_list[0]] = w_list[0]

    for i in range(1, N):
        for j in range(0, V+1):
            # indexが負にならないなら
            if j-v_list[i] >= 0:
                # i番目のitemを加えるか加えないかの最小値
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v_list[i]] + w_list[i])
            else:
                dp[i][j] = dp[i-1][j]

    # dpテーブルの最終行の中で、重さがW以下で価値が最大のものを探す
    res = 0
    for i in range(V+1):
        if dp[-1][i] <= W:
            res = i

    return res


if __name__ == '__main__':
    N, W = 4, 10 # Wは重さの上限
    w_list = [3, 3, 3, 2]
    v_list = [1, 2, 4, 1]
    res = main(N, W, w_list, v_list)

    print(res)