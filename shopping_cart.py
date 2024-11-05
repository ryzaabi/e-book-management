class ShoppingCart:
    """Represents a shopping cart for a customer."""

    def __init__(self, cart_owner, created_date):
        # Initialize with an empty list of items, the cart owner, item count, and creation date
        self.__cart_items = []
        self.__cart_owner = cart_owner
        self.__total_items = 0
        self.__created_date = created_date

    # Add and Remove Items
    def addItem(self, ebook):
        # Add an eBook to the cart and update item count
        self.__cart_items.append(ebook)
        self.__total_items += 1

    def removeItem(self, ebook):
        # Remove an eBook if it exists in the cart and update item count
        if ebook in self.__cart_items:
            self.__cart_items.remove(ebook)
            self.__total_items -= 1

    # Getters and Setters
    def getCartItems(self):
        """Return the list of items in the cart."""
        return self.__cart_items

    def setCartItems(self, cart_items):
        # Set a new list of items and update item count
        self.__cart_items = cart_items
        self.__total_items = len(cart_items)

    def getTotalItems(self):
        """Return the total number of items in the cart."""
        return self.__total_items

    def getCreatedDate(self):
        """Return the date the cart was created."""
        return self.__created_date

    # Calculate Total Price
    def getTotalPrice(self):
        # Calculate total price of all eBooks in the cart
        return sum(ebook.getPrice() for ebook in self.__cart_items)

    def __str__(self):
        # Return a summary of the cart with owner and item count
        return f"Shopping Cart for {self.__cart_owner.getName()} - {self.getTotalItems()} items"
