class Invoice:
    VAT_RATE = 0.08

    def __init__(self, order):
        self.subtotal = order.getTotalPrice()
        self.discounts = order._Order__discount_applied
        self.taxes = self.subtotal * self.VAT_RATE
        self.final_total = self.subtotal + self.taxes

    def generateInvoice(self):
        return (f"Invoice:\nSubtotal: ${self.subtotal:.2f}\nDiscounts: ${self.discounts:.2f}\n"
                f"VAT: ${self.taxes:.2f}\nFinal Total: ${self.final_total:.2f}")

    def __str__(self):
        return self.generateInvoice()
