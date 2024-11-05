class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def addItem(self, ebook):
        #Adds an eBook to the shopping cart."
        self.cart_items.append(ebook)

    def removeItem(self, ebook):
        #Removes an eBook from the shopping cart
        if ebook in self.cart_items:
            self.cart_items.remove(ebook)

    def getTotalPrice(self):
        #Calculates and returns the total price of all eBooks in the cart.
        return sum(ebook.getPrice() for ebook in self.cart_items)
