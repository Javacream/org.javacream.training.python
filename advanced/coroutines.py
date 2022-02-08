import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    future = say_after(1, 'hello')
    print(dir(future))
    print(future)
    await future
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())
