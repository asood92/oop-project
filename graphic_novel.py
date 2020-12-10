from book import Book


class Graphic_Novel(Book):
    def __init__(self, author, title, pagecount, artist, issueNumber=None):
        super.__init__(author, title, pagecount)
        self.artist = artist

        if issueNumber is None:
            self.issueNumber = input("What is the issue number of this graphic novel?")
        else:
            self.issueNumber = issueNumber

        return