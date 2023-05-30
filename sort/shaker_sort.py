def shakersort(seq):
    scan_count = 0
    # ソート済みの左端，右端を保持
    right = len(seq) - 1
    left = 0
    # 最後にスワップが起きた場所を格納する変数
    swapped = 0

    while left < right:
        scan_count += 1
        
        for i in range(left, right): # 先頭からチェック
            if seq[i+1] < seq[i]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = i
        # 最後のスワップの場所でrightを更新
        right = swapped

        for i in range(right, left, -1): #次は後ろからチェック
            if seq[i] < seq[i-1]:
                    seq[i], seq[i-1] = seq[i-1], seq[i]
                    swapped = i
        # 最後のスワップの場所でleftを更新
        left = swapped

    return scan_count, seq


if __name__ == '__main__':
    l = [1, 3, 5, 2, 4, 6]
    # c: スキャン回数, res: ソート済みの配列
    c, res = shakersort(l)
    print(res)
