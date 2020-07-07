from array import *
nums = array('i', [])
n = int(input('enter the length of the array'))

for e in range(n):
    x= int(input('enter the values'))
    nums.append(x)
print(nums)

index = int(input('enter the number which u search'))
k=0
for g in nums:
    if g==index:
        print(k)
        break

    k+=1
