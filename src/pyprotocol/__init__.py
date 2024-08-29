"""Commonly used protocols for type hinting."""

from typing import Protocol as _Protocol


class Stringable(_Protocol):
    """An object that can be converted to a string,
    i.e., has a `__str__` method."""

    def __str__(self) -> str:
        ...
