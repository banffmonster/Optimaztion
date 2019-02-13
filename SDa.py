# steepest descent for question a


from sympy import *
import numpy
a = 0.4
b = 0.8
e = 0.001

# starting point
x0 = 2.5
x = Symbol("x")

# objective function
f = 2*sin(x) - x**2/10
print("f(x) = ", f)

df = diff(f)
print("df = ", df)

# using backtracking to get step length t
def get_t(x0):
    t = Symbol("t")
    x1 = x0 + t * df.subs({x: x0})
    ft = f.subs({x: x1})
    s = 1

    while (ft.subs({t: s}) < (ft.subs({t: 0}) + a * (diff(ft, t).subs({t: 0})) * s)):
        s = b * s
        print("s = ", s)
        print("ft(s) = ", ft.subs({t: s}))
        print(ft.subs({t: 0}) + a * (diff(ft, t).subs({t: 0})) * s)
    return s


if __name__ == '__main__':

    i = 0
    # stop condition
    while (abs(df.subs({x:x0})) > e):
        st = get_t(x0)
        y = f.subs({x: x0})
        d = df.subs({x: x0})
        print("x%d = %f"%(i, x0), "f(x%d) = %f"%(i, y), "df(x%d) = %f"%(i, d), "t_%d = %f"%(i, st))

        # update x using steepest descent
        x0 = x0 + st * df.subs({x: x0})
        i = i+1
        print("\n\n")

    print("after %d iterations, the maximum is %f"%(i, y))
    exit()






