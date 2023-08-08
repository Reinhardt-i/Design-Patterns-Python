from abc import ABC, abstractmethod


class AuthenticationHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass


class UsernamePasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, username: str, password: str) -> bool:
        if username == "admin" and password == "admin123":
            print("UsernamePasswordAuthenticationHandler: Authentication successful.")
            return True
        elif self.next_handler is not None:
            return self.next_handler.authenticate(username, password)
        else:
            print("UsernamePasswordAuthenticationHandler: Authentication failed.")
            return False


class TwoFactorAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, username: str, password: str) -> bool:
        if username == "user" and password == "user123" and self.verify_otp("123456"):
            print("TwoFactorAuthenticationHandler: Authentication successful.")
            return True
        elif self.next_handler is not None:
            return self.next_handler.authenticate(username, password)
        else:
            print("TwoFactorAuthenticationHandler: Authentication failed.")
            return False

    @staticmethod
    def verify_otp(otp: str) -> bool:
        # Simulated OTP verification logic
        return otp == "123456"


class IPWhitelistingHandler(AuthenticationHandler):
    def authenticate(self, username: str, password: str) -> bool:
        client_ip = self.get_client_ip()
        if "192.168.192." not in client_ip:
            print("IPWhitelistingHandler: Authentication failed.")
            return False
        elif self.next_handler is not None:
            print("IPWhitelistingHandler: Authentication successful.")
            return self.next_handler.authenticate(username, password)
        else:
            print("IPWhitelistingHandler: Authentication failed.")
            return False

    @staticmethod
    def get_client_ip() -> str:
        # Simulated method to get client IP address
        return "192.168.192."


def main():
    up_handler = UsernamePasswordAuthenticationHandler()
    tfa_handler = TwoFactorAuthenticationHandler()
    ip_handler = IPWhitelistingHandler()

    ip_handler.set_next_handler(up_handler)
    up_handler.set_next_handler(tfa_handler)

    is_authenticated = ip_handler.authenticate("user", "user123")
    if is_authenticated:
        # Proceed with server access
        print("Access granted.")
    else:
        # Handle authentication failure
        print("Access denied.")


def print_chain_of_responsibility_description():
    print("""The Chain of Responsibility pattern is a behavioral design pattern that allows an object to pass a request along a
    chain of potential handlers until the request is handled or reaches the end of the chain. This pattern decouples
    senders and receivers of requests and provides a way to dynamically assign handlers without explicitly knowing
    which object will handle the request.

    In the provided code, we have implemented the Chain of Responsibility pattern for authentication handling. There are
    three concrete handler classes: UsernamePasswordAuthenticationHandler, TwoFactorAuthenticationHandler, and
    IPWhitelistingHandler. Each handler has a reference to the next handler in the chain.

    The AuthenticationHandler interface defines the common methods for the handlers, including set_next_handler and
    authenticate. Each handler implements the authenticate method, which performs the authentication logic specific to
    that handler. If the authentication is successful, it returns True; otherwise, it delegates the authentication to
    the next handler in the chain.

    In the Client class, we create instances of the handlers and set up the chain by calling set_next_handler to
    establish the order of handling. Finally, we call the authenticate method on the first handler in the chain to
    initiate the authentication process.

    By using the Chain of Responsibility pattern, we achieve flexibility and extensibility in handling authentication
    requests. Each handler in the chain can independently decide whether to handle the request or pass it to the next
    handler. This promotes separation of concerns and allows for easy modification or extension of the chain by adding
    or removing handlers. The pattern helps in keeping the code clean, modular, and easy to maintain.""")


if __name__ == "__main__":
    main()
    print_chain_of_responsibility_description()
