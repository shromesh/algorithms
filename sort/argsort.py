def argsort(a, reverse=False):
    if reverse:
        key = lambda i: -a[i]
    else:
        key = lambda i: a[i]

    return sorted(list(range(len(a))), key=key)

if __name__ == '__main__':
    a = [1, 3, 5, 2, 4, 6]
    print(argsort(a, reverse=True))
