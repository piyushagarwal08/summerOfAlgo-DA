# Uses python3
import functools
import sys
@functools.lru_cache(None)
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    m= (n+2) %60
    #print((fib(n+2)-1)%10)
    answer = fib(m)%10
    if answer == 0:
        print(answer)
    else:
        print(answer-1)
    #print((fib(m)%10)-1)
