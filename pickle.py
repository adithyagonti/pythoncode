import pickle
class customer:
    def __init__(self,cid,cname,caddr):
        self.cid=cid
        self.cname=cname
        self.caddr=caddr
    def display(self):
        print('cid:', self.cid)
        print('cname:', self.cname)
        print('caddr:',self.caddr)

with open('data.txt', 'wb') as f:
    c= customer('123', 'praveen','hyd')
    pickle.dump(c,f)

with open('data.txt', 'rb') as f:
    obj= pickle.load(f)
    obj.display()