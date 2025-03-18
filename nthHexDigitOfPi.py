## Return the Nth Hexadecimal Digit of Pi
## The 100th hex digit of pi is "C"

import math

def hexDigit(N):
    s = 0
    for n in range(N):
        s += 4 * pow(16, N-n-1, 8*n + 1) / (8*n + 1)
        s -= 2 * pow(16, N-n-1, 8*n + 4) / (8*n + 4)
        s -= pow(16, N-n-1, 8*n + 5) / (8*n + 5)
        s -= pow(16, N-n-1, 8*n + 6) / (8*n + 6)
    frac = s - math.floor(s)
    return math.floor(16*frac)

if __name__ == '__main__':
    print("Enter Nth Digit of Pi:")
    n = int(input())
    nthHex = hexDigit(n)
    print(nthHex)
