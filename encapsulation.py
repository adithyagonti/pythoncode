class costomer:
    def __init__(self):
        self.cid=15

    def store(self):
        self.cname="adhi"

c=costomer()
print(c.__dict__)
c.bal=234556.95
print(c.__dict__)