# Newton's technigue to solve question b

from sympy import *
import numpy as np


e = 0.001
# start point
[x0, y0] = [-1.0, 1.0]

# create symbol for x, y
x = Symbol("x")
y = Symbol("y")

# objective function
f = 2*x*y + 2*x - x**2 - 2*y**2

# calculate first derivative and second derivative expression
dx = diff(f, x)
dy = diff(f ,y)
dxx = diff(dx, x)
dxy = diff(dx, y)
dyx = diff(dy, x)
dyy = diff(dy, y)


if __name__ == '__main__':
    i = 0
    # begin iteration
    while True:

        print("[x%d, y%d] = [%f, %f]" % (i, i, x0, y0))
        Y = f.subs({x: x0, y: y0})
        print("f(x%d, y%d) = %f" % (i, i, Y))

        # calculate derivatives
        dx0 = float(dx.subs({x:x0, y:y0}))
        dy0 = float(dy.subs({x:x0, y:y0}))
        dxx0 = float(dxx.subs({x:x0, y:y0}))
        dxy0 = float(dxy.subs({x:x0, y:y0}))
        dyx0 = float(dyx.subs({x:x0, y:y0}))
        dyy0 = float(dyy.subs({x:x0, y:y0}))

        # create matrix
        xy0 = np.array([x0, y0])
        f1 = np.array([dx0, dy0])
        print("[dx%d, dy%d] = "%(i,i), f1)
        f2 = np.array([[dxx0, dxy0], [dyx0, dyy0]])
        print("[dxx, dxy, dyx, dyy] = ",'\n',f2)

        # update x, y vector using Newton's method
        xy0 = xy0 - np.matmul((np.linalg.inv(f2)), np.transpose(f1))
        print("\n\n")

        # stop condition
        if (abs(dx.subs({x:x0, y:y0}))< e and abs(dy.subs({x:x0, y:y0}))< e):
            break

        x0 = xy0[0]
        y0 = xy0[1]
        i = i + 1
    #f2 = np.array([[-2, 2], [2, -4]])
    # print(type(dxx0))
    # print(f1)
    # print(f2)
    #
    # test = np.array([[1,0],[0, 1]]);
    # print(np.linalg.inv(test));
    # print(np.linalg.inv(f2));
    print("after %d iterations, the maximum is %f at [%f, %f]"%(i, Y, x0, y0))
    exit()


