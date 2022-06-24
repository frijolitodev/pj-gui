from calcs.NewtonMethod import NewtonMethod

newton = NewtonMethod("x ** (1./3.) + x ** 7", 2 + 2j, 100, 10 ** -9)

print(newton.to_info())