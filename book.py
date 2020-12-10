class Book:
    def __init__(self, author, title, pagecount):
        self.author = author
        self.title = title
        self.pagecount = pagecount

    def print_book(self):
        print(f"{self.title} by {self.author}")


# if __name__ == "__main__":
#     # If you run this file from the terminal this block is run
#     book = Book("Amman Sood", "A terrible book", 300)
#     print(f'{book.author} wrote "{book.title}" which is {book.pagecount} pages long.')
