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
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"
