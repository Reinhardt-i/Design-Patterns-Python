## The 10 Architectural Patterns

### Layers Pattern
- **Main Idea:** Organize the system into horizontal layers, where each layer provides a specific set of services to the layer above it.
- **Components:** Presentation Layer, Business Logic Layer, Data Access Layer.
- **Common Mistakes and Myths:**
  - Mistake: Violating the separation of concerns by allowing cross-layer dependencies.
  - Myth: Adding more layers always improves the system's performance and scalability.
- **Context:** Suitable for complex systems with multiple layers of functionality, where the separation of concerns and modular design are important.

### Client-Server Pattern
- **Main Idea:** Separate the system into clients and servers, where clients make requests to servers for resources or services.
- **Components:** Client, Server.
- **Common Mistakes and Myths:**
  - Mistake: Overloading the server with too many responsibilities and not properly distributing the workload.
  - Myth: The client always initiates the communication in a client-server architecture.
- **Context:** Suitable for distributed systems where there is a clear division of roles between clients and servers, and scalability and resource sharing are important.

### Master-Slave Pattern
- **Main Idea:** Delegate tasks to one or more master components that control and coordinate the work of multiple slave components.
- **Components:** Master, Slave.
- **Common Mistakes and Myths:**
  - Mistake: Creating a single point of failure by relying too much on the master component.
  - Myth: The slave components are passive and have no decision-making capabilities.
- **Context:** Suitable for systems with a hierarchical structure where a central master component manages and coordinates the activities of multiple slave components.

### Pipe-Filter Pattern
- **Main Idea:** Process data through a series of filters connected by pipes, where each filter performs a specific transformation or validation.
- **Components:** Pipes, Filters.
- **Common Mistakes and Myths:**
  - Mistake: Creating a complex and rigid pipeline that is difficult to modify or extend.
  - Myth: The filters should only perform simple transformations and not contain complex logic.
- **Context:** Suitable for systems that require modular data processing and transformation, where data flows through a series of independent filters.

### Broker Pattern
- **Main Idea:** Introduce a central broker component that handles communication and coordination between multiple distributed components.
- **Components:** Broker, Distributed Components.
- **Common Mistakes and Myths:**
  - Mistake: Overloading the broker with too many responsibilities, leading to a performance bottleneck.
  - Myth: The broker pattern is only suitable for message-based systems and not applicable to other communication mechanisms.
- **Context:** Suitable for distributed systems where components need to communicate and coordinate their activities through a central intermediary.

### Peer-to-Peer Pattern
- **Main Idea:** Enable decentralized communication and collaboration between equal peers without relying on a central authority.
- **Components:** Peers.
- **Common Mistakes and Myths:**
  - Mistake: Assuming all peers are equally capable and trustworthy, neglecting the need for proper security measures.
  - Myth: Peer-to-peer systems are only suitable for file sharing and not applicable to other domains.
- **Context:** Suitable for systems where distributed peers need to collaborate and share resources without a centralized control or single point of failure.

### Event-Bus Pattern
- **Main Idea:** Establish a communication mechanism through an event bus, where components can publish and subscribe to events.
- **Components:** Event Bus, Publishers, Subscribers.
- **Common Mistakes and Myths:**
  - Mistake: Creating a tightly coupled system by allowing direct communication between components instead of using the event bus.
  - Myth: The event-bus pattern is only applicable to event-driven systems and not suitable for other architectures.
- **Context:** Suitable for systems where loose coupling and decoupled communication between components are important, and where multiple components need to react to events.

### Model-View-Controller Pattern
- **Main Idea:** Separate the user interface (view) from the application logic (model) through an intermediary component (controller) that handles user input and updates the model and view accordingly.
- **Components:** Model, View, Controller.
- **Common Mistakes and Myths:**
  - Mistake: Overloading the controller with too much logic, violating the single responsibility principle.
  - Myth: The model-view-controller pattern is only applicable to graphical user interfaces (GUIs) and not suitable for other user interface paradigms.
- **Context:** Suitable for systems with user interfaces that require separation of concerns between the application logic and the presentation layer, enabling easier maintenance and extensibility.

### Blackboard Pattern
- **Main Idea:** Utilize a shared knowledge repository (blackboard) that multiple specialized components can read from and write to.
- **Components:** Blackboard, Knowledge Sources, Control Component.
- **Common Mistakes and Myths:**
  - Mistake: Allowing direct communication between knowledge sources, bypassing the blackboard and introducing coupling.
  - Myth: The blackboard pattern is only suitable for AI or expert systems and not applicable to other domains.

### Interpreter Pattern
- **Main Idea:** Define a language grammar and interpret the input expressions to perform specific actions or transformations.
- **Components:** Grammar, Expressions, Context.
- **Common Mistakes and Myths:**
  - Mistake: Creating a complex and rigid grammar that is difficult to maintain or extend.
  - Myth: The interpreter pattern is only applicable to programming languages and not suitable for other domain-specific languages.
