def mod_power(x, n): # 効率化のため、(x**2)**n//2で実装する
    if n == 0:
        return 1
    res = mod_power(x*x % M, n//2)
    if n%2:
        # 奇数ならもう一回かける
        res = (res * x) % M
    return res

def main():
    N = int(input())

    # S1からSiまでを文字列的に結合したもののmodMと桁数を保持する。
    modM_list = []
    digits_list = []

    # i = 0
    a, b = map(int, input().split())
    num = (a * mod_power(10, b%O)) % M
    modM_list.append(num)
    digits_list.append(b + 1) # 桁数はb+1

    for i in range(1, N):
        a, b = map(int, input().split())
        num = (a * mod_power(10, b%O)) % M
        digits = b + 1

        # 10, 20なら1020なので、20 + 10*100 mod Mを計算する。
        modM_list.append(( num + (modM_list[i-1] * mod_power(10, digits%O))%M ) % M)
        digits_list.append(digits + digits_list[i-1]) # 桁数はもちろん累積和

    # 先に作っておいた配列を使ってクエリを処理する
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())

        if l == 1:
            print(modM_list[r-1])
        else:
            # r-1番目とl-2番目の差を使う。(indexが1始まりであるため)
            digits_delta = digits_list[r-1] - digits_list[l-2]
            res = ( modM_list[r-1] - (modM_list[l-2] * mod_power(10, digits_delta%O))%M )% M
            print(res)


if __name__ == '__main__':
    # global variables
    M = 998244353
    O = M-1 # 10**O mod M == 1を満たす(fermatの小定理)
    main()