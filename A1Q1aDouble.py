# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

total = np.double(0.0)
n = np.double(20)       # n for big numbers diverges, and doesn't get stuck within reasonable calculation time (passes 19.0)
bigN = np.double(pow(10, n))
#print(bigN)
k = np.double(1.0)

while k < bigN:
    total = total + np.double(np.double(1.0) / np.double(k));
    print("k = ", k, ", total =", total)
    k += 1
