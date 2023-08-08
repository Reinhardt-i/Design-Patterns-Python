## Iterators

Iterators in Python provide a way to traverse through a collection of elements one by one. They are composed of two main components: iterable and iterator.

**1. Iterable:**
An iterable is any object that can be looped over using a loop construct, such as a `for` loop. Examples of built-in iterables in Python include lists, tuples, strings, dictionaries, and sets.

**2. Iterator:**
An iterator is an object that implements the iterator protocol, which consists of two methods: `__iter__()` and `__next__()`.
- The `__iter__()` method returns the iterator object itself and is responsible for initializing or resetting the iterator.
- The `__next__()` method returns the next element in the iteration. If there are no more elements, it raises the `StopIteration` exception.

To create your own iterator, you need to define a class that implements these two methods.

Iterators are used to efficiently process elements in a collection one at a time. They provide a consistent way to access and iterate over elements, regardless of the underlying data structure.

Understanding iterators is crucial for elegant and efficient iteration over various data structures in Python. They are widely used and provide a powerful mechanism for working with collections in a sequential manner.
