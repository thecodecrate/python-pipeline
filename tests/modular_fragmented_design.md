# Modular Fragmented Design (MFD)

## 1. Introduction

Modular Fragmented Design (MFD) is a programming methodology that emphasizes the construction of software systems through the assembly of incomplete, interdependent modules called **Fragments**. Each Fragment represents a specific feature or modification and is designed to be integrated with other Fragments to form a complete, functional system. This approach promotes modularity, reusability, and a progressive understanding of the codebase.

This document specifies the conventions and structures to be followed when implementing MFD in Python applications. It outlines naming conventions, directory structures, class composition, interface implementation, and enforces standards to ensure consistency and maintainability across projects adopting this methodology.

## 2. Specification

### 2.1 Definitions

- **Fragment**: An incomplete module representing a specific feature or modification. Fragments are designed to be assembled with other Fragments to form a complete system. A Fragment can itself be an Assembled Package.

- **Assembled Class**: A class that combines a base class with mixins from Fragments to provide extended functionality.

- **Interface**: An abstract definition of methods and properties used for type-checking and ensuring that classes implement required functionalities.

- **Assembled Package**: A Python package containing Fragments and Assembled Classes, adhering to the MFD structure and conventions. The root directory of an Assembled Package can have any name the user chooses.

- **Mixin**: A class that provides methods and properties to be inherited by Assembled Classes, typically representing a Fragment's implementation.

- **Method Resolution Order (MRO)**: The order in which base classes are searched when executing a method.

### 2.2 Fragments

#### 2.2.1 Naming Conventions

- **Fragment Names**: Must start with `with_` followed by the feature name in lowercase with underscores (e.g., `with_user_authentication`).

- **Base Classes**: Named as `<ClassName>` (e.g., `Todoable`).

- **Mixin Classes**: Named as `<ClassName>Mixin` (e.g., `TodoableMixin`).

- **Interface Classes**:
  - **Base Class Interfaces**: Named as `<ClassName>Interface` (e.g., `TodoableInterface`).
  - **Mixin Interfaces**: Named as `<ClassName>InterfaceMixin` (e.g., `TodoableInterfaceMixin`).

#### 2.2.2 Structure

Each Fragment must:

- Reside within the `_fragments` directory of the Assembled Package.

- Contain its base classes, mixins, and interfaces.

- Have a `README.md` file documenting its purpose and dependencies.

- Enforce implementation of interfaces for all base classes and mixins.

### 2.3 Assembled Classes

#### 2.3.1 Naming Conventions

- **Assembled Classes**: Named identically to their base classes (e.g., `Todoable`).

- **Interfaces**: Named as `<ClassName>Interface` (e.g., `TodoableInterface`).

#### 2.3.2 Structure

Each Assembled Class must:

- Reside within the `_assembled` directory of the Assembled Package.

- Implement its interface, ensuring all required methods and properties are defined.

- Compose mixins and base classes following the enforced Method Resolution Order.

### 2.4 Interfaces

Interfaces are used to:

- Ensure type consistency across base classes, mixins, and Assembled Classes.

- Enforce the implementation of required methods and properties.

- Serve as contracts that classes must fulfill.

All interfaces must:

- Inherit from `Protocol` in the `typing` module.

- Be placed alongside their corresponding classes within the `_fragments` or `_assembled` directories.

- Follow the enforced naming conventions.

### 2.5 Directory Structure

An Assembled Package must have the following structure:

```text
/<package_root>/
    __assembled__.py
    /_fragments/
        /with_core/
            README.md
            <Fragment files>
        /with_crud_todo_list/
            README.md
            <Fragment files>
    /_assembled/
        <Assembled Classes and Interfaces>
```

- `__assembled__.py`: A required file indicating the directory is an Assembled Package.

- `/_fragments/`: Contains all Fragments and their interfaces.

- `/_assembled/`: Contains all Assembled Classes and their interfaces.

### 2.6 Method Resolution Order (MRO)

When composing classes, the MRO must be:

1. **Mixin Classes from Fragments** (ordered based on dependencies):
   - Mixins are renamed to match their Fragment folder name (e.g., `WithCrudTodoList`).

2. **Base Class**:
   - Imported and renamed to `WithBase`.

3. **Interface**:
   - Imported and renamed to `ImplementsInterface`.

For interfaces, the MRO is:

1. **Mixin Interfaces from Fragments** (ordered based on dependencies):
   - Mixin interfaces are renamed to match their Fragment folder name plus `Interface` (e.g., `WithCrudTodoListInterface`).

2. **Base Class Interface**:
   - Imported and renamed to `WithBaseInterface`.

3. **`Protocol`**:
   - From the `typing` module.

This order ensures that:

- Mixins override base class methods.

- Interfaces are properly implemented.

- Python's MRO is maintained for consistent behavior.

### 2.7 Enforced Conventions

The following conventions are **mandatory** and must be strictly followed:

- **Mandatory Directories**: The `/_fragments` and `/_assembled` directories are required.

- **Naming Conventions**: All classes, interfaces, and files must follow specified naming conventions.

- **Interfaces**: Implementation of interfaces is mandatory for all base classes, mixins, and Assembled Classes.

- **Assembled Package Indicator**: The `__assembled__.py` file is required.

- **Documentation**: Each Fragment must have a `README.md` documenting its purpose and dependencies.

### 2.8 Fragment Dependencies

- Fragments can depend on other Fragments.

- The `with_core` Fragment is foundational and must not depend on any other Fragments.

- Dependencies must be explicitly declared in the Fragment's `README.md`.

- A Fragment can itself be an Assembled Package.

### 2.9 Importing and Renaming Conventions

When importing classes and interfaces:

- **Base Classes and Interfaces**:
  - Imported base classes from Fragments must be renamed to `WithBase`.
  - Imported base class interfaces must be renamed to `WithBaseInterface`.

- **Mixins and Mixin Interfaces**:
  - Imported mixin classes from Fragments must be renamed to match their Fragment folder name (e.g., `WithCrudTodoList`).
  - Imported mixin interfaces must be renamed to match their Fragment folder name plus `Interface` (e.g., `WithCrudTodoListInterface`).

This convention avoids name conflicts and clarifies the origin of each imported class or interface.

## 3. Example

This example demonstrates implementing a `Todoable` class using Modular Fragment Design. The `Todoable` class allows for managing a todo list, with the core functionality provided by the `with_core` Fragment and extended CRUD operations provided by the `with_crud_todo_list` Fragment.

### 3.1 Fragment: `with_core`

#### 3.1.1 `README.md`

```markdown
# with_core

This Fragment provides the core functionality for the `Todoable` class, including the basic method `list_todo`.

Dependencies: None
```

#### 3.1.2 Interface: `TodoableInterface`

```python
# _fragments/with_core/todoable_interface.py
from typing import Protocol

class TodoableInterface(Protocol):
    def list_todo(self) -> list[str]:
        ...
```

#### 3.1.3 Base Class: `Todoable`

```python
# _fragments/with_core/todoable.py
from .todoable_interface import TodoableInterface as ImplementsInterface

class Todoable(ImplementsInterface):
    def list_todo(self) -> list[str]:
        return []
```

### 3.2 Fragment: `with_crud_todo_list`

#### 3.2.1 `README.md`

```markdown
# with_crud_todo_list

This Fragment adds CRUD functionality to the `Todoable` class, allowing todo items to be created, read, updated, and deleted.

Dependencies:
- with_core
```

#### 3.2.2 Interface Mixin: `TodoableInterfaceMixin`

```python
# _fragments/with_crud_todo_list/todoable_interface_mixin.py
from typing import Protocol
from ..with_core.todoable_interface import TodoableInterface as WithBaseInterface

class TodoableInterfaceMixin(WithBaseInterface, Protocol):
    def create_todo(self, item: str) -> None:
        ...
    def read_todo(self, index: int) -> str:
        ...
    def update_todo(self, index: int, item: str) -> None:
        ...
    def delete_todo(self, index: int) -> None:
        ...
```

#### 3.2.3 Mixin: `TodoableMixin`

```python
# _fragments/with_crud_todo_list/todoable_mixin.py
from .todoable_interface_mixin import TodoableInterfaceMixin as ImplementsInterface

class TodoableMixin(ImplementsInterface):
    _todo_list: list[str]

    def __init__(self):
        self._todo_list = []

    def create_todo(self, item: str) -> None:
        self._todo_list.append(item)

    def read_todo(self, index: int) -> str:
        return self._todo_list[index]

    def update_todo(self, index: int, item: str) -> None:
        self._todo_list[index] = item

    def delete_todo(self, index: int) -> None:
        del self._todo_list[index]

    def list_todo(self) -> list[str]:
        return self._todo_list
```

### 3.3 Assembled Class: `Todoable`

#### 3.3.1 Interface: `TodoableInterface`

```python
# _assembled/todoable_interface.py
from typing import Protocol
from .._fragments.with_crud_todo_list.todoable_interface_mixin import (
    TodoableInterfaceMixin as WithCrudTodoListInterface,
)
from .._fragments.with_core.todoable_interface import (
    TodoableInterface as WithBaseInterface,
)

class TodoableInterface(WithCrudTodoListInterface, WithBaseInterface, Protocol):
    pass
```

#### 3.3.2 Class: `Todoable`

```python
# _assembled/todoable.py
from .._fragments.with_crud_todo_list.todoable_mixin import TodoableMixin as WithCrudTodoList
from .._fragments.with_core.todoable import Todoable as WithBase
from .todoable_interface import TodoableInterface as ImplementsInterface

class Todoable(WithCrudTodoList, WithBase, ImplementsInterface):
    pass
```

### 3.4 Usage Example

```python
# example.py
from _assembled.todoable import Todoable

todo_manager = Todoable()
todo_manager.create_todo("Buy milk")
todo_manager.create_todo("Walk the dog")
print(todo_manager.list_todo())
# Output: ['Buy milk', 'Walk the dog']

todo_manager.update_todo(0, "Buy almond milk")
print(todo_manager.read_todo(0))
# Output: 'Buy almond milk'

todo_manager.delete_todo(1)
print(todo_manager.list_todo())
# Output: ['Buy almond milk']
```

## 4. Conclusion

Modular Fragment Design provides a structured and enforced approach to building software systems through the assembly of incomplete, interdependent Fragments. By following the conventions and specifications outlined in this document, developers can create modular, maintainable, and extensible applications. MFD encourages progressive understanding and collaboration, allowing developers to focus on individual Fragments and their integration into the complete system.
