from factory_method import ConcreteBookFactory
from observer import Members
from observer import NotificationSystem 

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Library():
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            print(book.title)
    
    def display_members(self):
        for member in self.members:
            print(member.name)

if __name__ == "__main__":

    library1 = Library()
    library2 = Library()

    ebook = ConcreteBookFactory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)
    paperback = ConcreteBookFactory.create_book("paperback", "The Alchemist", "Paulo Coelho", "987654321", 10)

    notification_system = NotificationSystem()
    member1 = Members("Alice", notification_system)
    member2 = Members("Bob", notification_system)
    library1.add_member(member1)
    library1.add_member(member2)

    library1.add_book(ebook)
    library1.add_book(paperback)

    library2.display_books()
    library2.display_members()