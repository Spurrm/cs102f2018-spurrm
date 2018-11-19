from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

f, g = symbols('f g', cls=Function)
print f(x)

# prints out derivative
print f(x).diff(x)

# prints out second derivative
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
print diffeq

# solved equation
print dsolve(diffeq, f(x))

# prints out the derivative of a given function
print dsolve(f(x).diff(x)*(1 - sin(f(x))), f(x))
