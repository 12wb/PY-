from sympy import *
x = Symbol("x")
expr = 2*x**2+x**3
print(diff(expr,x))