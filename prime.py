n=int(input('enter a value'))
for i in range(2,n//2):
    if n%i ==0:
        print("not a prime")
        break
else:
    print('prime')

print('bye')
