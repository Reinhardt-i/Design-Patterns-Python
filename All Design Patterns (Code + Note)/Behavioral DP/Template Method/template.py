from abc import ABC, abstractmethod


class FileProcessor(ABC):
    """
    FileProcessor is an abstract base class that defines the template method and the required steps for processing a file.
    """

    def process_file(self, file_path: str) -> None:
        """
        Template method that processes the file by executing the predefined sequence of steps.
        """
        self.open_file(file_path)
        self.extract_content()
        self.parse_content()
        self.close_file()

    @abstractmethod
    def extract_content(self) -> None:
        """
        Abstract method to extract the content from the file.
        """
        pass

    @abstractmethod
    def parse_content(self) -> None:
        """
        Abstract method to parse the content of the file.
        """
        pass

    @staticmethod
    def open_file(file_path: str) -> None:
        """
        Default method to open the file.
        """
        print("Opening file:", file_path)

    @staticmethod
    def close_file() -> None:
        """
        Default method to close the file.
        """
        print("Closing file")


class PDFFileProcessor(FileProcessor):
    """
    Concrete subclass of FileProcessor for processing PDF files.
    """

    def extract_content(self) -> None:
        print("Extracting content from PDF file")

    def parse_content(self) -> None:
        print("Parsing content of PDF file")


class DOCFileProcessor(FileProcessor):
    """
    Concrete subclass of FileProcessor for processing DOC files.
    """

    def extract_content(self) -> None:
        print("Extracting content from DOC file")

    def parse_content(self) -> None:
        print("Parsing content of DOC file")


class TextFileProcessor(FileProcessor):
    """
    Concrete subclass of FileProcessor for processing text files.
    """

    def extract_content(self) -> None:
        print("Extracting content from text file")

    def parse_content(self) -> None:
        print("Parsing content of text file")


if __name__ == '__main__':
    pdf_file_processor = PDFFileProcessor()
    pdf_file_processor.process_file("sample.pdf")
    print()

    doc_file_processor = DOCFileProcessor()
    doc_file_processor.process_file("sample.doc")
    print()

    text_file_processor = TextFileProcessor()
    text_file_processor.process_file("sample.txt")
    