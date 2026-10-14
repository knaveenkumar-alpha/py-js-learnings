 # Low-Level Design (LLD)

LLD describes the classes, objects, interfaces, relationships, and interactions needed to implement a feature. It focuses on maintainable, extensible, testable code.

## How to approach an LLD problem

The listed topics are useful building blocks, but they are not a rigid sequence. Follow this flow:

1. **Clarify requirements**
	- Identify actors, use cases, inputs, outputs, constraints, and edge cases.
	- State assumptions and define the scope before designing.

2. **Identify responsibilities and objects**
	- Convert important nouns into candidate classes and verbs into behaviors.
	- Give each class one clear responsibility and define its public operations.

3. **Apply OOP and the four pillars**
	- **Encapsulation:** keep state private and expose controlled behavior.
	- **Abstraction:** expose essential behavior while hiding implementation details.
	- **Inheritance:** model a genuine *is-a* relationship; do not use it only for reuse.
	- **Polymorphism:** allow interchangeable implementations through a common contract.

4. **Define relationships**
	- **Association:** one object uses or knows another.
	- **Aggregation:** a whole contains parts that can exist independently.
	- **Composition:** a whole owns parts whose lifecycle depends on it.
	- **Inheritance:** a subtype is substitutable for its parent.
	- Prefer composition over inheritance when it reduces coupling.

5. **Check the design with SOLID**
	- **S:** Single Responsibility
	- **O:** Open/Closed
	- **L:** Liskov Substitution
	- **I:** Interface Segregation
	- **D:** Dependency Inversion

6. **Choose interfaces or abstract classes**
	- Use an **interface** for a contract or capability that unrelated classes can implement.
	- Use an **abstract class** when related classes share state or meaningful default behavior.
	- Depend on abstractions and inject dependencies instead of constructing concrete dependencies internally.

7. **Apply design patterns only when justified**
	- Patterns solve recurring design problems; they are not mandatory steps.
	- Common examples include Factory, Strategy, Observer, Adapter, Decorator, Builder, and State.
	- Explain the benefit and trade-offs before introducing a pattern.

8. **Create and validate UML diagrams**
	- Use a class diagram for classes, key fields, methods, visibility, and relationships.
	- Use a sequence diagram to show important object interactions over time.
	- Walk through each use case and test how the design handles a new requirement.

## Quick checklist

- Requirements and assumptions are clear.
- Classes have focused responsibilities.
- Relationships and ownership are explicit.
- Public APIs and dependencies are defined.
- The design handles errors, extensibility, and concurrency where relevant.
- The simplest design that satisfies the requirements is preferred.

In short: **requirements → responsibilities → relationships → abstractions → interactions → validation**. Start simple, then introduce patterns or abstractions when a concrete requirement calls for them.
