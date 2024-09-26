from .core.builderable.builderable import Builderable
from .core.builderable.types import TBuilderOutput, TBuilderPart
from .traits.with_immutability.with_immutability import WithImmutability
from .traits.with_parts.with_parts import WithParts

# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.1.0"

# Expose the public API
__all__ = [
    # Core
    "Builderable",
    "TBuilderOutput",
    "TBuilderPart",
    # Traits
    "WithImmutability",
    "WithParts",
]
