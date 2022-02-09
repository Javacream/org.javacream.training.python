import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    future = say_after(2, 'hello')
    print(dir(future))
    print(future)
    await say_after(1, 'world')
    await future

    print(f"finished at {time.strftime('%X')}")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#asyncio.run(main())
