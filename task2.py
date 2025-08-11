from abc import ABC, abstractmethod
import logging
from logger import logger

# Налаштування логування, щоб замінити print
# logging.basicConfig(level=logging.INFO, format='%(message)s')

# Принцип єдиної відповідальності (SRP)
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self) -> list[Book]:
        pass


# Принцип підстановки Лісков (LSP) та Принцип інверсії залежностей (DIP)
# Library тепер залежить від абстракцій (інтерфейсів)
class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        logger.info(f"Книгу '{book.title}' додано до бібліотеки.")

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]
        logger.info(f"Книгу з назвою '{title}' видалено.")

    def show_books(self):
        if not self.books:
            logger.info("Бібліотека порожня.")
        for book in self.books:
            logger.info(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

# Принцип відкритості/закритості (OCP)
class LibraryManager:
    def __init__(self, library: Library.add_book and Library.remove_book and Library.show_books):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()