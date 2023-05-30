# copyを渡したりせずにseqを直接編集する
def qsort(seq, left, right):

    # 要素数が1か2なら再帰の終端
    if right == left:
        return
    elif right == left + 1:
        seq[left], seq[right] = min(seq[left: right+1]), max(seq[left: right+1])
        return 

    pivot = seq[right]
    j = left # スワップ先とするカーソル

    for i in range(left, right): # i=right-1で止まる
        # pivot以下ならスワップする
        if seq[i] <= pivot:
            seq[i], seq[j] = seq[j], seq[i]
            j += 1

    # pivotをjの位置へ移動
    seq[right], seq[j] = seq[j], seq[right]

    # 再帰
    if j == left:
        qsort(seq, left, j)
        qsort(seq, j+1, right)
    else:
        qsort(seq, left, j-1)
        qsort(seq, j, right)

    return seq


if __name__ == '__main__':
    l = [1, 3, 5, 2, 4, 6]
    res = qsort(l, 0, len(l)-1)
    print(res)
