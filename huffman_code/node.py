from dataclasses import dataclass, field
from typing import Optional


@dataclass(order=True)
class Node:
    weight: int
    char: Optional[str] = field(compare=False, default=None)
    left: Optional["Node"] = field(compare=False, default=None)
    right: Optional["Node"] = field(compare=False, default=None)
