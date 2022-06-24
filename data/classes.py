from dataclasses import dataclass


@dataclass
class Dims:
    width: int
    height: int

@dataclass
class MethodInfo:
    disp: str
    slug: str