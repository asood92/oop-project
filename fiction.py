from book import Book


class Movie(Book):
    def __init__(self, author, title, pagecount, series, genre):
        super().__init__(author, title, pagecount)
        self.series = series
        self.genre = genre

    def print_book(self):
        print(
            f"{self.title} by {self.author} in the series {self.series} under the {self.genre} genre"
        )


# if __name__ == "__main__":
#     # If you run this file from the terminal this block is run
#     book = Book("Amman Sood", "A terrible book", 300)
#     print(f'{book.author} wrote "{book.title}" which is {book.pagecount} pages long.')
