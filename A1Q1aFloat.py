# Written by Michael Rowe 26101267
# COMP 361 A1

import numpy as np

total = np.float32(0.0)
n = np.float32(20)       # n for big numbers has total stuck at 15.403683
bigN = np.float32(pow(10, n))
#print(bigN)
k = np.float32(1.0)

while k < bigN:
    total = total + np.float32(np.float32(1.0) / np.float32(k));
    print("k = ", k, ", total =", total)
    k += 1
    #if total == 15.403683:
        #exit(0)
