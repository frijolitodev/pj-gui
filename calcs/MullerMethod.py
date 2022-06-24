import math
import pandas as pd

from calcs.Method import Method, MethodDetails

class MullerMethod(Method):
    tabulacion: pd.DataFrame

    def __init__(self, fn, x0, x1, x2, tol):
        self.fn = fn
        
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        
        self.tol = tol
        self.calc()

    def calc(self):
        res = 0
        iterations = 0
        xa_list = []
        xb_list = []
        xc_list = []
        xr_list = []
        err_list = []
        a_list = []
        b_list = []
        c_list = []

        while (True):
            iterations = iterations + 1
            
            f1 = self.fn(self.x0)
            f2 = self.fn(self.x1)
            f3 = self.fn(self.x2)

            d1 = f1 - f3
            d2 = f2 - f3
            
            h1 = self.x0 - self.x2
            h2 = self.x1 - self.x2
            
            a0 = f3
            a1 = (((d2 * pow(h1, 2)) - (d1 * pow(h2, 2))) / ((h1 * h2) * (h1 - h2)))
            a2 = (((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2))) 

            x = ((-2 * a0) / (a1 + abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))
            y = ((-2 * a0) / (a1 - abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))

            # Tomando raiz mas cercana x0 x_2
            if (x >= y):
                res = x + self.x2
            else:
                res = y + self.x2
                
            # Calculando error
            err = self.abs_err(res - self.x2)

            # Guardando datos en las listas
            xa_list.append(self.x0)
            xb_list.append(self.x1)
            xc_list.append(self.x2)
            
            c_list.append(a0)
            a_list.append(a2)
            b_list.append(a1)
            
            xr_list.append(res)
            err_list.append(err)

            self.x0 = self.x1
            self.x1 = self.x2
            self.x2 = res
            self.error = err
            self.iterations = iterations

            if (err <= self.tol):
                self.result = res
                break
        
        Table = {
            "x_a": xa_list,
            "x_b": xb_list,
            "x_c": xc_list,
            "a": a_list,
            "b": b_list,
            "c": c_list,
            "x_r": xr_list,
            "err": err_list
        }

        self.tabulacion = pd.DataFrame(Table)

    def to_info(self):
        return [self.fn, self.tabulacion, self.result, MethodDetails(self.iterations, self.error)]

