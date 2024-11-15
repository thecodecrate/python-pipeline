# Title for this design methodology

some intro text...

## Partial Classes

The partial class pattern allows you to split the definition of a class over two or more source files.

Each partial class contains a piece of the class definition. All parts are combined into a single class definition to form the complete class:

```python
class ClassA(Partial1, Partial2):
    pass

class Partial1:
    def method1(self): ...
    def method2(self): ...

class Partial2:
    def method3(self): ...
    def method4(self): ...
```

There are several situations when splitting a class definition is desirable:

- When the class is too large and needs to be split into smaller parts.
- To group related methods together for better organization.
- To make easier concurrent development by team members.

## Partial Classes vs Traits

Technically, there's no difference between partial classes and traits. Both patterns allow you to split a class definition into multiple parts.

What distinguishes them is the intent behind their use:

- Partial classes are used to split a class definition into multiple parts, usually to group related methods together.
- Traits are used to define a set of methods that can be reused across multiple classes.

## Implementation

Some languages like C# have built-in support for partial classes. In C#, you can define a class in multiple files using the `partial` keyword.

Other languages, like Python, don't have built-in support for partial classes. However, you can achieve the same effect by using traits, mixins, multiple inheritance or a chained single inheritance pattern.

## A simple approach for partial classes in Python

We present a simple approach for working with partial classes in Python.

The approach consists of three parts:

1. A base class that defines the core functionality of the class.
2. Partial classes that define additional functionality.
3. A composed class that combines the base class and the partial classes.

The file structure follows this pattern:

```text
<class name>/
├── <class name>_base.py    # Base class: core functionality
├── partials/               # Folder containing all partial implementations
│   ├── with_<partial 1>.py
|   ├── with_<partial 2>.py
|   ├── ...
│   └── with_<partial n>.py
└── <class name>.py         # Composed class: base + partials
```

The "base class" is a technically a partial. It is the first partial and contains the core functionality of the class.

The name convention for a partial is `with_<partial name>.py`. The partials are stored in a `partials` folder.

Each class has a corresponding interface, not shown in the file structure. The interfaces are implemented as a protocol in Python.

## Example: Cat class

Let's create a `Cat` class that has a name and an age. We will split the class into two partials: one for the name and one for the age.

The base class will be called `CatBase` and will contain the name functionality:

```python
# cat/cat_base_interface.py
class CatBaseInterface(Protocol):
    def set_name(self, name: str) -> None: ...
    def get_name(self) -> str: ...
```

Now, we implement the concrete base class. A the concrete class of a partial (a base class is a partial) should import the corresponding interface and rename it as `ImplementsInterface`:

```python
# cat/cat_base.py
from .cat_base_interface import CatBaseInterface as ImplementsInterface

class CatBase(ImplementsInterface):
    _name: str

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name
```

Now, let's create a partial for the age.

On a partial interface, we import the interfaces of the partials that it depends on. In this case, the `CatBaseInterface`.

Base interfaces are always imported with the `WithBaseInterface` alias:

```python
# cat/partials/with_age_interface.py
from ..cat_base_interface import CatBaseInterface as WithBaseInterface

class WithAgeInterface(WithBaseInterface, Protocol):
    def set_age(self, age: int) -> None: ...
    def get_age(self) -> int: ...
```

On a partial concrete class, we import the interface and rename it as `ImplementsInterface`:

```python
# cat/partials/with_age.py
from .with_age_interface import WithAgeInterface as ImplementsInterface

class WithAge(ImplementsInterface):
    _age: int

    def set_age(self, age: int) -> None:
        self._age = age

    def get_age(self) -> int:
        return self._age
```

Finally, we compose the class. The composed interface should import the partial interfaces, the base interface, and the `Protocol` class:

```python
# cat/cat_interface.py
from .cat_base_interface import CatBaseInterface as WithBaseInterface
from .partials.with_age_interface import WithAgeInterface

class CatInterface(
    WithAgeInterface,
    WithBaseInterface,
    Protocol,
):
    pass
```

The composed concrete class must import the partials, the base class and the composed interface:

```python
# cat/cat.py
from .cat_base import CatBase as WithBase
from .partials.with_age import WithAge
from .cat_interface import CatInterface as ImplementsInterface

class Cat(
    WithAge,
    WithBase,
    ImplementsInterface,
):
    pass
```
