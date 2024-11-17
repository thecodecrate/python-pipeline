# \[spec-001\] Class Composition with Partial Classes

This document introduces a convention for class structuring using partial classes, focusing on simple, individual classes. In a different specification, we'll explore how to extend this approach horizontally across groups of classes, which is particularly useful when partials represent features in a project or package.

This document is language-agnostic and can be applied to any programming language that supports object-oriented programming.

## Background

Partial classes are a construct used to split a class definition across multiple source files.

Each partial class contains a section of the overall class definition. All parts are then combined into a single, complete class.

```pseudo
class Partial1
├── +method1()
└── +method2()

class Partial2
├── +method3()
└── +method4()

...

class ClassA
├── extends Partial1
├── ...
└── extends PartialN
```

There are several situations when splitting a class definition is desirable:

- **Modularity**: Break a large class into smaller, more manageable pieces.
- **Organization**: Group related methods together for better organization.
- **Collaboration**: Enable team members to work on different parts simultaneously.

## Partial Classes vs. Traits

While both partial classes and traits allow you to split a class's functionality, they serve different purposes.

**Partial classes** are used to split a single class into multiple parts.

**Traits**, on the other hand, provide reusable methods that can be incorporated into multiple classes.

## Support in Programming Languages

Some languages, like C#, have built-in support for partial classes. In C#, you can define a class in multiple files using the `partial` keyword.

Other languages, like Python, don't have built-in support for partial classes. However, you can achieve similar functionality by using traits, mixins, multiple inheritance, or with a single inheritance composition.

## Specification

This specification consists of three main components:

1. **Base Class**: Defines the core functionality of the class.
2. **Partials**: Partial classes that add extra functionality.
3. **Composed Class**: Combines the base class and partials into a single class.

A composed class typically looks like this:

```pseudo
# Base class
class CatBase
├── +set_name(name)
└── +get_name()

# Partial 1
class WithAge
├── +set_age(age)
└── +get_age()

# Partial 2
class WithAgility
├── +set_agility(agility)
└── +get_agility()

# Composed Class: Partials + Base
class Cat
├── extends WithAgility
├── extends WithAge
└── extends CatBase
```

In this convention, the base class is a special kind of partial that contains the core functionality. Partial classes are named using the pattern `With<PartialName>`.

The recommended file structure is:

```pseudo
<class_name>/
├── <class_name>_base.lang     # Base class with core functionality
│
├── partials/                  # Folder containing all partial implementations
│   ├── with_<partial1>.lang
│   ├── ...
│   └── with_<partialN>.lang
│
└── <class_name>.lang          # Composed class: base +partials
```

The `.lang` represents the language-specific file extension (e.g., `.py` for Python, `.cs` for C#). You must adapt the casing style (PascalCase, snake_case, etc.) to match the conventions of your programming language.

### One-to-One Interface Mapping

Each class must have a corresponding interface to help with type hinting and ensure that all methods are implemented correctly.

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

The interfaces have the same name as their concrete classes plus `Interface`, e.g. `CatInterface`, `CatBaseInterface`, `WithAgeInterface`, etc.

### Implementation Details

#### Base Class

The base class is a special partial that contains the core functionality for the composed class.

Interfaces must not contain any concrete implementation. An interface must only contain a list of method signatures to be implemented by its concrete class. This rule is valid for all interfaces, not just base class interfaces.

Base interfaces must be named `<ClassName>BaseInterface`.

```pseudo
class CatBaseInterface
├── +set_name(name)  # signature
└── +get_name()      # signature
```

Whenever you write a concrete class in this specification, you must import its interface and rename it to `ImplementsInterface`. The concrete class must inherit from the renamed interface.

```pseudo
ImplementsInterface = aliasTo(CatBaseInterface)

class CatBase
├── extends ImplementsInterface
│
├── +set_name(name)  # implementation
└── +get_name()      # implementation
```

Alternatively, you can have the base class empty and move the core functionality to a partial class. This approach is useful when you want to keep the base class clean.

```pseudo
class CatBaseInterface
└──

ImplementsInterface = aliasTo(CatBaseInterface)

class CatBase
└── extends ImplementsInterface
```

#### Partials

Partials add extra functionality to the composed class.

Partial interfaces must always import the base interface. When importing, they must be renamed as `WithBaseInterface` to distinguish the base class from other components and maintain naming consistency. Partial interfaces are named `With<PartialName>Interface`.

```pseudo
WithBaseInterface = aliasTo(CatBaseInterface)

class WithAgeInterface
├── extends WithBaseInterface
│
├── +set_age(age)
└── +get_age()
```

The concrete version of the partial class must import its own interface (`ImplementsInterface`). Usually, that's the only import used by the partial class. The partial class must not import the base class or other partial classes, even if it uses their methods. It must be named `With<PartialName>`.

```pseudo
ImplementsInterface = aliasTo(WithAgeInterface)

class WithAge
├── extends ImplementsInterface
│
├── +set_age(age)
└── +get_age()
```

A partial interface must import the interfaces of any other partials it depends on. This ensures that all necessary methods and attributes are available.

In this next trait, `WithAgility`, we import the interface of `WithAgeInterface` because it depends on its methods.

```pseudo
WithBaseInterface = aliasTo(CatBaseInterface)

class WithAgilityInterface
├── extends WithAgeInterface
├── extends WithBaseInterface
│
├── +set_agility(agility)
└── +get_agility()
```

As before, the concrete class of the partial should import its interface (`ImplementsInterface`) and nothing else.

```pseudo
ImplementsInterface = aliasTo(WithAgilityInterface)

class WithAgility
├── extends ImplementsInterface
│
├── +set_agility(agility)
└── +get_agility()
```

Concrete partial classes often only inherit `ImplementsInterface`; however, they can inherit other classes, as long as they are external and concrete (e.g., traits).

```pseudo
class WithPartial3
├── extends SomeTrait
├── extends ImplementsInterface
│
└── ... methods
```

#### Composed Class

A composed class combines the base class and partials into a single class.

A composed interface must import all partial interfaces plus the base interface. It must be named `<ClassName>Interface`.

```pseudo
WithBaseInterface = aliasTo(CatBaseInterface)

class CatInterface
├── extends WithAgilityInterface
├── extends WithAgeInterface
└── extends WithBaseInterface
```

The concrete composed class must import the concrete classes of all partials, the concrete base class (`WithBase`), and its own composed interface (`ImplementsInterface`). It must be named `<ClassName>`.

```pseudo
WithBase = aliasTo(CatBase)

ImplementsInterface = aliasTo(CatInterface)

class Cat
├── extends WithAgility
├── extends WithAge
├── extends WithBase
└── extends ImplementsInterface
```

The composed class and its interface should be empty. They only serve to combine the base class and partial classes. If you need to add additional methods or attributes, consider creating a new partial.

### Additional Considerations

1. When importing the interface `ImplementsInterface`, it must be placed at the bottom of the inheritance chain. This allows it to be overridden by other classes.

    ```pseudo
    class MyClass
    └── class ThirdClass
        └── class SecondClass
            └── class ImplementsInterface
    ```

    This rule applies to all types of concrete classes:

    - Base classes
    - Partials
    - Composed classes

1. When importing partials and their interfaces, they must be ordered from the highest-level to the lowest-level (base dependencies). The base class (`WithBase` or `WithBaseInterface`) is always the most basic dependency.

    ```pseudo
    class Cat
    └── class WithAgility
        └── class WithAge
            └── class WithBase
                └── class ImplementsInterface
    ```
