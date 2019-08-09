# Uses python3
import sys

def fibo(n,cache={0:0,1:1,2:1}):
    if n not in cache:
        cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]


def period(m,cache={}):
    if m not in cache:
        seq = []
        i = 0
        l = 0
        while True:
            seq.append(fibo(i)%m)
            l += 1
            i += 1
            if l%2 == 0:
                pre,post = seq[:l//2],seq[l//2:]
                if pre == post:
                    cache[m] = pre
                    return len(cache[m])
    return len(cache[m])


if __name__ == '__main__':
    input = sys.stdin.read();
    n,m = map(int,input.split())
    seq_len = period(m)
    low_n = n % seq_len
    print(fibo(low_n)%m)
#n,m = list(map(int,input().split()))
#period_len = period(m)
#print(period_len)
#low_n = n%period_len
#print(fibo(low_n)%m)

