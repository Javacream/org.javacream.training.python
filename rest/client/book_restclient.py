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


        url = 'http://h2908727.stratoserver.net:8080/api/books/ISBN1'
        async with session.get(url) as resp:
            books_json_string = await resp.text()
            book_dict = json.loads(books_json_string)
            print(book_dict['title'])

        url = 'http://h2908727.stratoserver.net:8080/api/books/Python'
        async with session.post(url) as resp:
            isbn = await resp.text()
            print(isbn)
            #async with session.delete('http://h2908727.stratoserver.net:8080/api/books/' + isbn) as resp:
            #    pass

#Windows Workaround
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
