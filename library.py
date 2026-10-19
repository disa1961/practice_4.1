class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self._is_available = True
        self._last_read_pages = 0

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read):
        if self._is_available:
            raise ValueError("Книга и так на полке")
        if pages_read < 0 or pages_read > self.pages:
            raise ValueError("Некорректное число прочитанных страниц")
        self._is_available = True
        self._last_read_pages = pages_read

    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def lend(self, isbn, reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError("Книги с таким ISBN нет в фонде")
        if not book.is_available:
            raise ValueError("Книга уже выдана")
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        book = self.find_by_isbn(isbn)
        if book is None or book not in reader.books:
            raise ValueError("У читателя нет этой книги")
        if pages_read < 0 or pages_read > book.pages:
            raise ValueError("Некорректное число прочитанных страниц")
        book.give_back(pages_read)
        reader.books.remove(book)
        reader.pages_read += pages_read

    def available(self):
        return [book for book in self._books if book.is_available]

    def unfinished(self):
        return [
            book for book in self._books
            if 0 < book.last_read_pages < book.pages
        ]

    def __len__(self):
        return len(self._books)
