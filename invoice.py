class Invoice:
    """Generates an invoice for an order, including VAT and discounts."""

    VAT_RATE = 0.08

    def __init__(self, order, invoice_date):
        self.__subtotal = order.getTotalPrice()
        self.__discounts = order.getDiscountApplied()
        self.__taxes = self.__subtotal * self.VAT_RATE
        self.__final_total = self.__subtotal + self.__taxes
        self.__invoice_date = invoice_date

    # Getters and Setters
    def getSubtotal(self):
        return self.__subtotal

    def setSubtotal(self, subtotal):
        self.__subtotal = subtotal
        self.__updateFinalTotal()

    def getDiscounts(self):
        return self.__discounts

    def setDiscounts(self, discounts):
        self.__discounts = discounts
        self.__updateFinalTotal()

    def getTaxes(self):
        return self.__taxes

    def setTaxes(self, taxes):
        self.__taxes = taxes
        self.__updateFinalTotal()

    def getFinalTotal(self):
        return self.__final_total

    def getInvoiceDate(self):
        return self.__invoice_date

    def setInvoiceDate(self, invoice_date):
        self.__invoice_date = invoice_date

    # Update Final Total
    def __updateFinalTotal(self):
        self.__final_total = self.__subtotal - self.__discounts + self.__taxes

    # Method to generate invoice summary
    def generateInvoice(self):
        return (f"Invoice Date: {self.__invoice_date}\nSubtotal: ${self.__subtotal:.2f}\n"
                f"Discounts: ${self.__discounts:.2f}\nVAT: ${self.__taxes:.2f}\n"
                f"Final Total: ${self.__final_total:.2f}")

    def __str__(self):
        return self.generateInvoice()
