"""Завдання: деталізувати працівників бібліотеки, додавші нові класи.

    Взяти за основу завдання вже виконане assignment15_01.py (скопіювати в новий файл)
    Додайте атрибут level до класу Employee
    Додайте нові класи:
        Librarian - віднаслідувати від Employee, задати level='librarian' у конструкторі потомка
        SeniorLibrarian - віданслідувати від Librarian (level="senior_librerian")
        Cleaner - віднаслідувати від Employee (level="cleaner")
    Додати новий метод (у кожний з класів ієрархії наслідування - Employee, Librarian, etc)
      get_description який би повертав строку з поясненням про працівника:
           Employee - I'm an employee keep doing what needs to be done
           Librarian - I'm a librarian keep books in order, visitors glad
           SeniorLibrarian - I'm a senior level librarian, keep the papers in order
           Cleaner - I'm a cleaner, keeping premises shining
    Замінити об'екти Employee у прегенерованому списку на конкретні - 2 об'єкта Librarian, 1 SeniorLibrarian,
      1 Cleaner
    Модіфікувати get_details у класі Employee: додати новий ключ description у який виставити
      значення self.get_description()

Попередній вивод повинен змінитися (виводити конкретних працівників).
"""
import uuid


class Employee:

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        self.level = None


    def get_details(self):
        return {
            "name": self.name,
            "experience":self.experience,
            "description": self.get_description()
        }

    def get_description(self):
        return "I'm an employee keep doing what needs to be done"

class Librarian(Employee):

    def __init__(self, name, experience):
        super().__init__(name, experience)
        self.level = "librarian"


    def get_description(self):
        return "I'm a librarian keep books in order, visitors glad"


class SeniorLibrarian(Librarian):

    def __init__(self, name, experience):
        super().__init__(name, experience)
        self.level = "senior_librerian"


    def get_description(self):
        return "I'm a senior level librarian, keep the papers in order"


class Cleaner(Employee):

    def __init__(self, name, experience):
        super().__init__(name, experience)
        self.level = "cleaner"


    def get_description(self):
        return "I'm a cleaner, keeping premises shining"


class Book:

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


class Library:

    def __init__(self):
        self.book_list = []
        self.employees = []


    def register_employee(self, Employee):
        self.employees.append(Employee)


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




BOOKS_TO_LOAD = [  # https://en.wikipedia.org/wiki/List_of_best-selling_books
    (uuid.uuid4(), "A Tale of Two Cities", "Charles Dickens", 1859),
    (uuid.uuid4(), "The Little Prince", "Antoine de Saint-Exupéry", 1943),
    (uuid.uuid4(), "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997),
    (uuid.uuid4(), "And Then There Were None", "Agatha Christie", 1939),
    (uuid.uuid4(), "Dream of the Red Chamber", "Cao Xueqin", 1791),
    (uuid.uuid4(), "The Hobbit", "J. R. R. Tolkien", 1937),
]


def upload_employee(library):

    library.register_employee(Librarian("Petrov Oleg", "3"))
    library.register_employee(Librarian("Smit Tom", "0.5"))
    library.register_employee(SeniorLibrarian("Melekina Anna", "10"))
    library.register_employee(Cleaner("Sidorov Ivan", "7"))
    library.register_employee(Employee("Melnuk Eva", "1.5"))


def upload_books(library):
    for isbn, title, author, year in BOOKS_TO_LOAD:
        library.add(Book(isbn, title, author, year))


def info(library):
    print("Список книг:")
    for b in library.book_list:
         print(f"- {b.author} - {b.title}/{b.year}")

    print("Список працівнків:")

    for i in library.employees:
        print(f"- {i.get_details().get('name')}:- \"{i.get_details().get('description')}\"")


if __name__ == "__main__":
    one_citys_library = Library()
    upload_books(one_citys_library)
    upload_employee(one_citys_library)
    my_reading, query = None, "And Then There Were None"
    if one_citys_library.search(query) != -1:
        print("OMG! They have it")
        my_reading = one_citys_library.lend(query)
    else:
        print("Damn! nothing to read.")

    print("My current reading: ")
    description = "nothing interesting" if my_reading is None \
        else f"{my_reading.isbn}, {my_reading.title}, {my_reading.author}, {my_reading.year}"
    print(description)
    info(one_citys_library)

