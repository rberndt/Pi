## Improved - Return the Nth Hexadecimal Digit of Pi
## Improved by adding an estimate of the infinite series originally ignored
## The 100th hex digit of pi is "C"

import math
import numpy as np

epsilon = np.finfo(float).eps

def term(N, n):
    return 16**(N-1-n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))

def hexDigit(N):
    s = 0
    for n in range(N):
        s += 4 * pow(16, N-n-1, 8*n + 1) / (8*n + 1)
        s -= 2 * pow(16, N-n-1, 8*n + 4) / (8*n + 4)
        s -= pow(16, N-n-1, 8*n + 5) / (8*n + 5)
        s -= pow(16, N-n-1, 8*n + 6) / (8*n + 6)
        s = s%1

    n = N+1
    while True:
        t = term(N,n)
        s += t
        n += 1
        if abs(t) < epsilon:
            break

    frac = s - math.floor(s)
    return math.floor(16*frac)

if __name__ == '__main__':
    print("Enter Nth Digit of Pi:")
    n = int(input())
    nthHex = hexDigit(n)
    print(nthHex)
