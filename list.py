
def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd


lst= []

n = int(input('enter the no of elements'))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print(lst)

even, odd = count(lst)

print("even: {} and odd: {}".format(even,odd))