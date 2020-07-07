class product:
    def __init__(self,price):
        self.price=price
    def __add__(self,second):
        return self.price+second.price

p1=product(45)
p2=product(20)
print('bill is', p1+p2)

class product:
    def __init__(self,price):
        self.price=price
    def __lt__(self,second):
        if self.price<second.price:
            return 'p1 is less than p2'
        else:
            return 'p2 is less than p1'

p1=product(60)
p2=product(70)
print(p1<p2)

class customer:
    def __init__(self,qty):
        self.qty=qty
    def __mul__(self,other):
        return self.qty*other.price

class product:
    def __init__(self,price):
        self.price=price


c=customer(15)
p=product(50)
print('bill is:', c*p)