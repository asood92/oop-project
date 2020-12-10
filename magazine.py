from book import Book


class Magazine(Book):
    """
    Magazine instantiates a magazine object, which both inherits from and is a subclass of Book.
    _type is not required outside of this class and is protected for that reason
    """

    _type = "Magazine"

    def __init__(self):
        """
        Initializes a graphic novel object, inheriting from book with super()
        """
        super().__init__()
        self.month = self.getMonth()
        self.year = self.getYear()

    def getMonth(self):
        """Prompts for user input for issue month
        Returns:
            string input
        """
        return input(f"Please enter the month of this issue of {self._type}: ")

    def getYear(self):
        """Prompts for user input for issue year
        Returns:
            string input
        """
        return input(f"Please enter the year of this issue of {self._type}: ")

    def contains(self, query):
        """
        Conditional function to parse through the object for a
        matching month or year. Inherits from and overrides the contains method in Book.
        Returns:
            containsQuery: Boolean flag
        """
        containsQuery = super().contains(query)
        if self.month.find(query) != -1:
            containsQuery = True
        if self.year.find(query) != -1:
            containsQuery = True
        return containsQuery

    def print_info(self):
        """
        Inherits everything in print_info() from Book, adds additional information only pertinent
        to Magazine, and outputs the full object information
        """
        return f"""{super().print_info()}\nMonth of Issue: {self.month}\nYear of Issue: {self.year}"""


if __name__ == "__main__":
    # If you run this file from the terminal this block is run
    magazine = Magazine()
    print(magazine.contains("Test"))