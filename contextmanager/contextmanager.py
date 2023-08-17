from contextlib import contextmanager, asynccontextmanager


# @contextmanager
@asynccontextmanager
async def test1():
    print("test1 start")
    try: 
        yield 1
    finally:
        print("test1 end")

@asynccontextmanager
async def test2():
    print("test2 start")
    try: 
        yield 2
    finally:
        print("test2 end")

async def main():
    print("main start")

    # withは__enter__を、async withは__aenter__を呼び出す。
    async with test1() as value1:
        async with test2() as value2:
            print(value2)
        print(value1)
        print(value2)    
    
    print("main end")

# from Jupyter
# if __name__ == '__main__':
#     await main()