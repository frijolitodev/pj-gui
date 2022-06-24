from abc import abstractmethod
from attr import dataclass
import pandas as pd
from sympy import lambdify, symbols
from pylatex import Document, Section, Subsection, Tabular, Math, Figure, Alignat

class Method:
    table: dict

    def __init__(self, fn) -> None:
        self.result = 0
        self.iterations = 0
        self.error = 0

        x = symbols('x')
        self.fn = lambdify(x, fn, ["numpy"])

    @abstractmethod    
    def to_info(self):
        pass

    def table_init(self, params):
        self.table = dict((key, []) for key in params)

    def table_filler(self, keys, values):
        for key, val in zip(keys, values):
            self.table[key].append(val)

    def dataframe(self):
        return pd.DataFrame(self.table)

    def abs_err(self, a, b):
        return abs(b - a)

@dataclass
class MethodDetails:
    iterations: int
    error: float