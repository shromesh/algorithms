def main(A, key):
    left = 0
    right = len(A) - 1

    while left < right:
        pivot = (left + right) // 2

        if key < A[pivot]: # これを満たす最小のものをさがす。
            right = pivot
        else:
            left = pivot + 1
    
    return A[left]
    

# sort済みの配列内で、keyを超える最小の要素を探す。
if __name__ == '__main__':
    A = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    key = 2
    print(main(A, key))

