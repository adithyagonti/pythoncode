names=[]
for i in range(1,6):
    ele= input('enter the names')
    names.append(ele)
print(names)

for x in names:
    n=len(x)
    if n<5:
       print(x)