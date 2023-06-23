from collections import deque, defaultdict

def roundrobin(*iterables):
    # roundrobin('ABC', 'D', 'EF') --> A D E B F C
    iterators = deque(map(iter, iterables)) # e.g. iter('ABC')
    while iterators:
        try:
            while True:
                yield next(iterators[0]) # next('ABC') -> 'A'
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()

# collenctions.Counterと同じ
def count_str(s):
    d = defaultdict(lambda: 0) 
    for k in s:
        d[k] += 1
    return d
