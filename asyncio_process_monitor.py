import asyncio
import random


async def task(name, duration):
    """Simulates an asynchronous task."""
    print(f"{name} started, will take {duration}s.")
    await asyncio.sleep(duration)
    print(f"{name} completed.")
    return f"{name} finished in {duration}s."


async def monitor(tasks, interval=1):
    """Periodically reports the status of running tasks."""
    while not all(task.done() for task in tasks):
        print(f"Monitor: {sum(not task.done() for task in tasks)} tasks still running...")
        await asyncio.sleep(interval)
    print("Monitor: All tasks completed.")


async def main():
    # Create tasks
    tasks = [asyncio.create_task(task(f"Task-{i + 1}", random.randint(2, 5))) for i in range(5)]

    # Run tasks and monitor concurrently
    task_group = asyncio.gather(*tasks)
    await asyncio.gather(task_group, monitor(tasks))

    # Process results
    print("\nResults:")
    for result in await task_group:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
