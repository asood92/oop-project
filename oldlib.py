from book import Book


class Library:
    def __init__(self, book_list=[]):
        self.book_list = book_list

    def new_book(self, book):
        self.book_list.append(book)

    def remove_book(self, title):  # book is the title of the book
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)
                break

    def print_books(self):
        for book in self.book_list:
            print(f"Book {book.title} by {book.author}")


# class Book:
#     def __init__(self, author, title, pagecount):
#         self.author = author
#         self.title = title
#         self.pagecount = pagecount

#     def print_book(self):
#         """ Prints the book info"""
#         return f"{self.title} is written by {self.author}"


# class Magazine(Book):
#     def __init__(
#         self,
#         author,
#         title,
#         pagecount,
#         month,
#         year,
#     ):
#         Book.__init__(self, author, title, pagecount)

#         self.month = month
#         self.year = year

#     def display(self):
#         return f"{self.title} is {self.pagecount} pages long. It's the {self.month} {self.year} issue."


class Graphic_Novel(Book):
    def __init__(self, author, title, pagecount, artist, issueNumber=None):
        Book.__init__(self, author, title, pagecount)
        self.artist = artist
        if issueNumber is None:
            self.issueNumber = input("What is the issue number of this graphic novel?")
        else:
            self.issueNumber = issueNumber

    def __repr__(self):
        return f"The graphic novel: ({self.title}, is illustrated by {self.artist}, is {self.pagecount} pages long, and is issue # {self.issueNumber}"


# class ReadingList:
#     def __init__(self):
#         self.list = []

#     def add_book(self, book):
#         """Add book to reading list"""
#         self.list.append(book)

#     def remove_book(self, book):
#         """Remove book from reading list"""
#         self.list.remove(book)

#     def total_pages(self):
#         """Returns total pages in reading list"""
#         total = 0
#         for book in self.list:
#             total += book.pages
#         return total

#     def __repr__(self):
#         return f"ReadingList({self.list})"

#     def __str__(self):
#         return f"Reading list of size {len(self.list)}"


# Initialise Library
# library = Library()

# Create a few books
# novel1 = Book("Harry Potter", 500, 1991)
# novel2 = Book("LotR", 1000, 1960)
# novel3 = Book("Game of Thrones", 2000, 2018)
# # comic1 = Graphic_Novel("Batman", 100, 2020, "Stan Lee")

my_lib = Library()
my_lib.new_book(Book("J.K Rowling", "Harry Potter", 1000))
my_lib.new_book(Book("Aryan Parekh", "Stack", 500))

# my_lib.remove_book("Stack")

my_lib.print_books()
# # Add books to library.
# library.new_book(novel1)
# library.new_book(novel2)
# library.new_book(novel3)
# # library.new_book(comic1)

# novel1.print_book()
# novel2.print_book()
# novel3.print_book()
# comic1.print_book()
# Create a new reading list.
# readingListOne = ReadingList()

# # Add a couple of books to reading list.
# readingListOne.add_book(novel1)
# readingListOne.add_book(comic1)