class Developer:
    def work(self):
        print('developing')

class tester:
    def work(self):
        print('testing')

class teacher:
    def teach(self):
        print('teaching')

class student:
    def learn(self):
        print('learning')

jobs=[Developer(), teacher(), tester(),student()]
for object in jobs:
    if hasattr(object, 'teach'):
        object.teach()
    if hasattr(object,'learn'):
        object.learn()
    if hasattr(object,'work'):
        object.work()