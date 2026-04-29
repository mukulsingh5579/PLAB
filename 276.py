#Asynchronous Programming (asyncio)
import asyncio

async def fetch_data():
    print("Start fetching...")
    await asyncio.sleep(2) # Simulates a network delay
    print("Done fetching!")

async def main():
    # Runs the function asynchronously
    await asyncio.gather(fetch_data(), fetch_data())

asyncio.run(main())