import asyncio
import aiohttp

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    # Define a list of URLs to request
    urls = ["https://docs.python.org/3/library/asyncio.html", 
            "https://docs.aiohttp.org/",
            "https://github.com/",
            "https://google.com/"]

    # Make a list of GET request coroutines
    tasks = [asyncio.create_task(get_content(url)) for url in urls]

    # Unpack each coroutine to gather contents from each URL concurrently
    responses = await asyncio.gather(*tasks)

    # Print the response for each request
    for url, response in zip(urls, responses):
        print(f"Response from {url}: {response}...")

if __name__ == "__main__":
    asyncio.run(main())