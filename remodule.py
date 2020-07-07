import re
mailid = input('enter your mail id')
matcher= re.fullmatch('\w[a-zA-Z0-9._]*@[a-zA-Z0-9]*.[a-zA-Z0-9]{2,5}',mailid )
if matcher !=None:
    print(' valid')
else:
    print('in valid')