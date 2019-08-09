init = 0
final = 1
for i in range(28):
    if i == 0:
        print(0)
        continue
    result = init + final
    init,final=result,init
    print(result,end="   ")
    print('result % 2:',result%2,end="   ")
    print('result % 3:',result%3,end='    ')
    print('result % 4:',result%4,end="    ")
    print('result % 5:',result%5,end='    ')
    print('result % 6:',result%6)
    


