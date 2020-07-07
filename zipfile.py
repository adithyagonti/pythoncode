from zipfile import *

f= ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('adhi.txt')
f.write('xyz.txt')
f.write('hai.txt')
f.close()


