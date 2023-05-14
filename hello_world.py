import asyncio

# Define an asynchronous function that prints some things, waits for some time, then prints some more things.
async def hello_world(task_num):
    print("Begin task #", task_num)
    print("Hello")
    print("Waiting...")
    await asyncio.sleep(2)
    print("World")
    print("This is asyncio!")

# Define an asynchronous function that creates two tasks that call the `hello_world()` coroutine and wait for them to complete.
async def main():
    task1 = asyncio.create_task(hello_world(task_num=1))
    task2 = asyncio.create_task(hello_world(task_num=2))
    await asyncio.gather(task1, task2)

# Run the `main()` function using `asyncio.run()`
if __name__ == "__main__":
    asyncio.run(main())