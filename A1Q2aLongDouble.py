# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np
import random

k = 0
#x = 1e-51
x = np.longdouble(random.uniform(0, 1))
bigN = 1835
fx = np.longdouble(2 * np.longdouble(pow(x, 3)) + 5) / np.longdouble(3 * pow(x, 2))

print("x^(0) =", x, "(Random longdouble between 0 and 1)")

while k < bigN:
    fx = np.longdouble(2 * np.longdouble(pow(x, 3)) + 5) / np.longdouble(3 * pow(x, 2))
    print("k =", k, ", f(x) =", fx)           # appears to converge at 1.7099759466766969894 / 1.7099759466766969895
    x = fx
    k += 1
