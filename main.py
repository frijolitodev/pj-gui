from window.MainWindow import *

mainTask = MainWindow()
mainTask.start()

# import ast
# from numpy import *
# from sympy import *

# # x = symbols('x')
# # f = "x ** 2"

# # fl = lambdify(x, f)

# # f = (x) ** 2

# # print(f.diff(x))

# # t = Derivative(fl, x)

# l = lambda x : eval("x ** 2", { "x": x })

# x = symbols('x')
# f = lambdify(x,l , ["numpy"])

# print(f(x).diff(x))
# print(f(2))