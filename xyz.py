from numpy import *

arr1 = array([87,65,43,22])
arr2 = array([12,34,56,78])
result = []

for i in range(0,len(arr1)):
    result.append(arr1[i]+arr2[i])

print('sum of arr1 and arr2 is:', result)
