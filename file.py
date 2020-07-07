from os.path import isfile
filename = input('enter the file name')
if isfile(filename):
    f=open(filename)

else:
    print('file does not exist')

lc=wc=cc=0
for line in f:
    lc=lc+1
    cc= cc+len(line)
    words=line.split()
    wc=wc+len(words)
print(lc)
print(wc)
print(cc)