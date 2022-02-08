import aiohttp
import asyncio
import json

async def main():

    async with aiohttp.ClientSession() as session:

        url = 'http://h2908727.stratoserver.net:8080/api/books'
        async with session.get(url) as resp:
            books_json_string = await resp.text()
            books_list = json.loads(books_json_string)
            book_dict = books_list[0]
            print(book_dict['title'])


#Windows Workaround
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())