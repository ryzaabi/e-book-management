class Discount:
    """Applies loyalty and bulk discounts to orders."""

    def __init__(self, loyalty_discount_rate=0.10, bulk_discount_rate=0.20, min_bulk_items=5):
        self.__loyalty_discount_rate = loyalty_discount_rate
        self.__bulk_discount_rate = bulk_discount_rate
        self.__min_bulk_items = min_bulk_items
        self.__last_applied_discount = 0.0

    # Getters and Setters
    def getLoyaltyDiscountRate(self):
        return self.__loyalty_discount_rate

    def setLoyaltyDiscountRate(self, rate):
        self.__loyalty_discount_rate = rate

    def getBulkDiscountRate(self):
        return self.__bulk_discount_rate

    def setBulkDiscountRate(self, rate):
        self.__bulk_discount_rate = rate

    def getMinBulkItems(self):
        return self.__min_bulk_items

    def setMinBulkItems(self, min_items):
        self.__min_bulk_items = min_items

    def getLastAppliedDiscount(self):
        return self.__last_applied_discount

    def setLastAppliedDiscount(self, discount):
        self.__last_applied_discount = discount

    # Apply Discounts
    def applyLoyaltyDiscount(self, order):
        discount = order.getTotalPrice() * self.__loyalty_discount_rate
        order.applyDiscount(discount)
        self.setLastAppliedDiscount(discount)
        return discount

    def applyBulkDiscount(self, order):
        if len(order.getEbooks()) >= self.__min_bulk_items:
            discount = order.getTotalPrice() * self.__bulk_discount_rate
            order.applyDiscount(discount)
            self.setLastAppliedDiscount(discount)
            return discount
        return 0.0

    def __str__(self):
        return (f"Loyalty Discount Rate: {self.__loyalty_discount_rate * 100}%\n"
                f"Bulk Discount Rate: {self.__bulk_discount_rate * 100}%\n"
                f"Minimum Bulk Items for Discount: {self.__min_bulk_items}\n"
                f"Last Applied Discount: ${self.__last_applied_discount:.2f}")
