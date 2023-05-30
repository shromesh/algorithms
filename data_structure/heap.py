class MyHeap:
    def __init__(self, size):
        self.dummy = 0
        self.size = size
        self.array = [self.dummy] * self.size
        self.last = 0 # データ数

    def add(self, value: int):
        if self.last != self.size:
            self.last += 1
            self.array[self.last] = value

            self.check_after_add(self.last)

    def remove(self):
        if self.last != 0:
            # 最大値を削除してreturn
            removed = self.array[1]

            # 1番右の葉を根ノードに移動。形は保った。
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.dummy

            self.last -= 1

            self.check_after_remove(1)
            return removed

    def check_after_add(self, i) -> None:
        if i==1:
            return
        
        # ノードiより親ノードが小さければスワップし再帰
        me = self.array[i]
        parent = self.array[i//2]
        if me > parent:
            self.array[i], self.array[i//2] = parent, me
            self.check_after_add(i//2)


    def check_after_remove(self, i):
        if 2*i > self.last:
            return

        # 根ノードから葉ノードまで順にたどり、
        # 子ノードのうち大きいほうとスワップしていく
        me = self.array[i]
        child0, child1 = self.array[2*i], self.array[2*i+1]
        if child0 >= child1:
            idx = 2*i
            maxch = child0
        else: 
            idx = 2*i+1
            maxch = child1

        if maxch > me:
            self.array[i], self.array[idx] = maxch, me
            self.check_after_remove(idx)


if __name__ == '__main__':
    heap_size = 10
    q = 3

    h = MyHeap(heap_size)
    h.add(q)
    h.remove()

