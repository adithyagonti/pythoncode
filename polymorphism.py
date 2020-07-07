class addition:
    def add(self,*values):
        total = sum(values)
        print('sum:',total)

ad = addition()
ad.add()
ad.add(4)
ad.add(4,5)
ad.add(4,5,6)
ad.add(4,5,6,7)
ad.add(4,5,6,7,8)
ad.add(4,5,6,7,8,9)