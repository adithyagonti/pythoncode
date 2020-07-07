
def fib(n):

    n1 = 0
    n2 = 1
    count =0

    if n<0:
        print('enter a positive number')
    elif n==1:
        print(n1)
    else:
        if count<n:
          print(n1)
          print(n2)

          for i in range(2,n):
                c = n1 + n2
                n1 = n2
                n2 = c
                print(c)

fib(8)