from book import Book


class Magazine(Book):
    def __init__(
        self,
        author,
        title,
        pagecount,
        month,
        year,
    ):
        Book.__init__(self, author, title, pagecount)
        self.author = author
        self.title = title
        self.pagecount = pagecount
        self.month = month
        self.year = year

    def add_magazine(self):
        return Magazine(self.title, self.author, self.pagecount, self.month, self.year)

    def __str__(self):
        return f"""
        *************\n
        Book Title: {self.title}\n
        Author: {self.author}\n
        Page Count: {self.pagecount}\n
        Month of Issue: {self.month}
        Year of Issue: {self.year}\n
        **************"""


# if __name__ == "__main__":
# If you run this file from the terminal this block is run
# magazine = Magazine("Time Magazine", "A new Hope", 300, "December", "2020")
# print(
#     f'{magazine.author} wrote "{magazine.title}" which is {magazine.pagecount} pages long. and which is the {magazine.month} {magazine.year} issue.'
# )
