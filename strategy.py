from abc import ABC, abstractmethod
from typing import List
from singleton import Library
from factory_method import ConcreteBookFactory


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, library):
        pass

class TitleSearchStrategy(SearchStrategy):
    def search(self, library, title):
        print("Searching by title")
        for book in library.books:
            if title == book.title:
                print(book)

class AuthorSearchStrategy(SearchStrategy):
    def search(self, library, author):
        print("Searching by author")
        for book in library.books:
            if author == book.author:
                print(book)


class Catalog:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def search(self, library, search_term):
        if self.strategy is None:
            print("No strategy set")
            return
        self.strategy.search(library, search_term)


if __name__ == "__main__":
    library = Library()

    ebook = ConcreteBookFactory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)
    paperback = ConcreteBookFactory.create_book("paperback", "The Alchemist", "Paulo Coelho", "987654321", 10)

    library.add_book(ebook)
    library.add_book(paperback)

    catalog = Catalog()
    catalog.set_strategy(TitleSearchStrategy())

    catalog.search(library, "Digital Fortress")

    catalog.set_strategy(AuthorSearchStrategy())
    catalog.search(library, "Paulo Coelho")