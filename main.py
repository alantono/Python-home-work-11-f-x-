from sympy import *
from sympy.plotting import plot
init_printing()
from sympy.calculus.util import minimum, maximum

x = Symbol('x')
f = 0.6 * x**3 + 5.5 * x**2 + 10 * x - 5
roots = solve(0.6 * x**3 + 5.5 * x**2 + 10 * x - 5, x)
root1 = roots[0]
root2 = roots[1]
root3 = roots[2]
print("Для функции: ", f)
print("Корни уравнения (complex): ", solve(0.6 * x**3 + 5.5 * x**2 + 10 * x - 5, x))
print("Корни уравнения (real):")
print("корень1 = ", complex(root1).real)
print("корень2 = ", complex(root2).real)
print("корень3 = ", complex(root3).real)

yprime = f.diff(x)
roots_der = list(solve(1.8*x**2 + 11.0*x + 10, x))
root_der1 = roots_der[0]
root_der2 = roots_der[1]
print("Функция возрастает на интервоале от - ∞ до ", round(root_der1, 1), "затем убывает до ", round(root_der2, 2), "затем снова возрастает до  + ∞")

interv = Interval(complex(root1).real, complex(root3).real)
res_min = minimum(f, x, interv)
res_max = maximum(f, x, interv)
print("Вершины функции на отрезке от ", round(complex(root1).real, 2), " до ", round(complex(root3).real, 2))
print("минимум - f(x) = ", res_min)
print("максимум - f(x) = ", res_max)

print("f(x) > 0 на участке от ", round(complex(root1).real, 2), " до ", round(complex(root2).real, 2), " и от ", round(complex(root3).real, 2), "до + ∞")
print("f(x) < 0 на участке от - ∞ до ", round(complex(root1).real, 2), " и от ", round(complex(root2).real, 2), " до ", round(complex(root3).real, 2))

plot(f)

