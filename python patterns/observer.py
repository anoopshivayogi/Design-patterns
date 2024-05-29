from abc import ABC, abstractmethod
from typing import List 
from factory_method import ConcreteBookFactory


class Observer(ABC):
    def update(self, value):
        pass

class NotificationSystem:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self, value):
        for observer in self.observers:
            observer.update(value)

class Members(Observer):
    def __init__(self, name, notification_system: NotificationSystem):
        self.name = name
        self.notification_system = notification_system
        self.notification_system.add_observer(self)
        self.books = []

    def borrow_book(self, book):
        self.books.append(book)
        self.notification_system.notify_observers(f"{self.name} borrowed {book.title}")

    def returned_book(self, book):
        self.books.append(book)
        self.notification_system.notify_observers(f"{self.name} returned {book.title}")
        
    def update(self, value):
        print(f"{self.name} received a notification: {value}")

    def list_books(self):
        print(f"{self.name} has the following books:")
        for book in self.books:
            print(book.title)

if __name__ == "__main__":

    notification_system = NotificationSystem()
    member1 = Members("Alice", notification_system)
    member2 = Members("Bob", notification_system)

    book_factory = ConcreteBookFactory()
    ebook = book_factory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)
    paperback = book_factory.create_book("paperback", "The Alchemist", "Paulo Coelho", "987654321", 10)

    member1.borrow_book(ebook)
    member2.borrow_book(paperback)

    member1.list_books()
    member2.list_books()

    member1.returned_book(ebook)
    member2.returned_book(paperback)

    member1.list_books()
    member2.list_books()