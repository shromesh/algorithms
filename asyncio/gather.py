import asyncio
import random

## asyncio.gather()
## test1を実行しawaitに到達するとtest2を実行し、その後、先にawaitが終わった方から結果を取得する。
## タスクを同時に作成して実行し、完了を待つための新しい代替手段は ですasyncio.TaskGroup。TaskGroupは、サブタスクのネストをスケジュールするためのgather よりも強力な安全性保証を提供します。タスク (またはサブタスク、タスクによってスケジュールされたタスク) で例外が発生した場合、TaskGroup は残りのスケジュールされたタスクをキャンセルしますが、 gather はキャンセルしません。


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
