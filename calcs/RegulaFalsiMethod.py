from dataclasses import dataclass
import numpy as np
import pandas as pd

from calcs.Method import Method, MethodDetails

class RegulaFalsiMethod(Method):

    tabulation: pd.DataFrame

    def __init__(self, fn, xa, xb, tol):
        Method.__init__(self, fn)

        self.xa = xa
        self.xb = xb
        self.tol = tol

        self.keys = ["a", "b", "fa", "fb", "c", "fc", "Error"]
        self.table_init(self.keys)

        self.calc()

    def aprox(self, p1, p2):
        fp1 = self.fn(p1)
        fp2 = self.fn(p2)

        c = p2 - fp2*(p1-p2)/(fp1-fp2)
        return c

    def calc(self):
        try:
            iterator = 0

            section = self.abs_err(self.xa, self.xb)

            if(section <= self.tol):
                self.result = "no se puede encontrar raices para este intervalo"

            while not(section <= self.tol):
                iterator = iterator + 1
                c = self.aprox(self.xa, self.xb)
                fc = self.fn(c)

                vals = [self.xa, self.xb, self.fn(self.xa), self.fn(self.xb), section, c, fc]
                self.table_filler(self.keys, vals)

                if(fc == 0):
                    return c

                cambia = np.sign(self.fn(self.xa))*np.sign(fc)
                if (cambia > 0):
                    section = self.abs_err(c, self.xa)
                    self.xa = c
                else:
                    section = self.abs_err(self.xb, c)
                    self.xb = c
            
            self.result = c
            self.iterations = iterator
            self.error = section

        except ZeroDivisionError:
            self.result = "no se puede encontrar raices para este intervalo"

    def to_info(self):
        return [self.dataframe(), self.result, MethodDetails(self.iterations, self.error)]
