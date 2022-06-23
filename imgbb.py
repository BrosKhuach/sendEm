from imgbb.client import Client
import os
import aiohttp
import asyncio
key = os.getenv('0ef6a485fd2c7fbb9cd6dd6fab7f1313')
session = aiohttp.ClientSession()
myclient = Client(key,session)

async def upload(image,name):
    response = await myclient.post(image,name)
    url = response['data']['url']
    print(f'Uploaded image URL: {url}')

if __name__=='__main__':
    asyncio.run(upload('Screenshot-2022-06-18-12-07-09-75-948cd9899890cbd5c2798760b2b95377.jpg','Cool picture'))