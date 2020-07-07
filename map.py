
data =[2,3,4]
res=[]
def double(n):
    return n*2
for i in data:
    ele=double(i)
    res.append(ele)
print(data)
print('with out map',res)

res=list(map(double,data))
print('with map function ',res)

res = list(map(lambda n:n*2,data))
print(res)

from functools import *

res = reduce((lambda a,b : a*b), data)
print(res)