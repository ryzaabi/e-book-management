class ShoppingCart:
    """Represents a shopping cart for a customer."""

    def __init__(self, cart_owner, created_date):
        self.__cart_items = []
        self.__cart_owner = cart_owner
        self.__total_items = 0
        self.__created_date = created_date

    # Add and Remove Items
    def addItem(self, ebook):
        self.__cart_items.append(ebook)
        self.__total_items += 1

    def removeItem(self, ebook):
        if ebook in self.__cart_items:
            self.__cart_items.remove(ebook)
            self.__total_items -= 1

    # Getters and Setters
    def getCartItems(self):
        return self.__cart_items

    def setCartItems(self, cart_items):
        self.__cart_items = cart_items
        self.__total_items = len(cart_items)

    def getTotalItems(self):
        return self.__total_items

    def getCreatedDate(self):
        return self.__created_date

    # Calculate Total Price
    def getTotalPrice(self):
        return sum(ebook.getPrice() for ebook in self.__cart_items)

    def __str__(self):
        return f"Shopping Cart for {self.__cart_owner.getName()} - {self.getTotalItems()} items"
