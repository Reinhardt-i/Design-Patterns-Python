# Questions and Answers on Architectural Patterns

## a. Tactic Examples in Architectural Patterns

**Q: In a previous learning unit, we introduced the name tactic for an architectural decision that influences the quality of the product. Architectural patterns can be viewed as being constructed from tactics. Can you give some examples?**

A: Certainly! Tactics are specific design decisions that impact the quality attributes of a software system. Here are a few examples of tactics commonly used in architectural patterns:

- Caching: Storing frequently accessed data in a cache to improve performance.
- Load Balancing: Distributing workload across multiple resources to enhance scalability and resource utilization.
- Replication: Creating redundant copies of components or data for improved reliability and fault tolerance.
- Encryption: Applying cryptographic algorithms to secure sensitive data for confidentiality and integrity.
- Failover: Switching to backup or redundant components in case of failure to ensure high availability.

## b. Preventing Divergence from Patterns

**Q: Once a pattern has been used in an architectural design, the reason for its use may be forgotten, and over time the design may start to diverge from the pattern. Do you think this should be prevented? If so, how?**

A: Yes, it is essential to prevent divergence from the intended architectural pattern to maintain the integrity of the design. Here are some practices to prevent divergence:

- Documentation: Thoroughly document architectural decisions and the rationale behind the selected pattern to serve as a reference for future modifications.
- Design Reviews: Conduct periodic design reviews to assess the current state of the system and identify any deviations from the original pattern.
- Continuous Education: Provide training and education to the development team, emphasizing the importance of adhering to architectural patterns.
- Automated Checks: Utilize automated tools and code analysis techniques to detect deviations from the pattern during code reviews and ensure modifications align with the architectural guidelines.

## c. Aspect-Oriented Programming and Architectural Patterns

**Q: Design patterns often represent crosscutting concerns that can be implemented using aspect-oriented programming or program transformation techniques. Is the same true of architectural patterns?**

A: While design patterns can be implemented using aspect-oriented programming (AOP) or program transformation techniques, architectural patterns have a broader scope and are not as easily implemented using these approaches. Architectural patterns focus on the overall structure, organization, and behavior of the system, whereas AOP primarily deals with crosscutting concerns within individual components.

However, there can be instances where certain aspects of an architectural pattern can be implemented using AOP techniques. Aspects such as logging, security, or performance monitoring can be applied across multiple components in a system, providing a level of separation and modularity.

It's important to note that architectural patterns address higher-level concerns, and their implementation often requires a holistic understanding of the system's structure and behavior. While AOP can contribute to the implementation of certain aspects within an architectural pattern, it should not be considered a replacement for the overall architectural design.

