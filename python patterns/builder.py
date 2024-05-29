from factory_method import ConcreteBookFactory

class BookBuilder:
    def __init__(self, book):
        self.book = book
        self.genre = None
        self.language = None
    
    def add_genre(self, genre):
        self.book.genre = genre
        return self

    def add_language(self, language):
        self.book.language = language
        return self

    def build(self):
        return self.book
    

if __name__ == "__main__":
    ebook = ConcreteBookFactory.create_book("ebook", "Digital Fortress", "Dan Brown", "123456789", 5)

    book_builder = BookBuilder(ebook)
    ebook = book_builder.add_genre("Thriller").add_language("English").build()

    print(ebook.genre)
    print(ebook.language)