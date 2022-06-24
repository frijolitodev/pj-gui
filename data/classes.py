from dataclasses import dataclass
import typing

@dataclass
class Dims:
    width: int
    height: int

@dataclass
class MethodInfo:
    disp: str
    slug: str

@dataclass 
class LatexSection:
    section: str
    data: typing.Any