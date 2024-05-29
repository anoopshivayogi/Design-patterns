from abc import ABC, abstractmethod

class BookFactory(ABC):
    @abstractmethod
    def create_book(self, title, author, isbn, copies):
        pass

class Book(ABC):
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    @abstractmethod
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")

class EBook(Book):
    def display_info(self):
        print(f"EBook: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")

class PaperBook(Book):
    def display_info(self):
        print(f"PaperBook: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")

class concreteBookFactory(BookFactory):
    @staticmethod
    def create_book(book_type, title, author, isbn, copies):
        if book_type == "ebook":
            return EBook(title, author, isbn, copies)
        elif book_type == "paperback":
            return PaperBook(title, author, isbn, copies)
        else:
            raise ValueError("Invalid book type")
        
    def example(self):
        print("This is an example method")
        
obj = concreteBookFactory()
obj.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)