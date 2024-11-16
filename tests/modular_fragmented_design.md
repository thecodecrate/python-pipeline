# Partial Classes

Partial classes enable you to split a class definition across multiple source files.

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

- **Modularity**: To break a large class into smaller, more manageable pieces.
- **Organization**: To group related methods together for better organization.
- **Collaboration**: To enable team members to work on different parts simultaneously.

## Partial Classes vs. Traits

While both partial classes and traits allow you to split a class's functionality, they serve different purposes.

**Partial classes** are used to split a single class into multiple parts.

**Traits**, on the other hand, provide reusable methods that can be incorporated into multiple classes.

## Implementation

Some languages, like C#, have built-in support for partial classes. In C#, you can define a class in multiple files using the `partial` keyword.

Other languages, like Python, don't have built-in support for partial classes. However, you can achieve similar functionality by using traits, mixins, multiple inheritance, or a chained single inheritance pattern.

## A Convention for Implementing Partial Classes in Python

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

### Import and Renaming Rules

Before diving into the example, let's outline the import and renaming conventions used in this approach:

1. **Concrete Classes Import Their Interfaces**: Every concrete class (base, partial, or composed) should import its corresponding interface. When importing, the interface should be renamed to `ImplementsInterface`.

2. **Consistency Across All Classes**: The above rule applies to all types of classes—base classes, partials, and composed classes.

3. **Partial Interfaces Import Dependencies**: The interface of a partial should import the interfaces of its dependencies.

4. **Renaming Base Interfaces**: When importing a base class or its interface, it should be renamed to `WithBase` or `WithBaseInterface`, respectively.

5. **Importing Order Matters**: The order of imports and inheritance lists is crucial due to Python's Method Resolution Order (MRO).

6. **Inheritance Order in Partial Interfaces**: In partial interfaces, the inheritance list should include the interfaces of the partials it depends on (with newer dependencies on top and more basic ones at the bottom), followed by `Protocol` to provide type-hint support.

7. **Concrete Partials Avoid Other Partials**: The concrete class of a partial should only import its corresponding interface (renamed to `ImplementsInterface`) and must not import other partials. However, it can import external concrete classes like traits.

8. **Composed Interface Imports**: The composed interface must import the interfaces of all partials and the base interface (renamed as `WithBaseInterface`), then inherit from them in the specified order, followed by `Protocol`.

9. **Composed Class Imports**: The concrete composed class should import the concrete classes of all partials, the concrete base class (renamed as `WithBase`), and the composed interface (renamed as `ImplementsInterface`). The inheritance list should follow this order due to Python's MRO.

### Example: `Vehicle` Class

Let's create a `Vehicle` class split into two partials: one for managing speed and another for calculating travel time, where the second partial depends on a method declared in the first partial.

#### Base Class: `VehicleBase`

The base class contains core functionality.

**Interface**:

```python
# vehicle/vehicle_base_interface.py
class VehicleBaseInterface(Protocol):
    def start(self) -> None: ...
    def stop(self) -> None: ...
```

**Implementation**:

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

**Explanation**:

- **Rule 1 & 2**: The concrete class `VehicleBase` imports its corresponding interface `VehicleBaseInterface`, renaming it to `ImplementsInterface`.
- **Rule 4**: When importing the base interface elsewhere, we'll rename it to `WithBaseInterface`.

#### First Partial: `WithSpeed`

The first partial adds speed-related methods.

**Interface**:

```python
# vehicle/partials/with_speed_interface.py
from ..vehicle_base_interface import VehicleBaseInterface as WithBaseInterface

class WithSpeedInterface(WithBaseInterface, Protocol):
    def set_speed(self, speed: float) -> None: ...
    def get_speed(self) -> float: ...
```

**Implementation**:

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

**Explanation**:

- **Rule 1 & 2**: `WithSpeed` imports its interface `WithSpeedInterface` as `ImplementsInterface`.
- **Rule 3 & 6**: The interface `WithSpeedInterface` imports its dependency `VehicleBaseInterface` (renamed to `WithBaseInterface`) and inherits from it, followed by `Protocol`.
- **Rule 4**: Renaming `VehicleBaseInterface` to `WithBaseInterface` when importing.
- **Rule 7**: The concrete partial `WithSpeed` only imports its corresponding interface and does not import other partials.

#### Second Partial: `WithTravelTime`

The second partial depends on the `get_speed` method from the first partial to calculate travel time.

**Interface**:

```python
# vehicle/partials/with_travel_time_interface.py
from .with_speed_interface import WithSpeedInterface

class WithTravelTimeInterface(WithSpeedInterface, Protocol):
    def calculate_travel_time(self, distance: float) -> float: ...
```

**Implementation**:

```python
# vehicle/partials/with_travel_time.py
from .with_travel_time_interface import WithTravelTimeInterface as ImplementsInterface

class WithTravelTime(ImplementsInterface):
    def calculate_travel_time(self, distance: float) -> float:
        speed = self.get_speed()
        return distance / speed if speed != 0 else float('inf')
```

**Explanation**:

- **Rule 1 & 2**: `WithTravelTime` imports its interface as `ImplementsInterface`.
- **Rule 3 & 6**: The interface `WithTravelTimeInterface` imports its dependency `WithSpeedInterface` and inherits from it, followed by `Protocol`.
- **Rule 7**: The concrete partial `WithTravelTime` only imports its interface.

#### Composed Interface: `VehicleInterface`

The composed interface combines all interfaces.

```python
# vehicle/vehicle_interface.py
from .partials.with_travel_time_interface import WithTravelTimeInterface
from .partials.with_speed_interface import WithSpeedInterface
from .vehicle_base_interface import VehicleBaseInterface as WithBaseInterface

class VehicleInterface(
    WithTravelTimeInterface,
    WithSpeedInterface,
    WithBaseInterface,
    Protocol,
):
    pass
```

**Explanation**:

- **Rule 8**: The composed interface imports the interfaces of all partials (`WithTravelTimeInterface`, `WithSpeedInterface`), the base interface (renamed as `WithBaseInterface`), and inherits from them in the specified order, followed by `Protocol`.
- **Rule 5**: The inheritance order is important due to Python's MRO.

#### Composed Class: `Vehicle`

The composed class combines the base class and all partials.

```python
# vehicle/vehicle.py
from .partials.with_travel_time import WithTravelTime
from .partials.with_speed import WithSpeed
from .vehicle_base import VehicleBase as WithBase
from .vehicle_interface import VehicleInterface as ImplementsInterface

class Vehicle(
    WithTravelTime,
    WithSpeed,
    WithBase,
    ImplementsInterface,
):
    pass
```

**Explanation**:

- **Rule 9**: The composed class imports the concrete classes of all partials (`WithTravelTime`, `WithSpeed`), the concrete base class (renamed as `WithBase`), and the composed interface (renamed as `ImplementsInterface`).
- **Rule 5**: The inheritance list follows the specified order due to Python's MRO.

#### Usage Example

Now, you can use the `Vehicle` class as a single, cohesive unit:

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
