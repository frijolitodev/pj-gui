import sympy as sp
import numpy as np
import pandas as pd

from calcs.Method import Method, MethodDetails


class NewtonMethod(Method):
    def __init__(self, fn, z0, n_max, tol):
        pd.set_option("display.precision", 6)
        Method.__init__(self, fn)
        self.z0 = z0

        x = sp.symbols('x')
        self.fprime = sp.lambdify(x, self.fn(x).diff(x))

        self.keys = [
            "z_n", "f(z_n)", "df(fz_n)", "z_(n+1)", "Error"
        ]

        self.table_init(self.keys)

        self.n_max = n_max
        self.tol = tol
        self.calc()

    def calc(self):
        try:
            i = 0
            z0 = self.z0

            if self.fprime(z0) != 0:

                while True:
                    f_z0 = self.fn(z0)
                    df_z0 = self.fprime(z0)

                    z = z0 - (f_z0 / df_z0)
                    df_z = self.fprime(z)
                    error = self.abs_err(z0, z)

                    vals = [z0, f_z0, df_z0, z, error]
                    self.table_filler(self.keys, vals)

                    if error < self.tol or i + 1 == self.n_max or df_z == 0:
                        break

                    z0 = z
                    i += 1
                    global root
                    root = z0

            self.result = root
            self.iterations = i
            self.error = error

        except ZeroDivisionError:
            self.result = "No se puede dividir entre cero"

    def to_info(self):
        return [self.dataframe(), self.result, MethodDetails(self.iterations, self.error)]
