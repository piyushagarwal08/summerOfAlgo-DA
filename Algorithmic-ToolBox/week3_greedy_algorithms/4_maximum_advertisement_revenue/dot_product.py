#Uses python3

import sys

#def max_dot_product_(a, b):
 #   #write your code here
  #  res = 0
   # for i in range(len(a)):
    #    res += a[i] * b[i]
   # return res

def max_dot_product(a,b):
    res = 0
    while len(a) != 0:
        max_a = max(a)
        max_b = max(b)
        res += max(a) * max(b)
        a.remove(max_a)
        b.remove(max_b)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
