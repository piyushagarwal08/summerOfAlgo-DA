# Uses python3
import sys

def get_fibonacci_huge_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current 


def get_fibonacci_huge_naive_v2(n,m):
    seq_len = []
    check = []
    for i in range((m*m)+1):
        value=get_fibonacci_huge_naive(i)
        seq_len.append(value%m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
