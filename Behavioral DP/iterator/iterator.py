from typing import TypeVar, Generic, Optional

T = TypeVar('T')  # Type variable for the element type


class MyList(Generic[T]):
    """
    MyList represents a custom list implementation.
    """

    class Node(Generic[T]):
        """
        Node represents a node in the list.
        """

        def __init__(self, data: T):
            self.data: T = data
            self.next: Optional[MyList.Node[T]] = None

    def __init__(self):
        self.head: Optional[MyList.Node[T]] = None
        self.tail: Optional[MyList.Node[T]] = None

    def add(self, data: T):
        """
        Adds an element to the list.
        """
        new_node = MyList.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def iterator(self) -> 'MyIterator[T]':
        """
        Returns an iterator for the list.
        """
        return self.MyListIterator(self.head)

    class MyListIterator(Generic[T]):
        """
        MyListIterator represents an iterator for the list.
        """

        def __init__(self, node: Optional[MyList.Node[T]]):
            self.current_node: Optional[MyList.Node[T]] = node

        def __iter__(self):
            return self

        def __next__(self) -> T:
            """
            Returns the next element in the iteration.
            Raises StopIteration if there are no more elements.
            """
            if self.current_node is None:
                raise StopIteration
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data


if __name__ == '__main__':
    # Example usage
    my_list = MyList[int]()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)

    my_iterator = my_list.iterator()
    for item in my_iterator:
        print(item)
        