def add():
    a=10
    b=20
    c= a+b
    print('sum is :', c)
add()


def add1(x,y):
    z=x+y
    print('sum is :', z)
m= int(input('enter 1st value'))
n= int(input('enter 2nd value'))
add1(m,n)

def add2():
    a=10
    b=50
    c= a+b
    return c
res= add2()
print(' sum is :', res)

def add3(x,y):
    z=x+y
    return z
m= int(input('enter 1st value'))
n= int(input('enter 2nd value'))
res= add3(m,n)
print('sum is:', res)

