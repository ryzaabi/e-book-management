from datetime import date
from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from discount import Discount

# Test 1: EBook creation and attribute access
def test_ebook():
    # Create an EBook instance and check its attributes
    ebook = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    # Assert that the title, author, and price are correctly stored
    assert ebook.getTitle() == "Python 101"
    assert ebook.getAuthor() == "John Doe"
    assert ebook.getPrice() == 29.99
    print("Test 1 Passed: EBook creation and attribute access")

# Test 2: Customer creation and loyalty membership
def test_customer():
    # Create a Customer instance and check if loyalty status is set correctly
    customer = Customer("Alice Smith", "alice@example.com", True)
    # Assert that the customer name and loyalty status are correct
    assert customer.getName() == "Alice Smith"
    assert customer.isLoyaltyMember() == True
    print("Test 2 Passed: Customer creation and loyalty membership")

# Test 3: Add and remove items in ShoppingCart
def test_shopping_cart():
    # Create a ShoppingCart instance and add two eBooks to it
    cart = ShoppingCart()
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    # Assert that two items were added to the cart
    assert len(cart.cart_items) == 2
    # Remove one item and check that the cart now has one item
    cart.removeItem(ebook1)
    assert len(cart.cart_items) == 1
    print("Test 3 Passed: Add and remove items in ShoppingCart")

# Test 4: Calculate total price in ShoppingCart
def test_shopping_cart_total():
    # Create a ShoppingCart instance and add two eBooks to calculate total
    cart = ShoppingCart()
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    # Assert that the total price of items in the cart is as expected
    assert cart.getTotalPrice() == 74.99
    print("Test 4 Passed: Calculate total price in ShoppingCart")

# Test 5: Create Order and apply discount
def test_order_total_with_discount():
    # Create an Order instance with two eBooks and apply a loyalty discount
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    order = Order(date.today(), [ebook1, ebook2])
    discount = Discount()
    discount.applyLoyaltyDiscount(order)
    
    # Assert that the discount was applied, reducing the total price
    assert order.getTotalPrice() < (ebook1.getPrice() + ebook2.getPrice())  
    print("Test 5 Passed: Order creation and discount application")

# Test 6: Generate Invoice
def test_invoice_generation():
    # Create an Order with two eBooks, apply discount, and generate an invoice
    ebook1 = EBook("Python 101", "John Doe", date(2020, 1, 1), "Education", 29.99)
    ebook2 = EBook("Learning AI", "Jane Smith", date(2021, 5, 17), "Technology", 45.00)
    order = Order(date.today(), [ebook1, ebook2])
    discount = Discount()
    discount.applyLoyaltyDiscount(order)
    
    # Create an Invoice for the order and check if it has a valid total
    invoice = Invoice(order)
    assert invoice.final_total > 0
    print(invoice)
    print("Test 6 Passed: Invoice generation")

# Run all test cases
if __name__ == "__main__":
    test_ebook()                # Run EBook test
    test_customer()             # Run Customer test
    test_shopping_cart()        # Run ShoppingCart add/remove test
    test_shopping_cart_total()  # Run ShoppingCart total price test
    test_order_total_with_discount()  # Run Order discount test
    test_invoice_generation()    # Run Invoice generation test

