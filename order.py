from datetime import date

class Order:
    def __init__(self, order_date, ebooks, discount_applied=0.0):
        self.__order_date = order_date
        self.__ebooks = ebooks
        self.__discount_applied = discount_applied
        self.__total_price = self.calculateTotal()

    def calculateTotal(self):
        #Calculates the total price after applying discounts
        subtotal = sum(ebook.getPrice() for ebook in self.__ebooks)
        return subtotal - self.__discount_applied

    def applyDiscount(self, discount):
        #Applies a discount to the Order
        self.__discount_applied = discount
        self.__total_price = self.calculateTotal()

    def getTotalPrice(self):
        #Returns the total price of the Order after discounts
        return self.__total_price

    def __str__(self):
        return f"Order Date: {self.__order_date}\nTotal Price after Discount: ${self.__total_price:.2f}"
