# Daniel's Modular Programming Design

Please help me organizing some ideas I have regarding a modularized programming design that I'm working on. Here it goes:

I recently started programming with a modularized design in mind. It works like this: the software (website, app, library, etc) starts with almost no code, like when you create a new project in a framework. Think of a new empty project in nextjs, laravel, ruby on rails, or wordpress installation. Then, I add features to the project as if they were plugins or game DLCs.

Technically, these DLCs/plugins are called "modules", however, in my design I call them "partials". The name "partials" comes from Laravel's partials, which are used to compose views. I'm not sure if I will keep this name, but that's the name I'm using for now.

The term "module" I think is too generic - someone not familiar with my design can be misled by the name. I thought about using other terms, but I couldn't find one that I loved.

For example, "plugins" for me are related to the "plugin pattern" or the "plugin architecture". When I think of "plugins" I think of an implementation using the observer pattern (like WordPress' plugins), which is not what I'm doing. My concept of "modules" is related to the "traits" concept in PHP. We extend the project in a static way, by composing classes. We don't extend it in a dynamically way as in the observer pattern.

A term that describes almost perfectly my idea of modules is the term "trait" as used in PHP. In PHP, a trait is a set of methods and properties that can be added to a class. For example, let's say you have a library that provides user authentication for Laravel. The library provides an `UserAuthenticable` trait that you should apply to the "User" model. By applying the trait, the User model gains methods like `login`, `logout`, `register`, etc, and thus, it gains a new feature: the ability to authenticate users.

While the term "trait" works well to describe adding a feature, a trait is limited to a single class. This means "trait" cannot be used as a synonym of "feature", as a feature may need (and most likely it will) to change multiple classes in order to have effect. Let's say that in order to work, the user authentication library also requires to add a trait to the controller, and another trait to the routes file. In this case, the "user authentication" feature is formed by three different traits. That's my problem with the term "trait" - traits are specific to a single class and features can (and mostly will) affect multiple classes. I needed a term that could be used as synonym for "feature", regardless of how many classes it affects.

Other terms I thought about using are "addons" and "extensions", however, they feel too decoupled from the project. "Addons" and "extensions" are things that you add to a project, but they are not part of the project itself. I want a term that makes it clear that the feature is part of the project, not an external thing that you add to the project.

I want a term that putting many pieces together to assembly the project. Like building a Lego's house. You have the base, the walls, the roof, the windows, the doors, etc. Each piece is a part of the house, but the house is the sum of all parts.

The term "partial" is the best term I could find. In Laravel, using the Blade template engine, a view is composed of multiple parts, called "partials". That's the concept I'm looking for and that's why I chose the term "partial" to describe the features that I add to a project. I just hope that the term doesn't causes confusion to other developers.

So, when a trait needs to be added to multiple classes to work, it's not a trait, it's a partial ;) That's what partials are: a trait that should be applied to multiple classes in order to add a feature to the project.

Now that we have a term for the modules, let's talk about other terms and naming conventions I will use for my modular programming.

We use the term "mixins" for the traits that compose a partial. The term "mixin" is the technical name of what traits are. It's more generic than "traits", but I opted for the term "mixin" to avoid confusion with the traditional definition of "trait" while maintaining the same concept and being technically correct.

Partial names start with "with_", followed by the feature it adds to the project. For example, a partial that adds user authentication to a project is called "with_user_authentication". A partial that adds stripe integration is called "with_stripe_integration".

Mixins have the same name of the class they extends, but with the word "Mixin" at the end. For example, the mixin for the "User" model is called "UserMixin". The mixin for the "Controller" is called "ControllerMixin". The mixin for the "Routes" file is called "RoutesMixin".

Besides mixins, partials can add new classes to the project. These new classes are called "base classes". For example, the "with_user_authentication" partial could have a "AuthenticationToken" class, for its internal usage. In this case, "AuthenticationToken" class is a base class. However, notice that these new classes (aka "base classes") not necessarily are for internal usage only. They can be used by the project as well.

We use class composition to apply partials to a project. For example, to allow a class "A" be extended by the project partials, we create a new class that extends "A" plus the mixins from the partials. The class will have the same name as its base-class, "A" in the example. This new composed class is called a "composed class".

For example, let's say the MVC framework we are using has a "Controller" class and we want to allow the project's partials to extend it. We would do this:

```python
from framework.controllers import Controller as WithBase
from partials.with_user_authentication.controller_mixin import ControllerMixin as WithUserAuthentication

class Controller(
  WithUserAuthentication,
  WithBase,
):
  pass
```

In this example, "Controller" class is a composed class. To avoid name conflicts, we always rename the imported base-class to "WithBase".

Here, we only have one mixin affecting the "Controller" class (from the "with_user_authentication" partial), but we could have multiple mixins. If we had multiple mixins, they all would have the same "ControllerMixin" name. This is because the name convention for mixins is `<base_class>Mixin`. To avoid name conflicts, we always rename the imported mixins to the same name as the partial folder they are from. In the example, it's `WithUserAuthentication`.

In a project, we always use the composed-class versions of a class, never their base classes directly. Base classes can only be used by mixins and by composed-classes definitions.

Ideally, each partial should have a file named `README.md` explaining what the partial does and that also lists the partials that it depends on. This is not mandatory, but it helps a lot when trying to understand the project structure.

It's recommended, but not enforced, to store the partials in a folder named `/partials` and the composed classes in a folder named `/classes`. This is not mandatory, but having a convention for storing these classes makes easier to find them.

The folder containing `/partials` and `/classes` is called a "composed package". A composed package must have a special file that indicates it is a composed package, named `__composed_package__.py`. This file can be empty.

A composed package doesn't have to be a python package. However, it is highly recommended to be a python package. This makes it easier to understand and organize the project.

I'm not 100% sold on the term "composed package". I'm not sure if it's the best term to describe the concept. I'm open to suggestions.

When composing classes in this modular way, we must have interfaces for each class. We always have a concrete and an interface class. This is valid for mixins in partials, for new base-classes in partials, and for composed classes.

The interfaces are used to ensure that the mixins and the composed classes have the methods they need. It's for type-checking.

The interfaces for the concrete classes of a partial are stored together, in the same partial folder. Interfaces have the word "Interface" after the class name, but before "Mixin" if the class is a mixin. For example, the interface for the "UserMixin" class is called "UserInterfaceMixin".

The interfaces for the concrete classes of composed classes are also stored in the `/classes` folder, alongside the concrete composed classes. The interfaces are named the same as the composed class, but with the word "Interface" at the end. For example, the interface for the "Controller" class is called "ControllerInterface".

Let's refactor our previous code to include the interfaces:

```python
# /classes/controller_interface.py
from framework.controllers import ControllerInterface as WithBaseInterface
from partials.with_user_authentication.controller_interface_mixin import ControllerInterfaceMixin as WithUserAuthenticationInterface

class ControllerInterface(
  WithUserAuthenticationInterface,
  WithBaseInterface,
  Protocol,
):
  pass
```

The composed-class interface must be a protocol. This is because we are using protocols to implement interfaces in python. However, I'm not sure if that's the best way to do it. Some alternatives to consider are: abstract classes (ABC), python's stub files, concrete classes, etc. For now, I will keep using protocols.

Due to Python's MRO (Method Resolution Order), we must follow a specific order when composing interface classes. The mixins are the first to be added, then the base-class, and finally, the "Protocol" special class.

As before, we rename the imported base-class to "WithBase" and the imported mixins to the same name as the partial folder they are from. The only difference is that we add the word "Interface" at the end, to indicate that they are interfaces.

```python
# /classes/controller.py
from framework.controllers import Controller as WithBase
from partials.with_user_authentication.controller_mixin import ControllerMixin as WithUserAuthentication
from .controller_interface import ControllerInterface as ImplementsInterface

class Controller(
  WithUserAuthentication,
  WithBase,
  ImplementsInterface,
):
  pass
```

For the concrete composed-class, we import the concrete mixins, the concrete base-class and finally, the composed-class interface. It's important to follow this order due to Python's MRO (Method Resolution Order). The mixins are the first to be called, then the base-class, and finally the composed-class itself (if anything is defined there). The last class to be called is the one that implements the interface.

As we did previously, we rename the imported base-class to "WithBase" and the imported mixins to the same name as the partial folder they are from.

For clarity, our convention is to always rename the composed-class interface to "ImplementsInterface".

A project can have multiple composed-packages. Each composed-package must have its own `/partials` and `/classes` folders. The `/partials` folder contains the partials and their interfaces. The `/classes` folder contains the composed classes and their interfaces.

Even a partial can be a composed-package, with its own `/partials` and `/classes` folders. This is useful when a partial is too big and needs to be split into smaller parts. However, it is more common to have a single composed-package: the project itself, usually matching the project's root or a sub-folder that contains the source-code (ex. `/src`).

It is recommended that the first partial of any composed-package to be named `with_core`. The "with_core" partial is the starting point of a composed-package. This partial contains the minimum necessary features for the composed-package to work. It's like a "minimum viable product" (MVP). The other partials depend on the "with_core" partial (directly or indirectly). The "with_core" partial doesn't depend on any other partial. Because of this, it usually only has base-classes and their interfaces, but not mixins. The exception is when it extends third-party classes.

Notice that the `with_core` is a convention and not a rule, however, it is highly recommended to follow it.

It is subjective how to break the code into partials. The idea is to break the code into smaller parts that are easier to understand and maintain. The goal is to have a project that is easy to extend and modify. The partials should be small enough to be understood in a single reading. The partials should be easy to test and to debug. The partials should be easy to reuse in other projects. Ideally, they should do a single thing only (single responsibility principle).

My mindset for defining which features are part of "core" and which features should be implemented as other modules is to think: "if this was a commercial product, like a game, and I would like to maximize profit with DLCs - what's the minimum I can put on the base product so I can sell the other features in separate DLCs, but still making the base product to be functional enough to be indentified as what it proposes to be? how much can i break the other features into separate DLCs, maximizing the amount of them - and thus, the profit, and still having each DLC useful independently?". The projects I work are not for sale, however, I like to keep this mindset to help me define the modules (partials).

Let's say we want to build a python library for a todo list. The library's API will provide a trait `Todoable` that can be added to any user-class to make it a todo list manager. The trait has a method `get_todo_list` that returns a list of todo items. The library will have a MVC version, where the todo list is hardcoded in the library, and a CRUD version, where the todo list is stored in a file.

Our `with_core` will implement the MVC. Then, we will have a `with_crud_todo_list` that will implement the CRUD functionality.

Let's implement the `with_core` partial for our todo list library.

```python
# partials/with_core/todo_item_collection.py
class TodoItemCollection:
  _items: list[str]

  def __init__(self, items: list[str]):
    self._items = items

  def _get_items(self) -> list[str]:
    return self._items
```

```python
# partials/with_core/todoable.py
class Todoable:
  todo_item_collection: TodoItemCollection

  def __init__(self):
    self.todo_item_collection = TodoItemCollection(items=[])

  def get_todo_list(self) -> list[str]:
    return self.todo_item_collection._get_items()
```

As we known, each class in a partial must have a corresponding interface. Let's extract the interfaces from the classes:

```python
# partials/with_core/todo_item_collection_interface.py
class TodoItemCollectionInterface(Protocol):
  def __init__(self, items: list[str]): ...
  def _get_items(self) -> list[str]: ...
```

```python
# partials/with_core/todoable_interface.py
class TodoableInterface(Protocol):
  def __init__(self): ...
  def get_todo_list(self) -> list[str]: ...
```

The previous concrete classes must implement these interfaces. Let's refactor them:

```python
# partials/with_core/todo_item_collection.py
from .todo_item_collection_interface import (
  TodoItemCollectionInterface as ImplementsInterface,
)

class TodoItemCollection(
  ImplementsInterface,
):
  # ... rest of the class remains the same
```

```python
# partials/with_core/todoable.py
from .todoable_interface import (
  TodoableInterface as ImplementsInterface,
)

class Todoable(
  ImplementsInterface,
):
  # the rest of the class remains the same
```

Each base class must have two files on `classes`: one for the concrete class and another for the corresponding interface).

```python
# classes/todo_item_collection_interface.py
from ..partials.with_core.todo_item_collection_interface import (
  TodoItemCollectionInterface as WithBaseInterface,
)

class TodoItemCollectionInterface(
  WithBaseInterface,
  Protocol,
):
  pass
```

```python
# classes/todo_item_collection.py
from ..partials.with_core.todo_item_collection import (
  TodoItemCollection as WithBase,
)
from .todo_item_collection_interface import (
  TodoItemCollectionInterface as ImplementsInterface,
)

class TodoItemCollection(
  WithBase,
  ImplementsInterface,
):
  pass
```

We do the same for `Todoable` and its interface on `classes`:

```python
# classes/todoable_interface.py
from ..partials.with_core.todoable_interface import (
  TodoableInterface as WithBaseInterface,
)

class TodoableInterface(
  WithBaseInterface,
  Protocol,
):
  pass
```

```python
# classes/todoable.py
from ..partials.with_core.todoable import (
  Todoable as WithBase,
)
from .todoable_interface import (
  TodoableInterface as ImplementsInterface,
)

class Todoable(
  WithBase,
  ImplementsInterface,
):
  pass
```

Done. We have the MVP implemented, however, it doesn't do much yet. It only returns an empty list.

Let's implement the "with_crud_todo_list" partial. This partial will add CRUD functionality to the todo list.

First, we need to define which other partials our "with_crud_todo_list" partial depends on. Here, the partial depends on the "with_core" partial. As we known, all partials depend on at least the "with_core" partial - the exception is the "with_core" partial, which doesn't depends on any other partial.

Now that we know the partial's dependencies, we can start implementing it:

```python
# partials/with_crud_todo_list/todo_item_collection_interface_mixin.py
from ..with_core.todo_item_collection_interface import (
  TodoItemCollectionInterface as WithBaseInterface,
)

class TodoItemCollectionInterfaceMixin(
  WithBaseInterface,
  Protocol,
):
  def create(self, item: str): ...
  def list_items(self):
  def read(self, index: int): ...
  def update(self, index: int, item: str): ...
  def delete(self, index: int): ...
```

On a partial interface, we import all mixins from the other partials that this partial depends on (related to the same base interface). We use these imported interfaces to compose the local interface mixin.

We always rename the imported mixins to the same name as the partial folder they are from. That's because they all have the same name. Notice that "WithBaseInterface" is a base class, not a mixin. That's why it was not renamed to "WithCore". For imported interfaces, we follow the same logic, plus "Interface".

After declaring the interfaces, let's implement their methods:

```python
# partials/with_crud_todo_list/todo_item_collection_mixin.py
from .todo_item_collection_interface_mixin import (
  TodoItemCollectionInterfaceMixin as ImplementsInterface,
)

class TodoItemCollectionMixin(ImplementsInterface):
  def create(self, item: str):
    self._get_items().append(item)

  def list_items(self):
    return self._get_items()

  def read(self, index: int):
    return self._get_items()[index]

  def update(self, index: int, item: str):
    self._get_items()[index] = item

  def delete(self, index: int):
    del self._get_items()[index]
```

We always import the interface mixin from the same folder. We rename this local imported interface to the same name as the base interface. This local interface contains the methods that we need to implement plus the methods that are available to use.

Usually, a concrete mixin class only inherits `ImplementsInterface`. However, in rare cases, it may inherit other classes. For example, when the partial applies an external trait. The implementation is achieved by adding the concrete version of the trait instead of actually coding the methods.

Now we have the partial implemented, we can add it to the composition on `classes`:

```python
# classes/todo_item_collection_interface.py
from ..partials.with_core.todo_item_collection_interface import (
  TodoItemCollectionInterface as WithBaseInterface,
)
from ..partials.with_crud_todo_list.todo_item_collection_interface_mixin import (
  TodoItemCollectionInterfaceMixin as WithCrudTodoListInterface,
)

class TodoItemCollectionInterface(
  WithCrudTodoListInterface,
  WithBaseInterface,
  Protocol,
):
  pass
```

```python
# classes/todo_item_collection.py
from ..partials.with_core.todo_item_collection import (
  TodoItemCollection as WithBase,
)
from ..partials.with_crud_todo_list.todo_item_collection_mixin import (
  TodoItemCollectionMixin as WithCrudTodoList,
)
from .todo_item_collection_interface import (
  TodoItemCollectionInterface as ImplementsInterface,
)

class TodoItemCollection(
  WithCrudTodoList,
  WithBase,
  ImplementsInterface,
):
  pass
```

There's no need to change the `Todoable` class on `classes`, as there's no mixin for it on the "with_crud_todo_list" partial.
