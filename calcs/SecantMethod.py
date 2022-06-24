from dataclasses import dataclass
import numpy as np
import pandas as pd

from calcs.Method import MethodDetails

class SecantMethod:
    tabulacion: pd.DataFrame

    def __init__(self, fx, xa, xb, tol):
        self.fx = fx
        self.xa = xa
        self.xb = xb
        self.tol = tol

        self.calc()
        self.err_abs()
        self.CorteEjex()
        self.Pendiente()

    def err_abs(self, x2, x1):
        return abs(x2 - x1)

    def Pendiente(self, x1,x2,f):
        #Se confirma que no sean los mismos puntos
        if(x1==x2):
            return 'Ingrese dos puntos distintos'
        else:
            #Se realiza el calculo de la pendiente
            m = (f(x2)-f(x1))/(x2-x1)
            return m

    def CorteEjeX(self):
        # Se obtiene la pendiente para x1 y x2
        m = self.Pendiente(self.xa,self.xb,self.fx)
        # Se realiza el calculo de xc
        x= self.xa -(1/m)*self.fx(self.xa)
        return x

    def calc(self):
        try:
            #Listas que se usaran para rellenar la tabla
            listA =[]
            listB =[]
            listC =[]
            listFa=[]
            listFb=[]
            listFc=[]
            listErr=[]
            i = 0 
            tramo = self.err_abs(self.xa,self.xb)

            if(tramo<=self.tol):
                self.result = "no se puede encontrar raices para este intervalo"

            while not(tramo<=self.tol):
                i = i + 1
                c = self.CorteEjeX(self.xa,self.xb)
                fc = self.fx(c)
                #Se añaden los datos a las listas
                listA.append(self.xa)
                listB.append(self.xb)
                listFa.append(self.fx(self.xa))
                listFb.append(self.fx(self.xb))
                listErr.append(tramo)
                listC.append(c)
                listFc.append(fc)

                if(fc == 0):
                    return c

                # Se calcula el error en funcion de xc y xa
                tramo = self.err_abs(c,self.xa)
                
                #Se intercambian los valores de xa, xb y xc
                self.xb = self.xa
                self.xa = c
        
            self.result = c
            Table ={
                "a": listA,
                "b": listB,
                "fa": listFa,
                "fb": listFb,
                "c": listC,
                "fc": listFc,
                "err": listErr
            }
            self.tabulacion = pd.DataFrame(Table)
            self.iterations = i
            self.error = tramo

        except ZeroDivisionError:
            self.result = "no se puede encontrar raices para este intervalo"

    def to_info(self):
        return [self.fx, self.tabulation, self.result, MethodDetails(self.iterations,self.error)]