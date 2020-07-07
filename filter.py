data = [34,45,56,67]

def even(n):
    if n%2==0:
        return True

res = list(filter(even,data))
print(res)

res= list(filter(lambda n: n%2==0, data))
print(res)
