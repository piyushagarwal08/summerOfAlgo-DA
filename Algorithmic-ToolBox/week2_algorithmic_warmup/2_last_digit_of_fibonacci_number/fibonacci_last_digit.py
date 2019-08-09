# Uses python3
import sys
#import random
#def get_fibonacci_last_digit_naive(n):
 #   if n <= 1:
  #      return n

  #  previous = 0
   # current  = 1

    #for _ in range(n - 1):
     #   previous, current = current, previous + current

   # return current % 10

def last_digit(n):
    if n<=1:
        return n
    initial = 0
    final = 1
    for i in range(n):
        result = initial + final
        final,initial = initial,result%10
    return result%10

#def get_fibonacci_last_digit_naive(n):
 #   if n<=1:
  #      return n
   # initial = 0
   # final = 1
   # for i in range(n):
    #    result = initial + final
     #   final,initial = initial,result
   # return result%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(last_digit(n))
#while True:
 #   n = random.randint(0,15)
  #  test = get_fibonacci_last_digit_naive(n)
   # check = last_digit(n)
    #if test != check:
     #   print(f'for {n}')
      #  print(f'test has value {test}')
       # print(f'check has value {check}')
       # break
  #  else:
   #     print(f'OK,{test},{check}')
