from datetime import date

class Order:
    """Represents a customer's order."""

    def __init__(self, order_id, order_date, ebooks, discount_applied=0.0):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__ebooks = ebooks
        self.__discount_applied = discount_applied
        self.__total_price = self.calculateTotal()

    # Getters and Setters
    def getOrderId(self):
        return self.__order_id

    def setOrderId(self, order_id):
        self.__order_id = order_id

    def getOrderDate(self):
        return self.__order_date

    def setOrderDate(self, order_date):
        self.__order_date = order_date

    def getEbooks(self):
        return self.__ebooks

    def setEbooks(self, ebooks):
        self.__ebooks = ebooks
        self.__total_price = self.calculateTotal()

    def getTotalPrice(self):
        return self.__total_price

    def getDiscountApplied(self):
        return self.__discount_applied

    def setDiscountApplied(self, discount_applied):
        self.__discount_applied = discount_applied
        self.__total_price = self.calculateTotal()

    # Methods for total calculation
    def calculateTotal(self):
        subtotal = sum(ebook.getPrice() for ebook in self.__ebooks)
        return subtotal - self.__discount_applied

    def applyDiscount(self, discount):
        self.setDiscountApplied(discount)

    def __str__(self):
        return f"Order ID: {self.__order_id}, Date: {self.__order_date}, Total: ${self.__total_price:.2f}"
