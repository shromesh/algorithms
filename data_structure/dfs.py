import sys
import resource
# from collections import deque

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


# 頂点Sから頂点Tに到達できるかどうかを判定する
def dfs(S, T, edges_list, seen):
    seen[S] = True
    # SからTに到達できるかどうか
    if S == T:
        return True

    # Sから行ける頂点を全て探索する
    for next_v in edges_list[S]:
        # すでに探索済みの頂点は探索しない
        if seen[next_v]:
            continue

        # 再帰的に探索
        if dfs(next_v, T, edges_list, seen):
            return True

    return False


if __name__ == '__main__':
    N, M, S, T = map(int, input().split())
    S -= 1
    T -= 1
    # 上のような入力から、まずはedges_listを作る
    edges_list = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges_list[a-1].append(b-1)
        edges_list[b-1].append(a-1)

    seen = [False] * N
    res = dfs(S, T, edges_list, seen)
    
    print('Yes' if res else 'No')
