# NとCi(1..i..N)が与えられる。
# 自身より手前に自身より大きいものが1個以下となるような並べ方の総数を求める。

import math

def main(N, C):
    M = 100003

    res = 1
    c_set = set(C)
    
    # 重複があるぶん
    # 2個以上ある要素の個数を求める
    dup_count = 0
    for c in c_set:
        a = C.count(c)
        if a >= 2:
            dup_count += a
    
    # 重複があるものにたいして
    res *= math.factorial(dup_count - 1) % M

    # 重複がないものにたいして
    res *= 2**(len(c_set)-1) % M

    return res


if __name__ == '__main__':
    # N = int(input())
    # C = list(map(int, input().split()))
    N = 20
    C = [1]*20

    res = main(N, C)
    print(res)


