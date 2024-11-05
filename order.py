from datetime import date

class Order:
    """Represents a customer's order."""

    def __init__(self, order_id, order_date, ebooks, discount_applied=0.0):
        # Initialize order with ID, date, list of eBooks, and any discount
        self.__order_id = order_id
        self.__order_date = order_date
        self.__ebooks = ebooks
        self.__discount_applied = discount_applied
        self.__total_price = self.calculateTotal()  # Calculate initial total price

    # Getters and Setters
    def getOrderId(self):
        """Get the order ID."""
        return self.__order_id

    def setOrderId(self, order_id):
        """Set a new order ID."""
        self.__order_id = order_id

    def getOrderDate(self):
        """Get the order date."""
        return self.__order_date

    def setOrderDate(self, order_date):
        """Set a new order date."""
        self.__order_date = order_date

    def getEbooks(self):
        """Get the list of eBooks in the order."""
        return self.__ebooks

    def setEbooks(self, ebooks):
        # Set a new list of eBooks and recalculate total price
        self.__ebooks = ebooks
        self.__total_price = self.calculateTotal()

    def getTotalPrice(self):
        """Get the total price of the order."""
        return self.__total_price

    def getDiscountApplied(self):
        """Get the discount applied to the order."""
        return self.__discount_applied

    def setDiscountApplied(self, discount_applied):
        # Set a new discount and recalculate total price
        self.__discount_applied = discount_applied
        self.__total_price = self.calculateTotal()

    # Calculate total price after discount
    def calculateTotal(self):
        subtotal = sum(ebook.getPrice() for ebook in self.__ebooks)  # Sum of eBook prices
        return subtotal - self.__discount_applied  # Subtract discount from subtotal

    def applyDiscount(self, discount):
        # Apply a discount to the order and recalculate total
        self.setDiscountApplied(discount)

    def __str__(self):
        # Return a summary of the order details
        return f"Order ID: {self.__order_id}, Date: {self.__order_date}, Total: ${self.__total_price:.2f}"
