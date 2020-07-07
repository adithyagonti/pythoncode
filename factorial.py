num=int(input('enter the value'))
if num<0:
    print('no factorial for _ve numbers')
elif num==0:
    print('the factorial of 0 is 1')
else:
    fact=1
    for i in range(1,num+1):
        fact= fact*i
    print("the factorial of", num,"is",fact)

