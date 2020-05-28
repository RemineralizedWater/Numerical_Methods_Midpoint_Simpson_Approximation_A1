# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

total= np.double(0.0)
n = 4     # n>=3 crashes, says: OverflowError: int too large to convert to float, but always stuck at 0.49999997
bigN = pow(10,n)
#print(bigN)
#print(pow(3, pow(10, 3)))
k = 1

while k < bigN:
    try:
        total = np.double(total + np.double(1.0 / np.double(pow(3, k))))
        print("k = ", k, ", total =", total)
        k += 1
    except OverflowError:
        exit(0)
