from typing import List


class Internet:
    """
    Internet interface that defines the connectTo method.
    """

    def connect_to(self, server_host: str) -> None:
        """
        Connects to the specified server host.
        """
        pass


class RealInternet(Internet):
    """
    RealInternet represents the real internet connection.
    """

    def connect_to(self, server_host: str) -> None:
        print("Connecting to:", server_host)


class ProxyInternet(Internet):
    """
    ProxyInternet represents the proxy for internet connection.
    """

    def __init__(self):
        self.real_internet = RealInternet()
        self.restricted_sites = ["blocked-site.com", "restricted-site.com"]

    def connect_to(self, server_host: str) -> None:
        if server_host in self.restricted_sites:
            print("Access to", server_host, "is restricted.")
        else:
            self.real_internet.connect_to(server_host)


if __name__ == '__main__':
    internet = ProxyInternet()

    internet.connect_to("google.com")
    # Output: Connecting to: google.com

    internet.connect_to("blocked-site.com")
    # Output: Access to blocked-site.com is restricted.

    internet.connect_to("open-site.com")
    # Output: Connecting to: open-site.com
    