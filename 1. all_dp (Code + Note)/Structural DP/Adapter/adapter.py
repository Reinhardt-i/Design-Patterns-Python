from abc import ABC, abstractmethod
import json

"""
Adapter Pattern Example: JSON, XML, and Proto Data Conversion

Scenario:
This example demonstrates the Adapter pattern used to convert data between three different formats: JSON, XML, and Proto.
We have separate classes to represent each data format, but we want to provide a uniform interface for data conversion,
allowing clients to switch between formats seamlessly.

Implementation:
The Adapter pattern is applied by creating adapter classes that implement a common interface (`Adapter`) for data
conversion. Each adapter class handles the conversion logic between a specific pair of formats (e.g., JSON to XML,
XML to JSON, Proto to XML). The `Client` class utilizes the adapter to convert data without knowledge of the underlying
conversion logic.

Usage:
1. Create instances of JSON, XML, or Proto data classes.
2. Instantiate the corresponding adapter classes (JsonToXmlAdapter, XmlToJsonAdapter, ProtoToXmlAdapter).
3. Initialize the `Client` class with the desired adapter.
4. Use the `Client` to convert data between different formats using the adapter.

Note:
In this example, the Proto to XML and XML to JSON conversion logic is the same. In a real-world scenario, different
conversion logic may exist, and the Adapter pattern would help encapsulate these details, promoting code flexibility
and maintainability.
"""



# Base adapter class implementing the common conversion logic
class Adapter(ABC):
    @abstractmethod
    def convert(self, data):
        """
        Abstract method for converting data.
        """
        pass
    
    
# JSON class representing a JSON object
class JSON:
    def __init__(self, data: str = "") -> None:
        self.data = data

    def __str__(self):
        return self.data


# XML class representing an XML object
class XML:
    def __init__(self, data: str = "") -> None:
        self.data = data

    def __str__(self):
        return self.data


# Proto class representing a Proto object
class Proto:
    def __init__(self, data: str = "") -> None:
        self.data = data

    def __str__(self):
        return self.data


# Adapter class to convert JSON to XML
class JsonToXmlAdapter(Adapter):
    def convert(self, data: JSON) -> XML:
        """
        Converts JSON data to XML format using a specific conversion logic.
        """
        xml_data = "<xml>{}</xml>".format(data)
        return XML(xml_data)


# Adapter class to convert XML to JSON
class XmlToJsonAdapter(Adapter):
    def convert(self, data: XML) -> JSON:
        """
        Converts XML data to JSON format using a specific conversion logic.
        """
        # Logic to convert XML data to JSON
        json_data = json.dumps({"xml_data": str(data)})
        return JSON(json_data)


# Adapter class to convert Proto to XML
class ProtoToXmlAdapter(Adapter):
    def convert(self, data: Proto) -> XML:
        """
        Converts Proto data to XML format using a specific conversion logic.
        """
        # Logic to convert Proto data to XML
        xml_data = "<xml>{}</xml>".format(data)
        return XML(xml_data)


# Client class utilizing the adapter pattern
class Client:
    def __init__(self, adapter: Adapter) -> None:
        """
        Initializes the client with a specific adapter.
        """
        self.adapter = adapter

    def convert(self, data) -> object:
        """
        Uses the adapter to convert data based on the adapter type.
        """
        return self.adapter.convert(data)


if __name__ == '__main__':
    # Usage
    json_to_xml_adapter = JsonToXmlAdapter()
    client1 = Client(json_to_xml_adapter)
    json_data = JSON('{"key": "value"}')
    xml_data = client1.convert(json_data)
    print("JSON to XML Data:", xml_data)

    xml_to_json_adapter = XmlToJsonAdapter()
    client2 = Client(xml_to_json_adapter)
    xml_data = XML('<xml><key>value</key></xml>')
    json_data = client2.convert(xml_data)
    print("XML to JSON Data:", json_data)

    proto_to_xml_adapter = ProtoToXmlAdapter()
    client3 = Client(proto_to_xml_adapter)
    proto_data = Proto('proto-data')
    xml_data = client3.convert(proto_data)
    print("Proto to XML Data:", xml_data)
