from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        details = f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"
        return details

    @abstractmethod
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")


class EBook(Book):
    def display_info(self):
        print(f"EBook: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")

class PaperBook(Book):
    def display_info(self):
        print(f"PaperBook: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")


# class BookFactory:
#     @abstractmethod
#     def create_book(self, title, author, isbn, copies):
#         pass

class ConcreteBookFactory:
    @staticmethod
    def create_book(book_type, title, author, isbn, copies):
        if book_type == "ebook":
            return EBook(title, author, isbn, copies)
        elif book_type == "paperback":
            return PaperBook(title, author, isbn, copies)
        else:
            raise ValueError("Invalid book type")


if __name__ == "__main__":
        
    # Creating a factory
    book_factory = ConcreteBookFactory()

    # Creating an eBook
    ebook = ConcreteBookFactory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)
    ebook.display_info()

    # Creating a Paperback book
    paperback = ConcreteBookFactory.create_book("paperback", "The Alchemist", "Paulo Coelho", "987654321", 10)
    paperback.display_info()
