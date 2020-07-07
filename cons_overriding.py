class A:
    def __init__(self):
        print('parent class constructor')

class B(A):
    def __init__(self):
        print('child class constructor')

c= B()