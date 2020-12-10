class Book:
    """
    Book is the parent class for Magazine, and Graphic Novel.
    _type is protected as Magazine and Graphic Novel have their own type,
    and thus its not necessary for it to be accessible to all instances
    """

    _type = "Book"

    def __init__(
        self,
    ):
        """ Instantiates a Book object by calling getAuthor, getTitle and getPagecount"""
        self.author = self.getAuthor()
        self.title = self.getTitle()
        self.pagecount = self.getPagecount()

    def getAuthor(self):
        """Prompts for user input for author name
        Returns:
            string input
        """
        return input(f"Please enter the name of the {self._type}'s author: ")

    def getTitle(self):
        """Prompts for user input for title
        Returns:
            string input
        """
        return input(f"Please enter the title of the {self._type} you wish to add: ")

    def getPagecount(self):
        """Prompts for user input for title
        Returns:
            pagecount: num
        """
        return input(f"Please enter the number of pages in the {self._type}: ")

    def contains(self, query):
        """
        Conditional function to parse through the object for a
        matching author, title or pagecount
        Returns:
            containsQuery: Boolean flag
        """
        containsQuery = False
        if self.author.find(query) != -1:
            containsQuery = True
        if self.title.find(query) != -1:
            containsQuery = True
        if self.pagecount.find(query) != -1:
            containsQuery = True
        return containsQuery

    def print_info(self):
        """
        Function to pass to __str__ for Book, Magazine, or Graphic Novel item information for printing
        """
        return f"""Book Title: {self.title}\nAuthor: {self.author}\nPage Count: {self.pagecount}"""

    def __str__(self):
        """
        Print function to overload the default python method, which would
        output the memory address of the object if not overloaded
        Returns:
            formatted string
        """
        line = f"******************\n"
        return f"""{line}{self.print_info()}\n{line}"""


if __name__ == "__main__":
    # If you run this file from the terminal this block is run
    book = Book()
    print(book.contains("Test"))
