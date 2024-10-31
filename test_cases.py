from datetime import date
from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from discount import Discount

# Test 1: EBook creation and attribute access
def test_ebook():
    ebook = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    assert ebook.getTitle() == "Python 101"
    assert ebook.getAuthor() == "John Doe"
    assert ebook.getPrice() == 29.99
    print("Test 1 Passed: EBook creation and attribute access")

# Test 2: Customer creation and loyalty membership
def test_customer():
    customer = Customer("Alice Smith", "alice@example.com", True)
    assert customer.getName() == "Alice Smith"
    assert customer.isLoyaltyMember() == True
    print("Test 2 Passed: Customer creation and loyalty membership")

# Test 3: Add and remove items in ShoppingCart
def test_shopping_cart():
    cart = ShoppingCart()
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    assert len(cart.cart_items) == 2
    cart.removeItem(ebook1)
    assert len(cart.cart_items) == 1
    print("Test 3 Passed: Add and remove items in ShoppingCart")

# Test 4: Calculate total price in ShoppingCart
def test_shopping_cart_total():
    cart = ShoppingCart()
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    assert cart.getTotalPrice() == 74.99
    print("Test 4 Passed: Calculate total price in ShoppingCart")

# Test 5: Create Order and apply discount
def test_order_total_with_discount():
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    order = Order(date.today(), [ebook1, ebook2])
    discount = Discount()
    discount.applyLoyaltyDiscount(order)
    
    assert order.getTotalPrice() < (ebook1.getPrice() + ebook2.getPrice())  # Check discount was applied
    print("Test 5 Passed: Order creation and discount application")

# Test 6: Generate Invoice
def test_invoice_generation():
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    order = Order(date.today(), [ebook1, ebook2])
    discount = Discount()
    discount.applyLoyaltyDiscount(order)
    
    invoice = Invoice(order)
    assert invoice.final_total > 0
    print(invoice)
    print("Test 6 Passed: Invoice generation")

# Run all test cases
if __name__ == "__main__":
    test_ebook()
    test_customer()
    test_shopping_cart()
    test_shopping_cart_total()
    test_order_total_with_discount()
    test_invoice_generation()
