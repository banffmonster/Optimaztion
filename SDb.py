# using steepest descent to solve question b

from sympy import *
from sympy import Symbol, Derivative


e = 0.001
a = 0.4
b = 0.8

# objective function
x = Symbol('x')
y = Symbol('y')
f = 2*x*y + 2*x - x**2 - 2*y**2

# deriative expression
dx = diff(f, x)
dy = diff(f, y)

# starting point
x0 = -1.0
y0 = 1.0

# using backtracking to get t, a = 0.4, b = 0.8
def get_t(x0, y0):
    dx0 = dx.subs({x: x0, y: y0})
    dy0 = dy.subs({x: x0, y: y0})
    t = Symbol('t')
    ft = f.subs({x: x0 + dx0 * t, y: y0 + t * dy0})
    s = 1 # start with t = 1
    # stop condition
    while (ft.subs({t:s}) < (ft.subs({t:0}) + a*(diff(ft, t).subs({t:0}))*s)):
        s = b*s
        print("t = ", s)
    return s

if __name__ == '__main__':
    i = 0

    # stop condition
    while ((abs(dx.subs({x:x0, y:y0})) > e) and (abs(dy.subs({y:y0, x:x0}))> e)):
        st = get_t(x0, y0)
        Y = f.subs({x: x0, y:y0})
        Dx = dx.subs({x: x0, y: y0})
        Dy = dy.subs({x: x0, y: y0})
        print("[x%d, y%d] = [%f, %f]"%(i, i, x0, y0), "f(x%d, y%d) = %f"%(i, i, Y), "d(x%d, y%d) = [%f, %f]"%(i, i, Dx, Dy), "t_%d = %f"%(i, st))

        # update x0, y0 using steepest descent
        x0 = x0 + st * Dx
        y0 = y0 + st * Dy
        i = i+1
        print("\n\n")
    print("after %d iterations, the maximum is %f"%(i, Y))
