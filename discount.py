class Discount:
    @staticmethod
    def applyLoyaltyDiscount(order):
        discount = order.getTotalPrice() * 0.10  # 10% discount for loyalty members
        order.applyDiscount(discount)
        return discount

    @staticmethod
    def applyBulkDiscount(order):
        discount = order.getTotalPrice() * 0.20  # 20% discount for 5 or more items
        order.applyDiscount(discount)
        return discount
