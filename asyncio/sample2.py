import asyncio

## asyncio.create_task()だと、taskを作成した時点で各処理が開始される


async def coro(n):
    print("coro start")
    await asyncio.sleep(n)
    print("coro end")


# 6秒かかる
# async def main():
#     print("main start")
#     await coro(1)
#     await coro(2)
#     await coro(3)
#     print("main end")


# 3秒かかる
async def main():
    print("main start")
    task1 = asyncio.create_task(coro(1))
    task2 = asyncio.create_task(coro(2))
    task3 = asyncio.create_task(coro(3))
    await task1
    await task2
    await task3
    print("main end")


if __name__ == "__main__":
    asyncio.run(main())
