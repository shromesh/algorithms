# この方法は最適ではない。。


from pprint import pprint
from math import factorial


def main(N, S, A, B):
    # iはA[i]を考えることに対応、jは袋の個数に対応
    # 3次元の空のリストを作る
    # dp = [[[] for _ in range(S+1)] for _ in range(N)]
    dp = [[[] for _ in range(S+1)] for _ in range(2)]

    # init (i=0)
    dp[0][0].append(0)
    dp[0][B[0]].append(A[0])

    # exe (i>=1)
    for ix in range(1, N):
        i = ix % 2
        # これから入れる配列のリセット
        dp[i] = [[] for _ in range(S+1)]

        for j in range(S+1):
            # 入れない場合
            for k in dp[i-1][j]:
                dp[i][j].append(k)
            # 入れる場合
            if j-B[ix] >= 0:
                for k in dp[i-1][j-B[ix]]:
                    dp[i][j].append(k+A[ix])


    # calc answer
    res = 0
    ans_dp = dp[(N-1) % 2] # dpのうち最後に編集された行

    # debug
    print(S)
    for k in ans_dp:
        print(len(k))


    for j in range(1, S+1): # j=0は袋が0なので除く
        for k in ans_dp[j]:
            if k % j == 0:
                res += 1
    return res

if __name__ == '__main__':
    N = 7*3
    A = [2, 5, 6, 5, 2, 1, 7]*3
    B = [0, 0, 1, 0, 0, 1, 1]*3
    S = sum(B)

    # init
    # for i, a in enumerate(A):
    #     A[i] = a % factorial(N)

    res = main(N, S, A, B)
    # print(res)
