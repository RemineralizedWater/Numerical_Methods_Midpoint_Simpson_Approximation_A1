# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

bigM = 2
h = np.longdouble(1.0 / bigM)
p = 4       # Up to M=16384, p=4 works as error proportion, from M=65536 onwards, p=0 works as error proportion, likely due to rounding errors
hp = pow(h, p)
prevHp = hp
prevError = 1
hpRatio = hp / prevHp
k = 0
x = np.longdouble(k * h)
intFxDx = np.longdouble(0.0)
fx = np.longdouble(np.sin(np.longdouble(np.pi) * x))
exactIntFx = np.longdouble(2.0 / np.pi)
delta = 0.0000001
firstDelta = 0
n = 1

if bigM % 2 == 0:
    while bigM < 128000000000000000000:
        while k <= bigM:
            x = np.longdouble(k * h)
            fx = np.longdouble(np.sin(np.longdouble(np.pi) * x))
            if (k == 0) or (k == bigM):
                intFxDx += fx
            elif k % 2 == 1:
                intFxDx += 4 * fx
            else:
                intFxDx += 2 * fx
            k += 1
        intFxDx *= h / 3.0
        error = np.longdouble(np.abs(exactIntFx - intFxDx))
        #error = np.longdouble(np.abs(exactIntFx - intFxDx)/exactIntFx)
        if ((error - delta) < 0) and (firstDelta == 0):
            print("Using the Simpson's Rule: For M =", bigM, ", intFxDx =", intFxDx, ", error is", error)
            print("This is the smallest value of M for which error is less than 10^(-7).", n,
                  " function evaluations are required.")
            print("For p =", p, "the previous to current error proportion is:", hpRatio)
            firstDelta += 1
        else:
            print("Using the Simpson's Rule: For M =", bigM, ", intFxDx =", intFxDx, ", error is", error)
            print("For p =", p, "the previous to current error proportion is:", hpRatio)
        bigM *= 2
        h = np.longdouble(1.0 / bigM)
        hp = pow(h, p)
        if error == 0:
            error = 1e-51
        hpRatio = hp / prevHp * prevError / error
        prevError = error
        prevHp = hp
        n += 1
        k = 0
        intFxDx = np.longdouble(0.0)
else:
    print("Error, M must be even")
