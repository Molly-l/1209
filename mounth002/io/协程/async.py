import asyncio

async def fun1():
    print("Start1")
    # 遇到阻塞跳出
    await asyncio.sleep(3)
    print("end1")

async def fun2():
    print("Start2")
    # 遇到阻塞跳出
    await asyncio.sleep(2)
    print("end2")

cor1 = fun1()
cor2 = fun2()

tasks = [asyncio.ensure_future(cor1),
         asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))