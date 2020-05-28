# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

total= np.float32(0.0)
n= np.float32(20)    # they just get stuck at 0.49999997
bigN= np.float32(pow(10, n))
#print(bigN)
#print(pow(3,bigN))
k = np.float32(1.0)

while k < bigN:
    total = total + np.float32(np.float32(1.0) / np.float32(pow(3, np.float32(k))));
    print("k = ", k, ", total =", total)
    k += 1
