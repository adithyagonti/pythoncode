class computer:
    def __init__(self):
        self.name='adhi'
        self.age=20
    def compare(self,other):
        if self.name==other.name:
            print('they are same')
        else:
            print('they are diff')

c1=computer()
c1.name='abhi'
c2=computer()

c1.compare(c2)

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
