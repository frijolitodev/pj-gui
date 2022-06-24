from abc import abstractmethod
from tkinter import *

from calcs.Method import Method

from calcs.SecantMethod import SecantMethod

class MainPanel:
    method_calc: Method

    def __init__(self, root, frame, slug, onLoad) -> None:
        self.root = root
        self.frame = frame

        if onLoad is not None:
            onLoad()

    @abstractmethod
    def calc_init(self, params):
        pass

class SecantPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Secante", onLoad)

        Label(self.frame, text="Valor para xa:").grid(row=0, column=1)
        self.xaEntry = Entry(self.frame, relief="raised")
        self.xaEntry.grid(row=0,column=2,columnspan=3)

        Label(self.frame, text="Valor para xb:").grid(row=1, column=1)
        self.xbEntry = Entry(self.frame, relief="raised")
        self.xbEntry.grid(row=1, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=2, column=1)
        self.tolEntry = Entry(self.frame, relief="raised")
        self.tolEntry.grid(row=2, column=2, columnspan=3)

    def calc_init(self, params):
        fn = params

        try:
            xa = float(self.xaEntry.get())
            xb = float(self.xbEntry.get())
            tol = float(self.tolEntry.get())

            self.method_calc = SecantMethod(fn, xa, xb, tol)
            print(self.method_calc.to_info())

        except ValueError:
            pass


class MullerPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Muller", onLoad)

        Label(self.frame, text="Valor para xa:").grid(row=0, column=1)
        self.xaEntry = Entry(self.frame, relief="raised")
        self.xaEntry.grid(row=0,column=2,columnspan=3)

        Label(self.frame, text="Valor para xb:").grid(row=1, column=1)
        self.xbEntry = Entry(self.frame, relief="raised")
        self.xbEntry.grid(row=1, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=2, column=1)
        self.tolEntry = Entry(self.frame, relief="raised")
        self.tolEntry.grid(row=2, column=2, columnspan=3)

class RegulaFalsiPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Regula Falsi", onLoad)

class NewtonPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Newton en C", onLoad)

        # z0 fn f' n_max tol