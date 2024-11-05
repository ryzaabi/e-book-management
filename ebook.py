class EBook:
    """Represents an e-book in the bookstore's catalog."""

    def __init__(self, title, author, publication_date, genre, price):
        self.__book_info = {"title": title, "author": author}
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters and Setters
    def getTitle(self):
        return self.__book_info["title"]

    def setTitle(self, title):
        self.__book_info["title"] = title

    def getAuthor(self):
        return self.__book_info["author"]

    def setAuthor(self, author):
        self.__book_info["author"] = author

    def getPublicationDate(self):
        return self.__publication_date

    def setPublicationDate(self, publication_date):
        self.__publication_date = publication_date

    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.getTitle()} by {self.getAuthor()} - ${self.getPrice():.2f}"
