# Partial Classes

A partial class is a construct to split a class definition across multiple source files.

Each partial class contains a section of the overall class definition. All parts are then combined into a single, complete class.

```text
class Partial1
├── method1
└── method2

class Partial2
├── method3
└── method4

...

class ClassA
├── Partial1
├── ...
└── PartialN
```

There are several situations when splitting a class definition is desirable:

- **Modularity**: Break a large class into smaller, more manageable pieces.
- **Organization**: Group related methods together for better organization.
- **Collaboration**: Enable team members to work on different parts simultaneously.

## Partial Classes vs. Traits

While both partial classes and traits allow you to split a class's functionality, they serve different purposes.

**Partial classes** are used to split a single class into multiple parts.

**Traits**, on the other hand, provide reusable methods that can be incorporated into multiple classes.

## Implementation

Some languages, like C#, have built-in support for partial classes. In C#, you can define a class in multiple files using the `partial` keyword.

Other languages, like Python, don't have built-in support for partial classes. However, you can achieve similar functionality by using traits, mixins, multiple inheritance, or a chained single inheritance pattern.

## CCS1-Python: A Convention for Partial Classes in Python

This section introduces a convention for implementing partial classes in Python, focusing on simple, individual classes. In later sections, we'll explore how to extend this approach horizontally across groups of classes, which is particularly useful when partials represent features in a project or package.

The approach consists of three main components:

1. **Base Class**: Defines the core functionality of the class.
2. **Partials**: Partial classes that add additional functionality.
3. **Composed Class**: Combines the base class and partials into a single class.

The recommended file structure is:

```text
<class_name>/
├── <class_name>_base.py       # Base class with core functionality
├── partials/                  # Folder containing all partial implementations
│   ├── with_<partial1>.py
│   ├── with_<partial2>.py
│   ├── ...
│   └── with_<partialN>.py
└── <class_name>.py            # Composed class: base + partials
```

In this convention, the base class is considered a special kind of partial that contains the core functionality. Partial classes are named using the pattern `With<PartialName>` and are stored in the `partials` folder.

Each class also has a corresponding interface, defined as a protocol, to enforce the expected behavior:

```text
<class_name>/
├── ...                                  # Previous structure
├── <class_name>_base_interface.py       # Interface for the base class
├── partials/                            # Folder containing all partial interfaces
│   ├── with_<partial1>_interface.py
│   ├── with_<partial2>_interface.py
│   ├── ...
│   └── with_<partialN>_interface.py
└── <class_name>_interface.py            # Composed interface: base + partial interfaces
```

By following this convention, you can organize your code for better modularity and maintainability when working with simple classes.

### Rules for Importing and Renaming

Before diving into the example, let's outline the import and renaming conventions used in this approach:

1. **Concrete Classes and Their Interfaces**: Each concrete class—whether it's base, partial, or composed—has a corresponding interface. A concrete class must always import its corresponding interface. When importing, rename the interface to `ImplementsInterface`.

    ```python
    # partials/with_partial1_interface.py
    from typing import Protocol

    class WithPartial1Interface(Protocol):
        # ... list of methods
    ```

    ```python
    # partials/with_partial1.py
    from .with_partial1_interface import WithPartial1Interface as ImplementsInterface

    class WithPartial1(ImplementsInterface):
        # ... implementation
    ```

    `ImplementsInterface` must always be the last item in the inheritance list to avoid MRO conflicts.

    ```python
    # cat.py
    from .partials.with_partial1 import WithPartial1
    from .cat_base import CatBase as WithBase
    from .cat_interface import CatInterface as ImplementsInterface

    class Cat(
        WithPartial1,
        WithBase,
        ImplementsInterface,  # Must be the last item
    ):
        ...
    ```

2. **Importing Base Classes**: When importing a base class or its interface into another module, rename them to `WithBase` and `WithBaseInterface`, respectively. This distinguishes the base class from other components and maintains naming consistency.

    ```python
    # cat_interface.py
    from .cat_base_interface import CatBaseInterface as WithBaseInterface

    class CatInterface(
        WithBaseInterface,  # Renamed to WithBaseInterface
        Protocol,
    ):
        ...
    ```

    ```python
    # cat.py
    from .cat_base import CatBase as WithBase
    from .cat_interface import CatInterface as ImplementsInterface

    class Cat(
        WithBase,  # Renamed to WithBase
        ImplementsInterface,
    ):
        ...
    ```

3. **Partial Interface Inheritance List**: A partial interface must import the interfaces of any other partials it depends on. This ensures that all necessary methods and attributes are available. It also must import the base interface and `Protocol`.

    ```python
    # partials/with_partial3_interface.py
    from .with_partial1_interface import WithPartial1Interface
    from .with_partial2_interface import WithPartial2Interface
    from ..cat_base_interface import CatBaseInterface as WithBaseInterface
    from typing import Protocol

    class WithPartial3Interface(
        WithPartial2Interface,  # Dependency: methods from Partial2
        WithPartial1Interface,  # Dependency: methods from Partial1
        WithBaseInterface,      # Base interface
        Protocol,
    ):
        ...
    ```

    The inheritance list must be ordered from the most specific (newer dependencies) to the most general (base dependencies), followed by the base class interface and `Protocol` to avoid MRO resolution conflicts.

4. **Partial Class Inheritance List**: The concrete class of a partial should import its corresponding interface `ImplementsInterface`. It must not import the base class, other partial classes, or their interfaces, even when it depends on them.

    ```python
    # partials/with_partial3.py
    from .with_partial3_interface import WithPartial3Interface as ImplementsInterface

    # MUST NOT import Base Class, Partial1, or Partial2, even though it uses their methods
    class WithPartial3(ImplementsInterface):
        # ... implementation
    ```

    Partial classes often only inherit `ImplementsInterface`; however, they can inherit other classes, as long as they are external concrete classes, like traits.

    ```python
    # partials/with_partial3.py
    from external_module import SomeTrait
    from .with_partial3_interface import WithPartial3Interface as ImplementsInterface

    class WithPartial3(
        SomeTrait,
        ImplementsInterface,
    ):
        # ... implementation
    ```

5. **Composed Interface Inheritance List**: The composed interface must import all partial interfaces and the base interface.

    ```python
    # cat_interface.py
    from .partials.with_partial3_interface import WithPartial3Interface
    from .partials.with_partial2_interface import WithPartial2Interface
    from .partials.with_partial1_interface import WithPartial1Interface
    from .cat_base_interface import CatBaseInterface as WithBaseInterface
    from typing import Protocol

    class CatInterface(
        WithPartial3Interface,  # Higher-level partials first
        WithPartial2Interface,
        WithPartial1Interface,  # Lower-level partials last
        WithBaseInterface,      # Base interface
        Protocol,               # Must be the last item
    ):
        ...
    ```

    The order of interfaces in the inheritance list is crucial to ensure that the MRO works correctly:

    - `With<...>` (all partials, from newer to older), then
    - `WithBaseInterface` (the base interface), followed by
    - `Protocol`.

6. **Composed Class Inheritance List**: The concrete composed class should import the concrete classes of all partials, the concrete base class (`WithBase`), and its own composed interface (`ImplementsInterface`). The inheritance list must follow this order to respect Python's MRO and ensure proper method resolution.

    ```python
    # cat.py
    from .partials.with_partial3 import WithPartial3
    from .partials.with_partial2 import WithPartial2
    from .partials.with_partial1 import WithPartial1
    from .cat_base import CatBase as WithBase
    from .cat_interface import CatInterface as ImplementsInterface

    class Cat(
        WithPartial3,         # Higher-level partials first
        WithPartial2,
        WithPartial1,         # Lower-level partials last
        WithBase,             # Base class
        ImplementsInterface,  # Interface must be the last item
    ):
        ...
    ```

7. **Composed Classes Must Be Empty**: The composed class and its interface should not contain any methods or attributes. They only serve to combine the base class and partials. If you need to add additional methods or attributes, consider creating a new partial.

    ```python
    # cat_interface.py
    class CatInterface(
        WithPartial3Interface,
        WithPartial2Interface,
        WithPartial1Interface,
        WithBaseInterface,
        Protocol,
    ):
        pass  # Body must be empty
    ```

    ```python
    # cat.py
    class Cat(
        WithPartial3,
        WithPartial2,
        WithPartial1,
        WithBase,
        ImplementsInterface,
    ):
        pass  # Body must be empty
    ```

### Example: `Vehicle` Class

Let's create a `Vehicle` class with methods for controlling a vehicle's basic operations, managing speed, and calculating travel time.

**Core functionality:**

- `start()`: Starts the vehicle.
- `stop()`: Stops the vehicle.

**Speed management:**

- `set_speed(speed: float)`: Sets the speed of the vehicle.
- `get_speed()`: Retrieves the current speed of the vehicle.

**Travel time calculation:**

- `calculate_travel_time(distance: float)`: Calculates the time required to travel a given distance at the current speed.

**Usage example:**

```python
vehicle = Vehicle()
vehicle.start()
vehicle.set_speed(80.0)
time = vehicle.calculate_travel_time(240.0)
print(f"Estimated travel time: {time} hours")
vehicle.stop()
```

We will split the class code into three parts:

- `VehicleBase`: Base class with core functionality.
- `WithSpeed`: Partial for managing speed.
- `WithTravelTime`: Partial for calculating travel time.

#### Base Class: `VehicleBase`

The base class with core functionality.

**Interface:**

```python
# vehicle/vehicle_base_interface.py
from typing import Protocol

class VehicleBaseInterface(Protocol):
    def start(self) -> None: ...
    def stop(self) -> None: ...
```

**Implementation:**

```python
# vehicle/vehicle_base.py
from .vehicle_base_interface import VehicleBaseInterface as ImplementsInterface

class VehicleBase(ImplementsInterface):
    _is_running: bool = False

    def start(self) -> None:
        self._is_running = True

    def stop(self) -> None:
        self._is_running = False
```

#### First Partial: `WithSpeed`

The first partial adds speed-related methods.

**Interface:**

```python
# vehicle/partials/with_speed_interface.py
from ..vehicle_base_interface import VehicleBaseInterface as WithBaseInterface
from typing import Protocol

class WithSpeedInterface(
    WithBaseInterface,  # Base interface
    Protocol,
):
    def set_speed(self, speed: float) -> None: ...
    def get_speed(self) -> float: ...
```

**Implementation:**

```python
# vehicle/partials/with_speed.py
from .with_speed_interface import WithSpeedInterface as ImplementsInterface

class WithSpeed(ImplementsInterface):
    _speed: float = 0.0

    def set_speed(self, speed: float) -> None:
        self._speed = speed

    def get_speed(self) -> float:
        return self._speed
```

#### Second Partial: `WithTravelTime`

The second partial depends on the `get_speed` method from the first partial to calculate travel time.

**Interface:**

```python
# vehicle/partials/with_travel_time_interface.py
from .with_speed_interface import WithSpeedInterface
from ..vehicle_base_interface import VehicleBaseInterface as WithBaseInterface
from typing import Protocol

class WithTravelTimeInterface(
    WithSpeedInterface,  # Dependency: methods from WithSpeed
    WithBaseInterface,   # Base interface
    Protocol,
):
    def calculate_travel_time(self, distance: float) -> float: ...
```

**Implementation:**

```python
# vehicle/partials/with_travel_time.py
from .with_travel_time_interface import WithTravelTimeInterface as ImplementsInterface

class WithTravelTime(ImplementsInterface):
    def calculate_travel_time(self, distance: float) -> float:
        speed = self.get_speed()
        return distance / speed if speed != 0 else float('inf')
```

#### Composed Interface: `VehicleInterface`

The composed interface combines all interfaces.

```python
# vehicle/vehicle_interface.py
from .partials.with_travel_time_interface import WithTravelTimeInterface
from .partials.with_speed_interface import WithSpeedInterface
from .vehicle_base_interface import VehicleBaseInterface as WithBaseInterface
from typing import Protocol

class VehicleInterface(
    WithTravelTimeInterface,  # Higher-level partials first
    WithSpeedInterface,       # Lower-level partials last
    WithBaseInterface,        # Base interface
    Protocol,                 # Must be the last item
):
    pass
```

#### Composed Class: `Vehicle`

The composed class combines the base class and all partials.

```python
# vehicle/vehicle.py
from .partials.with_travel_time import WithTravelTime
from .partials.with_speed import WithSpeed
from .vehicle_base import VehicleBase as WithBase
from .vehicle_interface import VehicleInterface as ImplementsInterface

class Vehicle(
    WithTravelTime,        # Higher-level partials first
    WithSpeed,             # Lower-level partials last
    WithBase,              # Base class
    ImplementsInterface,   # Must be the last item
):
    pass
```

#### Usage Example

Now you can use the `Vehicle` class as a single, cohesive unit:

```python
vehicle = Vehicle()
vehicle.start()
vehicle.set_speed(60.0)
time = vehicle.calculate_travel_time(120.0)
print(f"Travel time: {time} hours")
vehicle.stop()

# Output:
# Travel time: 2.0 hours
```

## Horizontal Partials Approach

In the previous section, we focused on implementing partial classes in Python for individual classes. Now, we'll explore an alternative approach that applies partials horizontally across a group of classes. This method is particularly useful when partials represent features that are shared across multiple classes within a project or package.

The file structure for this approach is:

```text
<package_name>/
├── partials/                        # Folder storing the partials
│   ├── with_core/                   # Package's core features
│   │   ├── <class1>_base.py
│   │   ├── ...
│   │   └── <classN>_base.py
│   │
│   ├── with_<feature1>/             # Package's feature 1
│   │   ├── <class...>_base.py       # Optional: New base classes for the package
│   │   └── <class...>_partial.py    # Optional: Partial classes for base classes from other features
│   │
│   ├── ...
│   │
│   └── with_<featureN>/             # Package's feature N
│       └── ...
│
└── classes/                         # Folder for composed classes
    ├── <class1>.py
    ├── ...
    └── <classN>.py
```

- **`partials/with_core/`**: Package's core features.
- **`partials/with_<feature>/`**: Package's extra features; Contains base classes and partials for classes.
- **`classes/`**: Stores the composed classes.

Each concrete class has a corresponding interface, stored in the same directory.

### Key Rules and Conventions

Most of the rules from the previous approach apply here, with some differences:

1. **Partial Names**: Partial classes have the same name as their base class but with the suffixes `Partial` and `PartialInterface` for the class and interface, respectively.

    ```text
    <package_name>/
    ├── partials/
    │   ├── with_core/
    │   │   ├── vehicle_base.py
    │   │   └── vehicle_base_interface.py
    │   │
    │   ├── with_speed/
    │   │   ├── vehicle_partial.py
    │   │   └── vehicle_partial_interface.py
    │   │
    │   └── with_travel_time/
    │       ├── vehicle_partial.py
    │       └── vehicle_partial_interface.py
    │
    └── classes/
        ├── vehicle.py
        └── vehicle_interface.py
    ```

2. **Importing Partials**: When importing a partial class, rename it to `With<PartialName>` and `With<PartialName>Interface` for its interface.

    ```python
    # classes/vehicle_interface.py
    from ..partials.with_travel_time.vehicle_partial_interface import VehiclePartialInterface as WithTravelTimeInterface
    from ..partials.with_speed.vehicle_partial_interface import VehiclePartialInterface as WithSpeedInterface
    from ..partials.with_core.vehicle_interface import VehicleInterface as WithBaseInterface

    class VehicleInterface(
        WithTravelTimeInterface, # Renamed partial interface
        WithSpeedInterface,      # Renamed partial interface
        WithBaseInterface,
        Protocol,
    ):
        pass
    ```

    ```python
    # classes/vehicle.py
    from ..partials.with_travel_time.vehicle_partial import VehiclePartial as WithTravelTime
    from ..partials.with_speed.vehicle_partial import VehiclePartial as WithSpeed
    from ..partials.with_core.vehicle import Vehicle as WithBase
    from .vehicle_interface import VehicleInterface as ImplementsInterface

    class Vehicle(
        WithTravelTime,  # Renamed partial class
        WithSpeed,       # Renamed partial class
        WithBase,
        ImplementsInterface,
    ):
        pass
    ```

3. **Base Classes in `classes/` Folder**: All base classes must have an entry in the `classes/` folder, along with their corresponding interfaces.

    ```text
    <package_name>/
    ├── partials/
    │   │   ...   # previous structure
    │   │
    │   ├── with_engine/   # Now, vehicles have an engine instance
    │   │   ├── engine_base.py
    │   │   ├── engine_base_interface.py
    │   │   ├── vehicle_partial.py
    │   │   └── vehicle_partial_interface.py
    │
    └── classes/
        ├── vehicle.py
        ├── vehicle_interface.py
        ├── engine.py   # New base class (from `partials/with_engine`)
        └── engine_interface.py
    ```

### Example: Horizontal Partials

In this example, we'll create a `Transport` package that demonstrates the horizontal partials approach. We start with a core partial that defines a `Vehicle` base class. Then, we'll introduce another partial that adds an `Engine` base class and extends `Vehicle` to include an engine. Finally, we'll create a partial that extends both `Vehicle` and `Engine` to add fuel management functionality.

#### Package Structure

```text
transport/
├── partials/
│   ├── with_core/
│   │   ├── vehicle_base.py
│   │   └── vehicle_base_interface.py
│   │
│   ├── with_engine/
│   │   ├── engine_base.py
│   │   ├── engine_base_interface.py
│   │   ├── vehicle_partial.py
│   │   └── vehicle_partial_interface.py
│   │
│   ├── with_fuel/
│   │   ├── vehicle_partial.py
│   │   ├── vehicle_partial_interface.py
│   │   └── engine_partial.py
│       └── engine_partial_interface.py
│
└── classes/
    ├── vehicle.py
    ├── vehicle_interface.py
    ├── engine.py
    └── engine_interface.py
```

#### Core Partial: `with_core`

**`VehicleBase` Interface**

```python
# partials/with_core/vehicle_base_interface.py
from typing import Protocol

class VehicleBaseInterface(Protocol):
    def start(self) -> None: ...
    def stop(self) -> None: ...
```

**`VehicleBase` Implementation**

```python
# partials/with_core/vehicle_base.py
from .vehicle_base_interface import VehicleBaseInterface as ImplementsInterface

class VehicleBase(ImplementsInterface):
    _is_running: bool = False

    def start(self) -> None:
        self._is_running = True

    def stop(self) -> None:
        self._is_running = False
```

#### Partial: `with_engine`

Introduces an `EngineBase` class and extends `Vehicle` to include an engine.

**`EngineBase` Interface**

```python
# partials/with_engine/engine_base_interface.py
from typing import Protocol

class EngineBaseInterface(Protocol):
    def ignite(self) -> None: ...
    def shutdown(self) -> None: ...
```

**`EngineBase` Implementation**

```python
# partials/with_engine/engine_base.py
from .engine_base_interface import EngineBaseInterface as ImplementsInterface

class EngineBase(ImplementsInterface):
    _is_running: bool = False

    def ignite(self) -> None:
        self._is_running = True

    def shutdown(self) -> None:
        self._is_running = False
```

**`VehiclePartial` Interface**

```python
# partials/with_engine/vehicle_partial_interface.py
from ..with_core.vehicle_base_interface import VehicleBaseInterface as WithBaseInterface
from .engine_base_interface import EngineBaseInterface
from typing import Protocol

class VehiclePartialInterface(
    EngineBaseInterface,    # New base class interface
    WithBaseInterface,      # Original base interface
    Protocol,
):
    def get_engine(self) -> EngineBaseInterface: ...
    def start(self) -> None    # Overriding start method
    def stop(self) -> None     # Overriding stop method
```

**`VehiclePartial` Implementation**

```python
# partials/with_engine/vehicle_partial.py
from .vehicle_partial_interface import VehiclePartialInterface as ImplementsInterface
from .engine_base import EngineBase

class VehiclePartial(ImplementsInterface):
    def __init__(self):
        super().__init__()
        self._engine = EngineBase()

    def get_engine(self) -> EngineBase:
        return self._engine

    def start(self) -> None:
        self._engine.ignite()
        super().start()

    def stop(self) -> None:
        self._engine.shutdown()
        super().stop()
```

#### Partial: `with_fuel`

Extends both `Vehicle` and `Engine` to add fuel management.

**`EnginePartial` Interface**

```python
# partials/with_fuel/engine_partial_interface.py
from ..with_engine.engine_base_interface import EngineBaseInterface as WithBaseInterface
from typing import Protocol

class EnginePartialInterface(
    WithBaseInterface,
    Protocol,
):
    def consume_fuel(self, amount: float) -> None: ...
    def get_fuel_level(self) -> float: ...
```

**`EnginePartial` Implementation**

```python
# partials/with_fuel/engine_partial.py
from .engine_partial_interface import EnginePartialInterface as ImplementsInterface

class EnginePartial(ImplementsInterface):
    _fuel_level: float = 0.0

    def consume_fuel(self, amount: float) -> None:
        if self._fuel_level >= amount:
            self._fuel_level -= amount
        else:
            raise RuntimeError("Not enough fuel.")

    def get_fuel_level(self) -> float:
        return self._fuel_level

    def refuel(self, amount: float) -> None:
        self._fuel_level += amount

    def ignite(self) -> None:
        if self._fuel_level <= 0:
            raise RuntimeError("Cannot ignite engine: no fuel.")
        super().ignite()
```

**`VehiclePartial` Interface**

```python
# partials/with_fuel/vehicle_partial_interface.py
from ..with_engine.vehicle_partial_interface import VehiclePartialInterface as WithEngineInterface
from typing import Protocol

class VehiclePartialInterface(
    WithEngineInterface,
    Protocol,
):
    def refuel(self, amount: float) -> None: ...
    def get_fuel_level(self) -> float: ...
```

**`VehiclePartial` Implementation**

```python
# partials/with_fuel/vehicle_partial.py
from .vehicle_partial_interface import VehiclePartialInterface as ImplementsInterface

class VehiclePartial(ImplementsInterface):
    def refuel(self, amount: float) -> None:
        self.get_engine().refuel(amount)

    def get_fuel_level(self) -> float:
        return self.get_engine().get_fuel_level()

    def start(self) -> None:
        self.get_engine().consume_fuel(1.0)  # Consume 1 unit of fuel on start
        super().start()
```

#### Composed Classes

**`EngineInterface`**

```python
# classes/engine_interface.py
from ..partials.with_fuel.engine_partial_interface import EnginePartialInterface as WithFuelInterface
from ..partials.with_engine.engine_base_interface import EngineBaseInterface as WithBaseInterface
from typing import Protocol

class EngineInterface(
    WithFuelInterface,
    WithBaseInterface,
    Protocol,
):
    pass
```

**`Engine`**

```python
# classes/engine.py
from ..partials.with_fuel.engine_partial import EnginePartial as WithFuel
from ..partials.with_engine.engine_base import EngineBase as WithBase
from .engine_interface import EngineInterface as ImplementsInterface

class Engine(
    WithFuel,
    WithBase,
    ImplementsInterface,
):
    pass
```

**`VehicleInterface`**

```python
# classes/vehicle_interface.py
from ..partials.with_fuel.vehicle_partial_interface import VehiclePartialInterface as WithFuelInterface
from ..partials.with_engine.vehicle_partial_interface import VehiclePartialInterface as WithEngineInterface
from ..partials.with_core.vehicle_base_interface import VehicleBaseInterface as WithBaseInterface
from typing import Protocol

class VehicleInterface(
    WithFuelInterface,
    WithEngineInterface,
    WithBaseInterface,
    Protocol,
):
    pass
```

**`Vehicle`**

```python
# classes/vehicle.py
from ..partials.with_fuel.vehicle_partial import VehiclePartial as WithFuel
from ..partials.with_engine.vehicle_partial import VehiclePartial as WithEngine
from ..partials.with_core.vehicle_base import VehicleBase as WithBase
from .vehicle_interface import VehicleInterface as ImplementsInterface

class Vehicle(
    WithFuel,
    WithEngine,
    WithBase,
    ImplementsInterface,
):
    pass
```

#### Usage Example

```python
vehicle = Vehicle()
vehicle.refuel(10.0)  # Add 10 units of fuel
vehicle.start()
print(f"Fuel level: {vehicle.get_fuel_level()} units")
vehicle.stop()
```

**Output:**

```
Fuel level: 9.0 units
```
