import aiohttp
import asyncio
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        content1, content2 = await asyncio.gather(
            fetch_url(session, 'https://www.geeksforgeeks.org/'),
            fetch_url(session, 'https://news.ycombinator.com/')
        )
        print("Elapsed time:", time.time() - start_time)

# Run the asynchronous main function
asyncio.run(main())
