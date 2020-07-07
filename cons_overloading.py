class student:
    def __init__(self,rno=12,name='xyz',address='hyd'):
        self.rno=rno
        self.name=name
        self.address=address
    def display(self):
        print(self.rno)
        print(self.name)
        print(self.address)

s1=student()
s1.display()
s2=student(333)
s2.display()
s3=student(7069,'sagar')
s3.display()
s4=student(5555,'mahi','banglore')
s4.display()
