"""Завдання: додати відсутній код (завершити імплементацию).

    Перевикористати класи з попереднього завдання (Book, Library).
    Додати метод save до класу Library який буде викликатиса при
    додаванні кожної нової книги до бібліотеки та записувати
    усі книги з пам'яті до файлу (файл відкривати на запис - w
    - для того щоб попередня інфа обнулялася кожного разу).
    Додати нову книгу до бібліотеки з ендпоінту http://localhost:5000/library/books/add/
    та переконатися що файл було створено.
    * Додати функцію upload_books_file - який буде загружати книжки з
    файлу LIBRARY_STORE_FILE та використати її замість upload_books
    таким чином кинжки можно буде накопичувати між сенсами роботи веб серверу.

Підказка: знадобиться postman чи подібна програма для передачі payload'у
        реквесту (тип якого буде POST) на виклик ендпоінту /library/books/add/

        payload для додавння нової книги виглядає як

        {
          "title": "The Lion, the Witch and the Wardrobe",
          "author": "C. S. Lewis",
          "year": 1950
        }

        у постмані це вкладка Body, під-опція raw, та тип JSON.
"""
import uuid  # генерує унікальне значення, не isbn але ж легше використати
import json
from typing import List, Any

from flask import Flask, request


class Book:

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

class Library:

    book_list = []

    def add(self, Book):
        self.book_list.append(Book)

    def search(self, title):
        for i in range(len(self.book_list)):
            if self.book_list[i].title == title:
                return i
        return -1

    def lend(self, title):
        for i in self.book_list:
            if i.title == title:
                return i

    def remove(self, title):
        for i in self.book_list:
            if i.title == title:
                self.book_list.remove(i)
                break


    def save(self, file):
        with open(file, encoding='utf-8', mode='w+') as file:
            for b in self.book_list:
                file.write(f"{b.isbn} | {b.title} | {b.author} | {str(b.year)} \n")


class LibraryIterator:

    def __init__(self, data):
        self.i = 0
        self.data = data.copy()

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        self.i += 1
        return self.data[self.i-1]


BOOKS_TO_LOAD = [  # https://en.wikipedia.org/wiki/List_of_best-selling_books
    (uuid.uuid4(), "A Tale of Two Cities", "Charles Dickens", 1859),
    (uuid.uuid4(), "The Little Prince", "Antoine de Saint-Exupéry", 1943),
    (uuid.uuid4(), "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997),
    (uuid.uuid4(), "And Then There Were None", "Agatha Christie", 1939),
    (uuid.uuid4(), "Dream of the Red Chamber", "Cao Xueqin", 1791),
    (uuid.uuid4(), "The Hobbit", "J. R. R. Tolkien", 1937),
]


def upload_books_file(library):
    with open(LIBRARY_STORE_FILE, encoding='utf-8', mode="r") as file:
        for l in file:
            isbn, title, author, year = l.split(' | ')
            library.add(Book(isbn, title, author, int(year)))


def upload_books(library):
    for isbn, title, author, year in BOOKS_TO_LOAD:
        library.add(Book(isbn, title, author, year))


app = Flask(__name__)
LIBRARY_STORE_FILE = "lib.txt"
one_citys_library = Library()


@app.route("/library/books/")
def library_books():
    """Returns all books in a library"""
    result = [
        {"isbn": b.isbn, "title": b.title, "author": b.author, "year": b.year}
        for b in LibraryIterator(one_citys_library.book_list)
    ]
    return dict(result=result)


@app.route("/library/books/add/", methods=["POST", ])
def library_books_add():
    try:
        payload = json.loads(request.data)
    except Exception as e:
        return dict(error=str(e)), 406

    try:
        b = Book(
            isbn=uuid.uuid4(),
            title=payload["title"],
            author=payload["author"],
            year=payload["year"]
        )
    except Exception as e:
        return dict(error=str(e)), 406

    one_citys_library.add(b)
    one_citys_library.save(LIBRARY_STORE_FILE)
    return dict(result="ok"), 200


if __name__ == "__main__":
    # upload_books(one_citys_library)
    upload_books_file(one_citys_library)
    app.run(debug=True)