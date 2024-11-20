# \[spec-001\] A Convention for Structuring Classes Using Partial Classes

This language-agnostic document introduces a convention for structuring individual classes using partial classes. It focuses on simplifying class definitions by splitting them into manageable parts, enhancing modularity and maintainability.

In a separate specification, we'll explore how to extend this approach horizontally across groups of classes, which is particularly useful when partials represent features in a project or package.

## Background

Partial classes enable you to split a single class definition across multiple source files. Each partial class contains a portion of the overall class, and all parts are combined to form the complete class. This approach helps manage complex classes by dividing them into smaller, more manageable pieces.

Example:

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    class Partial1["Partial1"] {
        +method1()
        +method2()
    }

    class Partial2["Partial2"] {
        +method3()
        +method4()
    }

    class Partial3["PartialN"] {
        +...()
        +methodN()
    }

    class Composed["ClassA"] {
    }

    %% Relationships
    Partial1 <|-- Composed
    Partial2 <|-- Composed
    Partial3 <|-- Composed

    %% Apply Styles
    style Partial1 bugfix:1, stroke-dasharray: 5 5, stroke-width:1px
    style Partial2 bugfix:1, stroke-dasharray: 5 5, stroke-width:1px
    style Partial3 bugfix:1, stroke-dasharray: 5 5, stroke-width:1px
    style Composed bugfix:1, font-weight: bold, stroke-width:2px
```

Using partial classes is beneficial in several scenarios:

- **Modularity**: Large classes can be broken down into smaller sections for easier understanding and maintenance.
- **Organization**: Related methods can be grouped together, improving code structure.
- **Collaboration**: Multiple developers can work on different parts simultaneously, reducing merge conflicts.

## Partial Classes vs. Traits

While both partial classes and traits allow you to split a class's functionality, they serve different purposes.

**Partial classes** are used to split a single class into multiple parts.

**Traits**, on the other hand, provide reusable methods that can be incorporated into multiple classes.

## Support in Programming Languages

Some programming languages, like C#, provide built-in support for partial classes using the `partial` keyword. This feature allows you to split a class definition across multiple files, which are then combined at compile time.

In languages without native support for partial classes, such as Python, you can achieve similar modularity through traits, mixins, multiple inheritance, or single inheritance composition.

It's important to note that while traditional partial classes are combined during compilation, in this specification, we use the term "partial classes" differently. Here, it refers to splitting a class into multiple parts for better organization and modularity, with the parts combined at the source code level rather than at compile time.

## Specification

This specification introduces a convention for structuring classes using partial classes. It involves three main components:

1. **🧬 Base Class**: Contains the core functionality of the class.
2. **🥬 Partial Classes**: Partial classes that add additional functionality.
3. **🥗 Composed Class**: Combines the base class and partials into a single class.

An example of a composed class is:

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    class Base["🧬 CatBase"] {
        <<*base*>>
        +set_name(name)
        +get_name()
    }

    class Partial1["🥬 WithAge"] {
        <<*partial*>>
        +set_age(age)
        +get_age()
    }

    class Partial2["🥬 WithAgility"] {
        <<*partial*>>
        +set_agility(agility)
        +get_agility()
    }

    class Composed["🥗 Cat"] {
        <<*composed*>>
    }

    %% Relationships
    Base <|-- Composed : extends
    Partial1 <|-- Composed : extends
    Partial2 <|-- Composed : extends

    %% Apply Styles
    style Base fill:#ffff6020, stroke-dasharray: 5 5
    style Composed bugfix:#111, stroke-width:2px, font-weight: bold
    style Partial1 bugfix:#111, stroke-dasharray: 5 5
    style Partial2 bugfix:#111, stroke-dasharray: 5 5
    style Partial3 bugfix:#111, stroke-dasharray: 5 5
    style Interface1 fill:#ff606020, stroke-dasharray: 2 2
```

In this convention:

- The base class (`CatBase`) includes the essential methods.
- Partial classes are named using the pattern `With<PartialName>` (e.g., `WithAge`, `WithAgility`).
- The composed class (`Cat`) extends the base class and incorporates all partials.

### File Structure

The recommended file structure is:

```pseudo
<class_name>/
├── <class_name>_base.lang       # Base class with core functionality
│
├── partials/                    # Folder containing all partial implementations
│   ├── with_<partial1>.lang     # Partial 1
│   ├── ...                      # Additional partial classes
│   └── with_<partialN>.lang     # Partial N
│
└── <class_name>.lang            # Composed class: base + partials
```

Notes:

- `<class_name>` is the name of your class (e.g., `Cat`).
- The `.lang` extension represents the language-specific file extension (e.g., `.py`, `.cs`).
- Adjust the naming conventions (PascalCase, snake_case, etc.) to match your programming language's standards.

### One-to-One Interface Mapping

To enhance type safety and ensure consistent implementation of methods, each class in this convention must have a corresponding interface. This one-to-one mapping applies to:

- **Base Class**
- **Partial Classes**
- **Composed Class**

```pseudo
<class_name>/
├── ...                                  # Previous structure
├── <class_name>_base_interface.lang     # Interface for the base class
│
├── partials/                            # Folder containing all partial interfaces
│   ├── with_<partial1>_interface.lang
│   ├── ...
│   └── with_<partialN>_interface.lang
│
└── <class_name>_interface.lang          # Composed interface: base +partial interfaces
```

Interfaces are named by appending `Interface` to its corresponding class name. For example:

- `CatBase` -> `CatBaseInterface`
- `WithAge` -> `WithAgeInterface`
- `Cat` -> `CatInterface`

### Implementation Details

#### Base Class

The **base class** serves as a special partial containing the core functionality of the composed class.

**Interfaces** should not contain any concrete implementations; they should only list method signatures that the concrete classes will implement. This rule applies to all interfaces, including base class interfaces.

Name base interfaces using the pattern `<ClassName>BaseInterface`. For example:

```mermaid
classDiagram
    class Interface1["🫥 CatBaseInterface"] {
        <<*base interface*>>
        +set_name(name)
        +get_name()
    }

    %% Apply Styles
    style Base fill:#ffff6020, stroke-dasharray: 5 5
    style Composed bugfix:#111, stroke-width:2px, font-weight: bold
    style Partial1 bugfix:#111, stroke-dasharray: 5 5
    style Partial2 bugfix:#111, stroke-dasharray: 5 5
    style Partial3 bugfix:#111, stroke-dasharray: 5 5
    style Interface1 fill:#ff606020, stroke-dasharray: 2 2
```

**Concrete** classes should inherit from their interfaces, after renaming them as `ImplementsInterface`. This rule applies to all concrete classes, including base classes.

```mermaid
classDiagram
    %% note for Base "ImplementsInterface = aliasTo(CatBaseInterface)"

    class Interface1["🫥 ImplementsInterface"] {
        <<*aliasOf CatBaseInterface*>>
        +set_name(name)
        +get_name()
    }

    class Base["🧬 CatBase"] {
        <<*base*>>
        +set_name(name)
        +get_name()
    }

    %% Relationships
    Interface1 <|-- Base : implements

    %% Apply Styles
    style Base fill:#ffff6020, stroke-dasharray: 5 5
    style Composed bugfix:#111, stroke-width:2px, font-weight: bold
    style Partial1 bugfix:#111, stroke-dasharray: 5 5
    style Partial2 bugfix:#111, stroke-dasharray: 5 5
    style Partial3 bugfix:#111, stroke-dasharray: 5 5
    style Interface1 fill:#ff606020, stroke-dasharray: 2 2
```

Alternatively, you can keep the base class empty and move core functionalities to a partial class, using the empty base class as a marker:

```mermaid
classDiagram
    note for CatBase "ImplementsInterface = aliasTo(CatBaseInterface)"

    class CatBaseInterface {
        <<*interface*>>
        %% Empty interface
    }

    class CatBase {
        %% Empty class
    }

    CatBase --|> CatBaseInterface : implements
```

#### Partials

**Partials** add additional functionalities to the composed class.

Partial interfaces must always import the base interface, renaming it to `WithBaseInterface` to maintain consistency and distinction. Partial interfaces are named `With<PartialName>Interface`. For example:

```mermaid
classDiagram
    note for WithBaseInterface "WithBaseInterface = aliasTo(CatBaseInterface)"

    class WithBaseInterface {
        <<*interface*>>
    }

    class WithAgeInterface {
        <<*interface*>>
        + set_age(age)
        + get_age()
    }

    WithBaseInterface <|-- WithAgeInterface : extends
```

For the concrete partial class:

- Import its own interface as `ImplementsInterface`.
- Inherit from `ImplementsInterface`.
- Do not import the base class or other partial classes, even if their methods are used.

Example:

```pseudo
ImplementsInterface = aliasTo(WithAgeInterface)

class WithAge
├── extends ImplementsInterface
│
├── +set_age(age)  # implementation
└── +get_age()     # implementation
```

If a partial depends on other partials, its interface must import those partials' interfaces. For example, `WithAgilityInterface` depends on `WithAgeInterface`:

```pseudo
WithBaseInterface = aliasTo(CatBaseInterface)

class WithAgilityInterface
├── extends WithAgeInterface
├── extends WithBaseInterface
│
├── +set_agility(agility)
└── +get_agility()
```

The concrete class:

```pseudo
ImplementsInterface = aliasTo(WithAgilityInterface)

class WithAgility
├── extends ImplementsInterface
│
├── +set_agility(agility)  # implementation
└── +get_agility()         # implementation
```

Concrete partial classes typically inherit only from `ImplementsInterface`, but they can also inherit from external concrete classes like traits:

```pseudo
class WithPartial3
├── extends SomeTrait
├── extends ImplementsInterface
│
└── ...  # methods
```

#### Composed Class

The **composed class** combines the base class and all partials into one.

Its interface must import all partial interfaces and the base interface and is named `<ClassName>Interface`:

```pseudo
WithBaseInterface = aliasTo(CatBaseInterface)

class CatInterface
├── extends WithAgilityInterface
├── extends WithAgeInterface
└── extends WithBaseInterface
```

The concrete composed class must:

- Import and inherit from the concrete classes of all partials.
- Import the concrete base class (`WithBase`).
- Import its own interface as `ImplementsInterface`.
- Inherit from `ImplementsInterface`.

Example:

```pseudo
WithBase = aliasTo(CatBase)
ImplementsInterface = aliasTo(CatInterface)

class Cat
├── extends WithAgility
├── extends WithAge
├── extends WithBase
└── extends ImplementsInterface
```

The composed class and its interface should remain empty, serving only to combine components. For additional methods or attributes, create a new partial.

### Additional Considerations

1. **Inheritance Order**

    When importing `ImplementsInterface`, place it at the bottom of the inheritance chain to allow overriding by other classes:

    ```pseudo
    class MyClass
    └── extends ThirdClass
         └── extends SecondClass
              └── extends ImplementsInterface
    ```

2. **Dependency Ordering**

    When importing partials and their interfaces, order them from highest-level dependencies to the base. The base class (`WithBase` or `WithBaseInterface`) is the most fundamental dependency:

    ```pseudo
    class Cat
    ├── extends WithAgility
    ├── extends WithAge
    ├── extends WithBase
    └── extends ImplementsInterface
    ```
