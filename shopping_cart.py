class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def addItem(self, ebook):
        self.cart_items.append(ebook)

    def removeItem(self, ebook):
        if ebook in self.cart_items:
            self.cart_items.remove(ebook)

    def getTotalPrice(self):
        return sum(ebook.getPrice() for ebook in self.cart_items)
