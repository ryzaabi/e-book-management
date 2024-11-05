class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def getTitle(self):
        #Returns the title of the eBook
        return self.__title

    def getAuthor(self):
        #Returns the author of the eBook
        return self.__author

    def getPrice(self):
        #Returns the price of the eBook
        return self.__price

    def __str__(self):
        return f"{self.__title} by {self.__author} - ${self.__price:.2f}"
