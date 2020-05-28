# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np
import random

k = 0
x = np.longdouble(random.uniform(0, 1))
#x = np.longdouble(1e-161)
#x = np.longdouble(0.99999999999999994)
#x = np.longdouble(0.5)
x1 = x2 = x3 = x4 = x5 = x
c1 = np.longdouble(0.95)
c2 = np.longdouble(1.55)
c3 = np.longdouble(2.0)
c4 = np.longdouble(3.6)
c5 = np.longdouble(3.98)
bigN = 8000
fx1 = np.longdouble(c1 * np.longdouble(x) * np.longdouble(1 - x))
fx2 = np.longdouble(c2 * np.longdouble(x) * np.longdouble(1 - x))
fx3 = np.longdouble(c3 * np.longdouble(x) * np.longdouble(1 - x))
fx4 = np.longdouble(c4 * np.longdouble(x) * np.longdouble(1 - x))
fx5 = np.longdouble(c5 * np.longdouble(x) * np.longdouble(1 - x))

print("x^(0) =", x, "(Random longdouble between 0 and 1)")

while k < bigN:
    fx1 = np.longdouble(c1 * np.longdouble(x1) * np.longdouble(1 - x1))     # appears to converge to 0 at x=inf, doesn't get stuck. NOT AFFECTED BY X0.
    fx2 = np.longdouble(c2 * np.longdouble(x2) * np.longdouble(1 - x2))     # appears to converge to 0.35483870967741937326 or 0.35483870967741937334, or gets stuck there. Therefore this IS AFFECTED by X0, BUT PERHAPS ONLY DUE TO SIZE LIMITATIONS.
    fx3 = np.longdouble(c3 * np.longdouble(x3) * np.longdouble(1 - x3))     # appears to converge to 0.5. NOT AFFECTED BY X0.
    fx4 = np.longdouble(c4 * np.longdouble(x4) * np.longdouble(1 - x4))     # appears to diverge (oscillates between 0 and 1). NOT AFFECTED BY X0.
    fx5 = np.longdouble(c5 * np.longdouble(x5) * np.longdouble(1 - x5))     # appears to diverge (oscillates between 0 and 1). NOT AFFECTED BY X0.
    print("k = ", k, "f(x1) =", fx1, ", f(x2) =", fx2, ", f(x3) =", fx3, ", f(x4) =", fx4, ", f(x5) =", fx5)
    x1 = fx1
    x2 = fx2
    x3 = fx3
    x4 = fx4
    x5 = fx5
    k += 1
