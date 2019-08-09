# Uses python3
import sys
import math
#import random
#def lcm_naive(a, b):
 #   for l in range(1, a*b + 1):
  #      if l % a == 0 and l % b == 0:
   #         return l

   # return a*b
def lcm_naive_v2(a,b):
    factor = a/math.gcd(a,b)
    return int(b*factor)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive_v2(a, b))
#while True:
 #   a,b = random.randint(1,30),random.randint(1,30)
  #  test = lcm_naive(a,b)
   # check = lcm_naive_v2(a,b)
   # if test != check:
    #    print(f'for value of {a} and {b}')
     #   print(f'test is {test}')
      #  print(f'check is {check}')
       # break
   # else:
    #    print(f'OK {test} and {check}')
