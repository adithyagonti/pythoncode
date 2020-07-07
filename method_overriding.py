class A:
    def msg(self):
        print('good morning')

class B(A):
    def msg(self):
        print('good nyt')

c= B()
c.msg()
