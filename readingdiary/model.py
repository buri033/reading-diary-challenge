from datetime import datetime


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:

        if page > self.pages:
            return False
        else:
            note = Note(text, page, date)
            self.notes.append(note)
            return True

    def set_rating(self, rating: int) -> bool:
        if not rating == Book.EXCELLENT and rating == Book.GOOD and rating == Book.BAD:
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        pages = [note.page for note in self.notes]
        if len(pages) == 0:
            return -1

        return max(set(pages), key=pages.count)

    def __str__(self) -> str:
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nRating: {"unrated"}"


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False

        book = Book(isbn, title, author, pages)
        self.books[isbn] = book
        return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:

        book = self.search_by_isbn(isbn)
        if not book:
            return False

        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Book | None:
        if not self.books:
            return None

        max_notes_book = None
        max_notes = 0
        for book in self.books.values():
            if len(book.notes) > max_notes:
                max_notes = len(book.notes)
                max_notes_book = book

        return max_notes_book
# TODO: Add code here
