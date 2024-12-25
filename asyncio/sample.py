import asyncio
import random


async def test1():
    print("test1 start")
    t = random.randint(1, 5)
    await asyncio.sleep(t)
    print("test1 end")
    return t


async def test2():
    print("test2 start")
    await asyncio.sleep(2)
    print("test2 end")
    return 2


async def main():
    print("main start")
    task = asyncio.gather(test1(), test2())
    result = await task

    for i, t in enumerate(result):
        print(f"test{i+1} finished in {t} seconds")


if __name__ == "__main__":
    asyncio.run(main())
