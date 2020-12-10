from graphic_novel import Graphic_Novel
from book import Book
from magazine import Magazine


class Library:

    catalog = []

    def add_book(self):
        choice = int(
            input(
                "Would you like to add a book, magazine, or graphic novel? Type 1 for book, 2 for magazine or 3 for graphic novel: "
            )
        )

        while (choice != 1) or (choice != 2) or (choice != 3):
            choice = int(
                input(
                    "Invalid selection. \n Would you like to add a book, magazine, or graphic novel? Type 1 for book, 2 for magazine or 3 for graphic novel: "
                )
            )

        title = input(
            "What is the title of the item you are adding to the library? \n "
        )
        author = input("Who is the author?  \n")
        pagecount = input("How many pages is it?  \n")

        if choice == 2:
            month = input("What month is this magazine from? \n")
            year = input("What year is this magazine from? \n")
            return Magazine(title, author, pagecount, month, year)

        elif choice == 3:
            artist = input("Who is the artist? \n")
            issueNumber = input("What issue number is it?? \n")
            return Graphic_Novel(author, title, pagecount, artist, issueNumber)
        else:
            return Book(title, author, pagecount)

    def append_book(self, book):
        self.catalog.append(book)

    # def add_magazine(self):
    #     title = input(
    #         "What is the title of the book you are adding to the library? \n  "
    #     )
    #     author = input("Who is the author?  \n")
    #     pagecount = input("How many pages is it?  \n")
    #     month = input("What month is this magazine from? \n")
    #     year = input("What year is this magazine from? \n")

    #     return Magazine(title, author, pagecount, month, year)

    # def append_magazine(self):
    #     newMagazine = self.add_magazine()
    #     print(newMagazine)
    #     self.catalog.append(newMagazine)

    # def add_graphic_novel(self):
    #     title = input(
    #         "What is the title of the graphic novel you are adding to the library? \n  "
    #     )
    #     author = input("Who is the author?  \n")
    #     pagecount = input("How many pages is it?  \n")
    #     artist = input("Who is the artist? \n")
    #     issueNumber = input("What issue number is it?? \n")

    #     return Graphic_Novel(author, title, pagecount, artist, issueNumber)

    # def append_graphic_novel(self):
    #     newComic = self.add_graphic_novel()
    #     self.catalog.append(newComic)

    def __str__(self):
        return f"""
        *************\n
        Book Title: {self.title}\n
        Author: {self.author}\n
        Page Count: {self.pagecount}\n
        Month of Issue: {self.month}
        Year of Issue: {self.year}\n
        **************"""


if __name__ == "__main__":
    library = Library()
    magazine1 = Magazine("Time ", "A new Hope", 300, "December", "2020")
    magazine2 = Magazine(" Magazine", "A Hope", 800, "December", "2121")
    library.append_book(magazine1)
    library.append_book(magazine2)
