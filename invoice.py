class Invoice:
    """Generates an invoice for an order, including VAT and discounts."""

    VAT_RATE = 0.08  # VAT rate of 8%

    def __init__(self, order, invoice_date):
        # Initialize with order's total price, discounts, and calculate VAT and final total
        self.__subtotal = order.getTotalPrice()
        self.__discounts = order.getDiscountApplied()
        self.__taxes = self.__subtotal * self.VAT_RATE
        self.__final_total = self.__subtotal + self.__taxes - self.__discounts
        self.__invoice_date = invoice_date  # Date the invoice is created

    # Getters and Setters
    def getSubtotal(self):
        """Return the subtotal before VAT and discounts."""
        return self.__subtotal

    def setSubtotal(self, subtotal):
        # Set a new subtotal and update the final total
        self.__subtotal = subtotal
        self.__updateFinalTotal()

    def getDiscounts(self):
        """Return the total discounts applied."""
        return self.__discounts

    def setDiscounts(self, discounts):
        # Set a new discount amount and update the final total
        self.__discounts = discounts
        self.__updateFinalTotal()

    def getTaxes(self):
        """Return the calculated VAT amount."""
        return self.__taxes

    def setTaxes(self, taxes):
        # Set a new tax amount and update the final total
        self.__taxes = taxes
        self.__updateFinalTotal()

    def getFinalTotal(self):
        """Return the final total after VAT and discounts."""
        return self.__final_total

    def getInvoiceDate(self):
        """Return the invoice date."""
        return self.__invoice_date

    def setInvoiceDate(self, invoice_date):
        """Set a new invoice date."""
        self.__invoice_date = invoice_date

    # Update Final Total
    def __updateFinalTotal(self):
        # Recalculate the final total with updated subtotal, taxes, or discounts
        self.__final_total = self.__subtotal + self.__taxes - self.__discounts

    # Method to generate invoice summary
    def generateInvoice(self):
        """Return a summary of the invoice with date, subtotal, discounts, VAT, and final total."""
        return (f"Invoice Date: {self.__invoice_date}\nSubtotal: ${self.__subtotal:.2f}\n"
                f"Discounts: ${self.__discounts:.2f}\nVAT: ${self.__taxes:.2f}\n"
                f"Final Total: ${self.__final_total:.2f}")

    def __str__(self):
        # Return the generated invoice summary as a string
        return self.generateInvoice()

    def __str__(self):
        """Returns the invoice summary as a string."""
        return self.generateInvoice()
