class MyHash:
    def __init__(self, size: int):
        self.size = size
        self.array = [-1] * self.size

    def add(self, v: int):
        s = self.size
        i = v % s # hash
        if self.array[i] == -1:
            self.array[i] = v

        # すでに値が入っている場合は、入れても良い場所を線形探索
        else:
            while True:
                i = (i+1) % s # sizeを超えたら先頭に戻る
                if self.array[i] == -1:
                    self.array[i] = v
                    break

    def search(self, v: int):
        s = self.size
        i = v % s # hash
        if self.array[i] == v:
            print('found')
        elif self.array[i] == -1:
            print('not found')
        
        # vでも-1でもない場合は線形探索
        else:
            for _ in range(s):
                i = (i+1) % s # sizeを超えたら先頭に戻る
                if self.array[i] == v:
                    print('found')
                    break
            else: # 1周してもbreakしなければ
                print('not found')


if __name__ == '__main__':
    size = 10**6
    h = MyHash(25*size) # 25倍くらいがちょうどよい

    v = 10
    h.add(v)
    h.search(v)

