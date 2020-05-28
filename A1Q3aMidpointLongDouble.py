# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

bigM = 2
h = np.longdouble(1.0 / bigM)
p = 2       # Keeps error proportion up to M=67108864 (and likely past)
hp = pow(h, p)
prevHp = hp
prevError = 0
hpRatio = hp / prevHp
k = 0
x = np.longdouble(k * h)
xh2 = np.longdouble(x + h / 2.0)
intFxDx = np.longdouble(0.0)
fx = np.longdouble(np.sin(np.longdouble(np.pi) * xh2))
exactIntFx = np.longdouble(2.0 / np.pi)
delta = 0.0000001
firstDelta = 0
n = 1

while bigM < 128000000000000:
    while k < bigM:
        x = np.longdouble(k * h)
        xh2 = np.longdouble(x + h / 2.0)
        fx = np.longdouble(np.sin(np.longdouble(np.pi) * xh2))
        intFxDx += fx
        k += 1
    intFxDx *= h
    error = np.longdouble(np.abs(exactIntFx - intFxDx))
    #error = np.longdouble(np.abs(exactIntFx - intFxDx)/exactIntFx)
    if ((error - delta) < 0) and (firstDelta == 0):
        print("Using the Midpoint Rule: For M = " , bigM , ", intFxDx = " , intFxDx, ", error is ", error)
        print("This is the smallest value of M for which error is less than 10^(-7). ", n, " function evaluations are required.")
        print("For p =", p, "the previous to current error proportion is: ", hpRatio)
        firstDelta += 1
    else:
        print("Using the Midpoint Rule: For M = " , bigM , ", intFxDx = ", intFxDx, ", error is ", error)
        print("For p =", p, "the previous to current error proportion is: ", hpRatio)
    bigM *= 2
    h = np.longdouble(1.0 / bigM)
    hp = pow(h, p)
    hpRatio = hp / prevHp * prevError / error
    prevError = error
    prevHp = hp
    n += 1
    k = 0
    intFxDx = np.longdouble(0.0)
