class Discount:
    @staticmethod
    def applyLoyaltyDiscount(order):
        #Applies a 10% loyalty discount to the Order
        discount = order.getTotalPrice() * 0.10  # 10% discount for loyalty members
        order.applyDiscount(discount)
        return discount

    @staticmethod
    def applyBulkDiscount(order):
        #Applies a 20% discount for bulk purchases (5 or more items)
        discount = order.getTotalPrice() * 0.20 # 20% discount for 5 or more items
        order.applyDiscount(discount)
        return discount
