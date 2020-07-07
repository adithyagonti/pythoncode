n=int(input('enter a value'))
factors=0
for i in range(1,n+1):
    if n%i==0:
        factors+=1
if factors==2:
    print("prime")
else:
     print("not a prime")


