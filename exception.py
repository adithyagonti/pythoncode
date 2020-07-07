print("line 1")
try:
    a=int(input('enter the first value'))
    b= int(input('enter the second value'))
    print(a/b)
except ZeroDivisionError:
    print("zerodivisionerror has occurred")
except TypeError:
    print('type error has occurred')
except:
    print('some exception has occurred')

else:
    print('else suite')
 
finally:
    print('finally suite')
print("line 3")
print("line 4")
