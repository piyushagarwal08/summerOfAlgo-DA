# Uses python3
import sys

def get_change(m):
    #write your code here
    c = 0
    while m != 0:
        if m >= 10:
            c += 1
            m -=10
        elif m<10 and m>=5:
            c += 1
            m -= 5
        else:
            c += 1
            m -= 1
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

#n = int(input())
#print(get_change(n))
