from abc import ABC, abstractmethod
from factory_method import ConcreteBookFactory

class BookDecorator(ABC):
    def __init__(self, book):
        self._book = book

    @abstractmethod
    def display_info(self):
        pass

    def __str__(self):
        return self._book.__str__()


class GenreDecorator(BookDecorator):
    def __init__(self, book, genre):
        super().__init__(book)
        self._genre = genre

    def display_info(self):
        print(self._book)

    def __str__(self):
        return f"{self._book}, Genre: {self._genre}"


class LanguageDecorator(BookDecorator):
    def __init__(self, book, language):
        super().__init__(book)
        self._language = language

    def display_info(self):
        print(self._book) 
    
    def  __str__(self):
        return f"{self._book}, Language: {self._language}"


if __name__ == "__main__":
    ebook = ConcreteBookFactory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)
    ebook = GenreDecorator(ebook, "Thriller")
    ebook = LanguageDecorator(ebook, "English")

    print(ebook)