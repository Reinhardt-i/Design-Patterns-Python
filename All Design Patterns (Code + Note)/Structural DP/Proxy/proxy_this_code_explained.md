In the provided code, we have an example of the Proxy pattern, which is used to control access to the internet. The code consists of three main classes: Internet, RealInternet, and ProxyInternet.

The Internet interface defines the connect_to method, which represents connecting to a server host.

The RealInternet class implements the Internet interface and represents the real internet connection. When the connect_to method is called on an instance of RealInternet, it simply connects to the specified server host.

The ProxyInternet class also implements the Internet interface and acts as a proxy for the internet connection. It internally holds an instance of RealInternet to handle the actual connection. The ProxyInternet class maintains a list of restricted sites, which are sites that the user is not allowed to access.

When the connect_to method is called on an instance of ProxyInternet, it first checks if the server host is in the list of restricted sites. If it is, it displays a message indicating that access is restricted. Otherwise, it delegates the connection to the RealInternet instance and connects to the specified server host.

In the main function, we create an instance of ProxyInternet and use it to connect to different server hosts. We can see that when connecting to a regular site like "google.com", it connects successfully. However, when attempting to connect to a restricted site like "blocked-site.com", it displays a message indicating that access is restricted.

The Proxy pattern allows us to control access to an object by providing a proxy object that acts as an intermediary. It can add additional behavior, such as access restrictions, without modifying the original object's code.




