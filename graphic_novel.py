from book import Book


class Graphic_Novel(Book):
    """
    Graphic_Novel instantiates a graphic novel object, which both inherits from and is a subclass of Book.
    _type is not required outside of this class and is protected for that reason
    """

    _type = "Graphic Novel"

    def __init__(self):
        """
        Initializes a graphic novel object, inheriting from book with super()
        """
        super().__init__()
        self.artist = self.getArtist()
        self.issue = self.getIssue()

    def getArtist(self):
        """Prompts for user input for artist name
        Returns:
            string input
        """
        return input(f"Please enter the artist of this {self._type}: ")

    def getIssue(self):
        """Prompts for user input for issue number
        Returns:
            string input
        """
        return input(f"Please enter the issue number of this {self._type}: ")

    def contains(self, query):
        """
        Conditional function to parse through the object for a
        matching artist or issue number. Inherits from and overrides the contains method in Book.
        Returns:
            containsQuery: Boolean flag
        """
        containsQuery = super().contains(query)
        if self.artist.find(query) != -1:
            containsQuery = True
        if self.artist.find(query) != -1:
            containsQuery = True

        return containsQuery

    def print_info(self):
        """
        Inherits everything in print_info() from Book, adds additional information only pertinent
        to Graphic Novels, and outputs the full object information
        """
        return f"""{super().print_info()}\nArtist: {self.artist}\nIssue: {self.issue}"""


if __name__ == "__main__":
    # If you run this file from the terminal this block is run
    comic = Graphic_Novel()
    print(comic.contains("Test"))