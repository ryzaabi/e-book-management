class EBook:
    """Represents an e-book in the bookstore's catalog."""

    def __init__(self, title, author, publication_date, genre, price):
        """
        Initializes the e-book with title, author, publication date, genre, and price.
        """
        # Store title and author in a dictionary for easy access
        self.__book_info = {"title": title, "author": author}
        # Set the other attributes directly
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters and Setters for each attribute
    def getTitle(self):
        """Returns the title of the e-book."""
        return self.__book_info["title"]

    def setTitle(self, title):
        """Sets a new title for the e-book."""
        self.__book_info["title"] = title

    def getAuthor(self):
        """Returns the author of the e-book."""
        return self.__book_info["author"]

    def setAuthor(self, author):
        """Sets a new author for the e-book."""
        self.__book_info["author"] = author

    def getPublicationDate(self):
        """Returns the publication date of the e-book."""
        return self.__publication_date

    def setPublicationDate(self, publication_date):
        """Sets a new publication date for the e-book."""
        self.__publication_date = publication_date

    def getGenre(self):
        """Returns the genre of the e-book."""
        return self.__genre

    def setGenre(self, genre):
        """Sets a new genre for the e-book."""
        self.__genre = genre

    def getPrice(self):
        """Returns the price of the e-book."""
        return self.__price

    def setPrice(self, price):
        """Sets a new price for the e-book."""
        self.__price = price

    def __str__(self):
        """Returns a string representation of the e-book with title, author, and price."""
        return f"{self.getTitle()} by {self.getAuthor()} - ${self.getPrice():.2f}"
