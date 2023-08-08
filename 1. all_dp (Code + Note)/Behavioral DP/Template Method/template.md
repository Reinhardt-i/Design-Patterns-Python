# Template Method Pattern Crash Course

## What is the Template Method Pattern?

The Template Method pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class but allows subclasses to provide certain steps of the algorithm implementation. It allows for the same algorithm to be reused with different variations in the steps.

## How to Identify the Template Method Pattern?

The Template Method pattern can be identified by the following characteristics:

1. The pattern involves defining an abstract base class that provides a template method.
2. The template method defines the overall algorithm structure by calling abstract methods or hook methods.
3. The abstract methods represent steps of the algorithm that must be implemented by concrete subclasses.
4. The concrete subclasses provide specific implementations for the abstract methods.
5. The template method orchestrates the execution of the algorithm by calling the abstract methods in the correct order.

## When to Use the Template Method Pattern?

Use the Template Method pattern when:

1. You have an algorithm that has a general structure but requires specific steps to be implemented differently.
2. You want to avoid code duplication by extracting common parts of an algorithm into a base class.
3. You want to allow clients to extend certain parts of the algorithm while keeping the overall structure intact.
4. You want to define a "template" for an algorithm and let subclasses provide specific implementations for certain steps.

## Intents and Components of the Template Method Pattern:

1. Intent:
   - Define the skeleton of an algorithm in a base class but allow subclasses to provide specific implementations of certain steps.

2. Components:
   - Abstract Class: Represents the base class that defines the template method and abstract methods or hook methods.
   - Concrete Class: Extends the abstract class and provides concrete implementations for the abstract methods.
   - Template Method: Defines the overall algorithm structure and calls the abstract methods or hook methods.
   - Abstract Methods/Hook Methods: Represent the steps of the algorithm that must be implemented by subclasses.

## How to Implement the Template Method Pattern?

To implement the Template Method pattern, follow these steps:

1. Identify the algorithm that has a common structure but requires variations in certain steps.
2. Design an abstract base class that provides a template method. The template method should define the overall algorithm structure and call abstract methods or hook methods.
3. Declare abstract methods or hook methods in the abstract base class. These methods represent the steps of the algorithm that must be implemented by subclasses.
4. Implement concrete subclasses that extend the abstract base class. Each subclass should provide specific implementations for the abstract methods.
5. The template method in the abstract base class should orchestrate the execution of the algorithm by calling the abstract methods or hook methods in the correct order.
6. Clients should interact with the concrete subclasses, which provide variations in the algorithm's implementation while adhering to the template method defined in the base class.

Remember, the key idea behind the Template Method pattern is to define the overall algorithm structure in a base class but allow subclasses to provide specific implementations for certain steps.

