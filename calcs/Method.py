from abc import abstractmethod
from attr import dataclass

class Method:
    @abstractmethod    
    def to_info(self):
        pass

    def abs_err(self, a, b):
        return abs(b - a)

@dataclass
class MethodDetails:
    iterations: int
    error: float