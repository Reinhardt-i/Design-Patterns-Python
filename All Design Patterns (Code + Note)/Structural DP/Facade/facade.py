class BankAccount:
    """
    BankAccount represents a bank account with deposit, withdrawal, and balance functionalities.
    """

    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.
        """
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account if the balance is sufficient.
        """
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount} from account {self.account_number}")
        else:
            print(f"Insufficient balance in account {self.account_number}")

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.
        """
        return self.balance


class CreditCardProcessor:
    """
    CreditCardProcessor represents a credit card processor for processing payments.
    """

    def process_payment(self, credit_card_number: str, amount: float) -> None:
        """
        Processes the payment using the specified credit card number and amount.
        """
        print(f"Processing payment of ${amount} using Credit Card: {credit_card_number}")
        # Credit card processing logic...


class EmailService:
    """
    EmailService represents an email service for sending emails.
    """

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient with the given subject and body.
        """
        print(f"Sending email to: {recipient}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # Email sending logic...


class BankingFacade:
    """
    BankingFacade provides a simplified interface for banking operations.
    """

    def __init__(self, account_number: int, balance: float):
        self.bank_account = BankAccount(account_number, balance)
        self.card_processor = CreditCardProcessor()
        self.email_service = EmailService()

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account and sends a deposit notification email.
        """
        self.bank_account.deposit(amount)
        self.email_service.send_email(
            "customer@example.com",
            "Deposit Notification",
            f"You have deposited ${amount} into your account."
        )

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account and sends a withdrawal notification email.
        """
        self.bank_account.withdraw(amount)
        self.email_service.send_email(
            "customer@example.com",
            "Withdrawal Notification",
            f"You have withdrawn ${amount} from your account."
        )

    def make_payment_with_credit_card(self, credit_card_number: str, amount: float) -> None:
        """
        Processes a payment using the specified credit card and sends a payment confirmation email.
        """
        self.card_processor.process_payment(credit_card_number, amount)
        self.email_service.send_email(
            "customer@example.com",
            "Payment Confirmation",
            f"Your payment of ${amount} has been processed using Credit Card: {credit_card_number}"
        )

    def get_account_balance(self) -> float:
        """
        Returns the current balance of the bank account.
        """
        return self.bank_account.get_balance()


if __name__ == '__main__':
    banking_facade = BankingFacade(123456789, 1000.0)
    banking_facade.deposit(500.0)
    banking_facade.withdraw(200.0)
    banking_facade.make_payment_with_credit_card("1234 5678 9012 3456", 100.0)

    account_balance = banking_facade.get_account_balance()
    print(f"Current Account Balance: ${account_balance}")
    