# Uses python3
import sys
import math
#def gcd_naive(a, b):
    #current_gcd = 1
   # for d in range(2, min(a, b) + 1):
       # if a % d == 0 and b % d == 0:
        #    if d > current_gcd:
         #       current_gcd = d

   # return current_gcd
def gcd_math(a,b):
    return math.gcd(a,b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_math(a, b))
#a,b = 50,254
#print(gcd_math(a,b))
#print(gcd_naive(a,b))
