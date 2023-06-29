# Design-Patterns-Python
Repo for SWE 321/322 (Software Architecture and Design Pattern) notes.


### A high-level overview of the 15 design patterns. For more clarity, check the folders, each pattern has their own separate notes.

## Creational Patterns

### Singleton Pattern

- **Description**: Ensures that only one instance of a class is created and provides a global point of access to it.
- **Components**: Singleton class, `getInstance()` method.
- **Composite Usage**: Can be used in combination with other patterns, such as Factory Method or Abstract Factory.
- **Common Mistakes and Myths**: Overusing singletons can lead to tight coupling and make testing and dependency management difficult.

### Factory Method Pattern

- **Description**: Defines an interface for creating objects but allows subclasses to decide which class to instantiate.
- **Components**: Creator, ConcreteCreator, Product, ConcreteProduct.
- **Composite Usage**: Can be used in combination with other patterns, such as Abstract Factory.
- **Common Mistakes and Myths**: Overcomplicating the factory hierarchy or not adhering to the Open-Closed Principle.

### Abstract Factory Pattern

- **Description**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- **Components**: AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct.
- **Composite Usage**: Can be used in combination with other patterns, such as Factory Method.
- **Common Mistakes and Myths**: Overcomplicating the abstract factory hierarchy or violating the Single Responsibility Principle.

### Builder Pattern

- **Description**: Separates the construction of complex objects from their representation, allowing the same construction process to create different representations.
- **Components**: Builder, ConcreteBuilder, Director, Product.
- **Composite Usage**: Can be used in combination with other patterns, such as Abstract Factory or Singleton.
- **Common Mistakes and Myths**: Overcomplicating the builder implementation or not following the Liskov Substitution Principle.

### Prototype Pattern

- **Description**: Creates objects by cloning an existing object, thereby avoiding the need for explicit class instantiation.
- **Components**: Prototype, ConcretePrototype.
- **Composite Usage**: Can be used in combination with other patterns, such as Registry or Factory Method.
- **Common Mistakes and Myths**: Ignoring the shallow or deep cloning requirements or not properly handling the copying process.

## Structural Patterns

### Adapter Pattern

- **Description**: Converts the interface of a class into another interface that clients expect, enabling classes to work together that couldn't otherwise due to incompatible interfaces.
- **Components**: Target, Adapter, Adaptee.
- **Composite Usage**: Can be used in combination with other patterns, such as Decorator or Facade.
- **Common Mistakes and Myths**: Overusing adapters when a simpler solution is available or not considering the trade-offs of interface compatibility.

### Bridge Pattern

- **Description**: Separates an abstraction from its implementation, allowing them to vary independently.
- **Components**: Abstraction, RefinedAbstraction, Implementor, ConcreteImplementor.
- **Composite Usage**: Can be used in combination with other patterns, such as Adapter or Composite.
- **Common Mistakes and Myths**: Overcomplicating the bridge hierarchy or failing to identify the proper separation between abstraction and implementation.

### Composite Pattern

- **Description**: Treats individual objects and compositions of objects uniformly, allowing clients to manipulate them in a unified manner.
- **Components**: Component, Leaf, Composite.
- **Composite Usage**: Often used in combination with other patterns, such as Iterator or Visitor.
- **Common Mistakes and Myths**: Overusing the composite pattern when a simpler structure is sufficient or not handling leaf and composite objects uniformly.

### Decorator Pattern

- **Description**: Dynamically adds new behavior to an object by wrapping it with one or more decorator objects.
- **Components**: Component, ConcreteComponent, Decorator, ConcreteDecorator.
- **Composite Usage**: Can be used in combination with other patterns, such as Adapter or Composite.
- **Common Mistakes and Myths**: Overcomplicating the decorator hierarchy or not understanding the impact on object behavior and interfaces.

### Facade Pattern

- **Description**: Provides a simplified interface to a complex subsystem, making it easier to use and decoupling clients from the subsystem's implementation details.
- **Components**: Facade, Subsystem classes.
- **Composite Usage**: Can be used in combination with other patterns, such as Adapter or Mediator.
- **Common Mistakes and Myths**: Creating a facade that exposes too much or not properly encapsulating the subsystem.

## Behavioral Patterns

### Chain of Responsibility Pattern

- **Description**: Allows multiple objects to handle a request one after another until it is processed by an object that can handle it.
- **Components**: Handler, ConcreteHandler, Client.
- **Composite Usage**: Can be used in combination with other patterns, such as Command or Observer.
- **Common Mistakes and Myths**: Overcomplicating the chain or not ensuring that requests are eventually handled.

### Observer Pattern

- **Description**: Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.
- **Components**: Subject, Observer, ConcreteSubject, ConcreteObserver.
- **Composite Usage**: Can be used in combination with other patterns, such as Mediator or Strategy.
- **Common Mistakes and Myths**: Overusing observers, leading to performance issues or not properly managing dependencies.

### Visitor Pattern

- **Description**: Defines a new operation to be performed on elements of an object structure without changing the classes of the elements.
- **Components**: Visitor, ConcreteVisitor, Element, ConcreteElement, Object Structure.
- **Composite Usage**: Can be used in combination with other patterns, such as Composite or Iterator.
- **Common Mistakes and Myths**: Overcomplicating the visitor hierarchy or violating the Single Responsibility Principle.

### Command Pattern

- **Description**: Encapsulates a request as an object, thereby allowing parameterization of clients with different requests, queue or log requests, and support undoable operations.
- **Components**: Command, ConcreteCommand, Invoker, Receiver.
- **Composite Usage**: Can be used in combination with other patterns, such as Composite or Observer.
- **Common Mistakes and Myths**: Overcomplicating the command hierarchy or not properly decoupling senders and receivers.

## Causion

1. Overusing design patterns: It's essential to use design patterns judiciously. Not every problem requires a design pattern, and using them unnecessarily can lead to overcomplication.

2. Ignoring the context: Design patterns are not silver bullets. They need to be applied considering the specific context and requirements of the problem at hand.

3. Forcing a pattern: Trying to fit a problem into a particular design pattern, even if it doesn't naturally align, can lead to convoluted and less maintainable code.

4. Lack of flexibility: Design patterns should be flexible and adaptable. Avoid rigid implementations that make it challenging to modify or extend the codebase.

5. Not documenting the intent: It's crucial to document and communicate the intent of using a design pattern to ensure a clear understanding among team members.

Remember, design patterns are tools to help solve recurring design problems, but they should be used wisely, considering the specific context and requirements of the project.
