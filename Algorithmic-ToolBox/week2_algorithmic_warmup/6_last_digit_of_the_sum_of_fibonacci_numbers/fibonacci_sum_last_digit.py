# Uses python3
import sys
import random
import math
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1 or n ==2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result
#if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    #fab_no=fibonacci_sum_naive(n+2)-1
    #print(fab_no%10)
n = int(input())
fab_no = fibonacci(n+2)-1
print(fab_no%10)
