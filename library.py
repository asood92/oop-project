from book import Book
from graphic_novel import Graphic_Novel
from magazine import Magazine


class Library:
    """
    Library instantiates list catalog, which is composed of objects
    from the Book, Magazine, and Graphic_Novel classes
    """

    catalog = []

    def add_book(self):
        """Initializes a new Book object, and appends it to catalog[]"""
        self.catalog.append(Book())

    def add_magazine(self):
        """Initializes a new Magazine object, and appends it to catalog[]"""
        self.catalog.append(Magazine())

    def add_graphic_novel(self):
        """Initializes a new Graphic Novel object, and appends it to catalog[]"""
        self.catalog.append(Graphic_Novel())

    def filterCatalog(self, filter):
        """
        filterCatalog is passed the parameter filter,
        which is either Book, Magazine or Graphic Novel,
        and then prints out every object in catalog matching that filter
        """
        for item in self.catalog:
            if type(item) == filter:
                print(item)

    def searchCatalog(self, query):
        """
        searchCatalog is passed the query filter,
        which is any string the user enters,
        and if found in any object, that object is printed
        """
        for item in self.catalog:
            if item.contains(query):
                print(item)

    def print_catalog(self):
        """
        Simple function to print every item in catalog
        """
        for item in self.catalog:
            print(item)


""" Executed if the user runs library.py from terminal """
if __name__ == "__main__":
    """ Instantiates Library, then gathers user input for desired function, and outputs accordingly"""
    library = Library()
    choice = 0
    while choice != -1:
        choice = int(
            input(
                "Would you like to add a book, magazine, or graphic novel?\n 1 for book,\n 2 for magazine,\n 3 for graphic novel,\n 4 to filter the catalog by media type,\n 5 to search the catalog by a query, or\n 6 to print the entire catalog or\n -1 to quit.: "
            )
        )
        print()
        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.add_magazine()

        elif choice == 3:
            library.add_graphic_novel()

        elif choice == 4:
            searchType = int(
                input(
                    "Enter 1, 2 or 3 to view all books, magazines or graphic novels, respectively: "
                )
            )
            if searchType == 1:
                library.filterCatalog(Book)

            elif searchType == 2:
                library.filterCatalog(Magazine)

            elif searchType == 3:
                library.filterCatalog(Graphic_Novel)

        elif choice == 5:
            searchType = input(
                "Please enter what you would like to search the catalog for: "
            )
            library.searchCatalog(searchType)

        elif choice == 6:
            library.print_catalog()

    print("Thanks for checking out your local library, have a great day! \n")