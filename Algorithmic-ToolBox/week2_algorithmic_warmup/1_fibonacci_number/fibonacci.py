# Uses python3
#import random
#def calc_fib(n):
 #   if (n <= 1):
  #      return n

   # return calc_fib(n - 1) + calc_fib(n - 2)
def calc_fib(n):
    if (n<=1):
        return n
    initial = 0
    final = 1
    for i in range(n):

        result = initial + final
        final = initial
        initial = result
    return result

#while True:
 #   n = random.randint(0,30)
  #  test=calc_fib(n)
   # check = calc_fib_v2(n)

   # if test != check:
    #    print(f'for {n}')
     #   print(f'value of testcase is {test}')
      #  print(f'value of checkcase is {check}')
   # else:
    #    print('OK',check,test)
n = int(input())
print(calc_fib(n)%239)
