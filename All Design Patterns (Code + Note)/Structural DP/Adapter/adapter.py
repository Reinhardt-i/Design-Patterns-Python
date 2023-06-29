from abc import ABC, abstractmethod
import json


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
    print("XML Data:", xml_data)
    
    xml_to_json_adapter = XmlToJsonAdapter()
    client2 = Client(xml_to_json_adapter)
    xml_data = XML('<xml><key>value</key></xml>')
    json_data = client2.convert(xml_data)
    print("JSON Data:", json_data)
    