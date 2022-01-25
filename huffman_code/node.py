from dataclasses import dataclass, field
from typing import Optional


@dataclass(order=True)
class Node:
    weight: int
    char: Optional[str] = field(compare=False, default=None)
    left: Optional["Node"] = field(compare=False, default=None)
    right: Optional["Node"] = field(compare=False, default=None)

    def is_leaf(self):
        return self.char is not None
