from abc import ABC, abstractmethod

# Abstraction
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Low-level module
class PaypalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using PayPal.")

# Low-level module
class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Stripe.")

# High-level module
class PaymentService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
    
    def process_payment(self, amount):
        self.payment_processor.process_payment(amount)

# Client code
paypal_processor = PaypalPaymentProcessor()
payment_service = PaymentService(paypal_processor)
payment_service.process_payment(100)

stripe_processor = StripePaymentProcessor()
payment_service = PaymentService(stripe_processor)
payment_service.process_payment(200)