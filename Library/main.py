from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    total: int = 1
    available: int = 1

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


@dataclass
class Reader:
    name: str
    surname: str
    id: int
    borrowed: list[Book] = field(default_factory=lambda: [])

    def __eq__(self, other):
        return self.id == other.id


@dataclass
class Library:
    books: list[Book] = field(default_factory=lambda: [])
    readers: list[Reader] = field(default_factory=lambda: [])

    def find_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                print("There is such book!")
                return book
            return None

    def find_reader(self, reader_id):
        for reader in self.readers:
            if reader.id == reader_id:
                return reader

    def add_book(self, title, author):

        if book := self.find_book(title, author):
            book.total += 1
            book.available += 1
        else:
            new_book = Book(title, author)
            self.books.append(new_book)

    def add_reader(self, name, surname, reader_id):
        new_reader = Reader(name, surname, reader_id)
        for reader in self.readers:
            if reader == new_reader:
                print("Cannot append Reader.")
                return

        self.readers.append(new_reader)

    def lend_book(self, reader_id, title, author):
        reader = self.find_reader(reader_id)
        book = self.find_book(title, author)
        if reader and book and book.available >= 1:
            book.available -= 1
            reader.borrowed.append(book)
        else:
            print(f"Book {title} is not available. Try again later.")


library = Library()
library.add_book('Hobbit', 'J.R.R. Tolkien')
library.add_book('Hobbit', 'J.R.R. Tolkien')
library.add_book('Władca Pierścieni', 'J.R.R. Tolkien')
library.add_reader('Adam', 'Nowak', 1)
library.add_reader('Adam', 'Nowak', 1)
library.add_reader('Adam', 'Nowak', 2)
library.find_book('Hobbit', 'J.R.R. Tolkien')
library.lend_book(1, 'Hobbit', 'J.R.R. Tolkien')
library.lend_book(1, 'Hobbit', 'J.R.R. Tolkien')
library.lend_book(2, 'Hobbit', 'J.R.R. Tolkien')
print(library)
print(library.find_reader(1))