"""
Scenario: Online Shopping System
This codebase demonstrates an online shopping system with a focus on maintaining the SOLID principles. 

The system consists of three main classes: Order, PaymentProcessor, and NotificationService. 
It allows users to place orders, process payments, and receive notifications for successful orders.

1. Order: Represents an order containing multiple products. It follows the SRP by having a single responsibility
        of managing order-related operations, such as calculating the total amount and generating an invoice.

2. PaymentProcessor: Handles payment processing for different payment methods. It adheres to the OCP by being open 
        for extension to support various payment methods without modifying existing code. New payment methods 
        can be added as separate classes implementing a common interface.

3. NotificationService: Represents a notification service responsible for sending notifications to customers. 
        The ISP is applied by using an interface (NotificationServiceInterface) that clients can choose to 
        implement only the methods they need.

4. DiscountedOrder: Inherits from the Order class to represent an order with promotions and discounts. It maintains 
        the LSP as it can be substituted for its base class (Order) without altering the correctness of the program.

5. OrderProcessor: A client class that depends on abstractions, adhering to the DIP. It takes instances of Order,
        PaymentProcessor, and NotificationService as dependencies and processes an order by utilizing these abstractions.

"""


# Order class responsible for handling order-related operations
class Order:
    def __init__(self, order_id, items, total_amount):
        self.order_id = order_id
        self.items = items
        self.total_amount = total_amount

    def calculate_total_amount(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def generate_invoice(self):
        invoice = f"Invoice for Order {self.order_id}\n"
        for item in self.items:
            invoice += f"{item.name}: {item.price} x {item.quantity}\n"
        invoice += f"Total Amount: {self.total_amount}\n"
        return invoice


# Product class representing the items in an order
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# OCP : Classes should be open for extension but closed for modification. (Demonstarted here)

# PaymentProcessor class responsible for handling different payment methods
class PaymentProcessor:
    def process_payment(self, order):
        # This method is closed for modification (no changes needed)
        total_amount = order.calculate_total_amount()
        # Here, we can add different payment methods without modifying the existing code
        # For example, add PayPal, Credit Card, or Stripe payment methods here.
        # Each new payment method can be implemented as a separate class implementing a common interface.
        # The PaymentProcessor class is open for extension to support new payment methods.


# ISP : Clients should not be forced to implement interfaces they do not use. (Demonstarted here)

# Interface for notification service
class NotificationServiceInterface:
    def send_notification(self, message):
        pass


# EmailNotificationService implementing the notification interface
class EmailNotificationService(NotificationServiceInterface):
    def send_notification(self, message):
        # Logic to send email notification
        print(f"Sending email notification: {message}")


# SMSNotificationService implementing the notification interface
class SMSNotificationService(NotificationServiceInterface):
    def send_notification(self, message):
        # Logic to send SMS notification
        print(f"Sending SMS notification: {message}")


# LSP: Subclasses should be substitutable for their base classes. (Demonstarted here)

# Subclass of Order that supports promotions and discounts
class DiscountedOrder(Order):
    def __init__(self, order_id, items, total_amount, discount):
        super().__init__(order_id, items, total_amount)
        self.discount = discount

    def calculate_total_amount(self):
        # Calculate the total amount for the discounted order
        total = super().calculate_total_amount()
        total -= self.discount
        return total


# DIP: Depend upon abstractions, not concretions. (Demonstarted here)

# Client class that depends on abstractions
class OrderProcessor:
    def __init__(self, order, payment_processor, notification_service):
        self.order = order
        self.payment_processor = payment_processor
        self.notification_service = notification_service

    def process_order(self):
        # Process the payment using the payment processor
        self.payment_processor.process_payment(self.order)

        # Generate and send the invoice using the notification service
        invoice = self.order.generate_invoice()
        self.notification_service.send_notification(invoice)


if __name__ == "__main__":
    # Sample order with two products
    order_id = 1
    items = [Product("Item 1", 100, 2), Product("Item 2", 50, 3)]
    total_amount = 250

    # Create instances of classes
    order = Order(order_id, items, total_amount)
    payment_processor = PaymentProcessor()
    email_notification_service = EmailNotificationService()

    # Process the order using the OrderProcessor class
    order_processor = OrderProcessor(order, payment_processor, email_notification_service)
    order_processor.process_order()

