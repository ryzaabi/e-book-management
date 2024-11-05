class Discount:
    """Class to apply loyalty and bulk discounts to orders."""

    def __init__(self, loyalty_discount_rate=0.10, bulk_discount_rate=0.20, min_bulk_items=5):
        # Initialize discount rates and minimum items for bulk discount
        self.__loyalty_discount_rate = loyalty_discount_rate
        self.__bulk_discount_rate = bulk_discount_rate
        self.__min_bulk_items = min_bulk_items
        self.__last_applied_discount = 0.0  # Track last applied discount amount

    # Getters and Setters
    def getLoyaltyDiscountRate(self):
        """Get the loyalty discount rate."""
        return self.__loyalty_discount_rate

    def setLoyaltyDiscountRate(self, rate):
        """Set a new loyalty discount rate."""
        self.__loyalty_discount_rate = rate

    def getBulkDiscountRate(self):
        """Get the bulk discount rate."""
        return self.__bulk_discount_rate

    def setBulkDiscountRate(self, rate):
        """Set a new bulk discount rate."""
        self.__bulk_discount_rate = rate

    def getMinBulkItems(self):
        """Get the minimum number of items for bulk discount eligibility."""
        return self.__min_bulk_items

    def setMinBulkItems(self, min_items):
        """Set the minimum number of items required for bulk discount."""
        self.__min_bulk_items = min_items

    def getLastAppliedDiscount(self):
        """Get the last applied discount amount."""
        return self.__last_applied_discount

    def setLastAppliedDiscount(self, discount):
        """Update the last applied discount amount."""
        self.__last_applied_discount = discount

    # Apply Discounts
    def applyLoyaltyDiscount(self, order):
        """
        Apply a loyalty discount to the order.
        Calculates 10% discount and applies it to the order's total price.
        """
        discount = order.getTotalPrice() * self.__loyalty_discount_rate
        order.applyDiscount(discount)
        self.setLastAppliedDiscount(discount)  # Update last applied discount
        return discount

    def applyBulkDiscount(self, order):
        """
        Apply a bulk discount if order meets the minimum item requirement.
        Checks if order has 5 or more items, then applies 20% discount.
        """
        if len(order.getEbooks()) >= self.__min_bulk_items:
            discount = order.getTotalPrice() * self.__bulk_discount_rate
            order.applyDiscount(discount)
            self.setLastAppliedDiscount(discount)  # Update last applied discount
            return discount
        return 0.0  # No discount if conditions are not met

    def __str__(self):
        """Return a summary of the discount details."""
        return (f"Loyalty Discount Rate: {self.__loyalty_discount_rate * 100}%\n"
                f"Bulk Discount Rate: {self.__bulk_discount_rate * 100}%\n"
                f"Minimum Bulk Items for Discount: {self.__min_bulk_items}\n"
                f"Last Applied Discount: ${self.__last_applied_discount:.2f}")
