import asyncio
import aiohttp

class Book:
    def __init__ (self, isbn, title, price, available):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.available = available

class BooksService:
        endpoint = 'http://h2908727.stratoserver.net:8080/api/books'
        async def find_all(self):
            async with aiohttp.ClientSession() as session:
                async with session.get(BooksService.endpoint) as resp:
                    books_list = await resp.json()
                    return list(map(lambda book_dict: Book(**book_dict), books_list))
        async def find_by_isbn(self, isbn):
            async with aiohttp.ClientSession() as session:
                async with session.get(BooksService.endpoint + "/" + isbn) as resp:
                    book = await resp.json()
                    return Book(**book)
        async def delete_by_isbn(self, isbn):
            async with aiohttp.ClientSession() as session:
                async with session.delete(BooksService.endpoint + "/" + isbn) as resp:
                    pass
        async def create(self, title):
            async with aiohttp.ClientSession() as session:
                async with session.post(BooksService.endpoint + "/" + title) as resp:
                    isbn = await resp.text()
                    return isbn
