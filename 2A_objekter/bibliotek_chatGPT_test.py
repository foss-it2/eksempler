from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, publication_year, code):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.code = code


class PrintedBook(Book):
    def __init__(self, title, author, publication_year, code):
        super().__init__(title, author, publication_year, code)


class EBook(Book):
    def __init__(self, title, author, publication_year, code, download_link):
        super().__init__(title, author, publication_year, code)
        self.download_link = download_link
        self.expiry_date = None

    def set_expiry_date(self):
        self.expiry_date = datetime.now() + timedelta(days=30)


class RareBook(Book):
    def __init__(self, title, author, publication_year, code, location):
        super().__init__(title, author, publication_year, code)
        self.location = location


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_book_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_book_by_code(self, code):
        return [book for book in self.books if book.code == code]

    def search_book_by_publication_year(self, year):
        return [book for book in self.books if book.publication_year == year]

    def __str__(self):
        book_list = []
        for book in self.books:
            book_list += f"Title: {book.title}\n"
            book_list += f"Author: {book.author}\n"
            book_list += f"Publication Year: {book.publication_year}\n"
            if isinstance(book, EBook):  # Sjekker om boken er en EBook
                book_list += f"Download Link: {book.download_link}\n"
                if book.expiry_date:
                    book_list += f"Expiry Date: {book.expiry_date}\n"
            elif isinstance(book, RareBook):  # Sjekker om boken er en RareBook
                book_list += f"Location: {book.location}\n"
            book_list += "\n"
        return f"Books in library:\n{book_list}"


library = Library()

bok1 = PrintedBook("tittel","forfatter",2024,12345)

library.add_book(bok1)

print(library)

