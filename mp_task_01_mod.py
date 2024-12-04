import aiohttp
import asyncio
import time
import requests

# список url для АТ-01
urls = ['https://www.example.com'] * 50

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def asyncio_run():
    start_time = time.perf_counter()
    asyncio.run(fetch_all(urls))
    end_time = time.perf_counter()
    print(f'asyncio time: {end_time - start_time:0.2f} \n')

if __name__ == '__main__':
    asyncio_run()
