from abc import abstractmethod
from attr import dataclass
import pandas as pd
from sympy import lambdify, symbols

class Method:
    table: dict

    def __init__(self, fn) -> None:
        self.result = 0
        self.iterations = 0
        self.error = 0

        x = symbols('x')
        self.fn = lambdify(x, fn, ["numpy"])

    def table_init(self, params):
        self.table = dict((key, []) for key in params)

    def table_filler(self, keys, values):
        for key, val in zip(keys, values):
            self.table[key].append(val)

    def dataframe(self):
        return pd.DataFrame(self.table)

    @abstractmethod    
    def to_info(self):
        pass

    def abs_err(self, a, b):
        return abs(b - a)

@dataclass
class MethodDetails:
    iterations: int
    error: float