import csv
with open('emp.csv', 'w', newline='') as f:
    w=csv.writer(f)
    w.writerow(['Eno','Ename','Esal','Eaddr'])
    n=int(input('enter the num of values:'))

    for i in range(1,n+1):
        a=int(input('enter'+str(i)+'employee no:'))
        b=input('enter'+str(i)+ 'employee name:')
        c = float(input('enter' + str(i) + 'employee sal:'))
        d = input('enter' + str(i) + 'employee address:')
        w.writerow([a,b,c,d])