# Newton's technigue to solve question a

from sympy import *

e = 0.001

# start point
x0 = 2.5

# objective function
x = Symbol("x")
f = 2*sin(x) - x**2/10

# derivative expression
df1 = diff(f)
df2 = diff(df1)

if __name__ == '__main__':
    i = 0
    while(True):
        #print(abs(df1.subs({x: x0})))
        y = f.subs({x:x0})
        print("x%d = %f, f(x%d) = %f"%(i, x0, i, y))

        # stop condition
        if(abs(df1.subs({x: x0})) < e):
            break

        # update x using Newton's method
        x0 = x0 - df1.subs({x: x0}) / df2.subs({x: x0})
        i = i+1
        print("\n\n")

    print("after %d iterations, the maximum is %f"%(i, y))
    exit()