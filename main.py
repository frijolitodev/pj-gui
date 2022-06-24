# from window.MainWindow import *

# mainTask = MainWindow()
# mainTask.start()

from calcs.MullerMethod import MullerMethod

m = MullerMethod((lambda x: x * x ** 0.5 + 10 * x - 20), 4.5, 5.5, 5, 0.0001)

for item in m.to_info():
    print(item)
