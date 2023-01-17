import asyncio

async def seq():
    print("step1")
    await asyncio.sleep(1)
    print("step2")
    return "Hugo"

async def caller():
    await asyncio.gather(seq(), seq(), seq());
asyncio.run(caller())