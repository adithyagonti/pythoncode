from array import *

arr = array('i', [])
n= int(input('enter the length of array'))

for e in range(n):
    x= int(input('enter the values'))
    arr.append(x)

print(arr)
val= int(input('enter the value of search'))

a=0
for e in arr:
    if e==val:
        print(a)
        break
    a+=1

print(arr.index(val))
