data=[1,2,3,4,5]
res = list(map(lambda n:n*2,data))
print(res)

from functools import *

num = reduce((lambda a,b : a+b), res)
print(num)