class Invoice:
    """Generates an invoice for an order, including VAT and discounts."""

    VAT_RATE = 0.08  # 8% VAT rate

    def __init__(self, order, invoice_date):
        """
        Initializes the invoice with order details and invoice date.
        """
        self.__subtotal = order.getTotalPrice()  # Total price before taxes and discounts
        self.__discounts = order.getDiscountApplied()  # Applied discounts
        self.__taxes = self.__subtotal * self.VAT_RATE  # Calculate VAT
        self.__final_total = self.__subtotal + self.__taxes - self.__discounts  # Final total after applying VAT and discounts
        self.__invoice_date = invoice_date  # Date of the invoice

    # Getters and Setters
    def getSubtotal(self):
        return self.__subtotal

    def setSubtotal(self, subtotal):
        """Sets a new subtotal and updates the final total."""
        self.__subtotal = subtotal
        self.__updateFinalTotal()

    def getDiscounts(self):
        return self.__discounts

    def setDiscounts(self, discounts):
        """Sets new discounts and updates the final total."""
        self.__discounts = discounts
        self.__updateFinalTotal()

    def getTaxes(self):
        return self.__taxes

    def setTaxes(self, taxes):
        """Sets new tax amount and updates the final total."""
        self.__taxes = taxes
        self.__updateFinalTotal()

    def getFinalTotal(self):
        return self.__final_total

    def getInvoiceDate(self):
        return self.__invoice_date

    def setInvoiceDate(self, invoice_date):
        """Sets a new invoice date."""
        self.__invoice_date = invoice_date

    def __updateFinalTotal(self):
        """Updates the final total based on subtotal, discounts, and taxes."""
        self.__final_total = self.__subtotal + self.__taxes - self.__discounts

    def generateInvoice(self):
        """Creates a summary of the invoice."""
        return (f"Invoice Date: {self.__invoice_date}\nSubtotal: ${self.__subtotal:.2f}\n"
                f"Discounts: ${self.__discounts:.2f}\nVAT: ${self.__taxes:.2f}\n"
                f"Final Total: ${self.__final_total:.2f}")

    def __str__(self):
        """Returns the invoice summary as a string."""
        return self.generateInvoice()
