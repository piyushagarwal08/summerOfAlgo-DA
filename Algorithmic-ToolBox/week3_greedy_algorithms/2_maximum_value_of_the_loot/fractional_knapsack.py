# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    fractions = []
    for i in range(len(values)):
        fractions.append(values[i]/weights[i])
   # print(fractions,'this is fractions list')
    while capacity != 0:
        #print('values are: ',values)
       # print('weights are: ',weights)
       # print('current capacity:',capacity)
        max_value = max(fractions)
       # print('max value is:',max_value)
        index_pos = fractions.index(max_value)
       # print('with index pos:',index_pos)
        if weights[index_pos] <= capacity:
            value += values[index_pos] 
            capacity -= weights[index_pos]
            fractions.pop(index_pos)
            weights.pop(index_pos)
            values.pop(index_pos)
         #   print('so value increases to:',value)
        #    print('capacity left to be full:',capacity)
        else:
            value += capacity*max_value
            capacity = 0
          #  print('value increases to:',value)
          #  print('capacity left in bag:',capacity)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
 #   data = list(map(int,input().split()))
    n, capacity = data[0:2]
   # for i in range(n):
    #    data += list(map(int,sys.stdin.read().split()))
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    if n ==1:
        if weights[0] >= capacity:
            opt_value = capacity * ( values[0]/weights[0])
        else:
            opt_value = values[0]
    else:
        opt_value = get_optimal_value(capacity, weights, values)
   # print(capacity)  # length should be 1
   # print(weights)  # length should be 3
   # print(values)   # length should be 3
    print("{:.10f}".format(opt_value))
