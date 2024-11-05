from datetime import date
from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from discount import Discount

def test_system():
    # Test eBook Creation
    ebook1 = EBook("Python Programming", "Yousif Alzaabi", date(2021, 1, 1), "Education", 30.00)
    ebook2 = EBook("Data Science", "Mohammed Alzaabi", date(2021, 5, 1), "Technology", 45.00)
    print(f"Test eBook Creation: {ebook1}, {ebook2}")

    # Test Customer Creation
    customer = Customer("Rashed Alzaabi", "rashed@example.com", True, date(2020, 1, 1))
    print(f"Test Customer Creation: {customer}")

    # Test Shopping Cart
    cart = ShoppingCart(customer, date.today())
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    print(f"Test Shopping Cart: {cart}, Total: ${cart.getTotalPrice()}")

    # Test Order and Discount
    order = Order("ORD123", date.today(), cart.getCartItems())
    discount = Discount()
    loyalty_discount = discount.applyLoyaltyDiscount(order)
    bulk_discount = discount.applyBulkDiscount(order)
    print(f"Test Order: Order Total after Loyalty Discount: ${order.getTotalPrice():.2f}")

    # Test Invoice Generation
    invoice = Invoice(order, date.today())
    print("Generated Invoice:\n", invoice.generateInvoice())

if __name__ == "__main__":
    test_system()
