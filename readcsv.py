import csv
with open('adhi.csv','r')as f:
    r=csv.reader(f)
    data = list(r)
    print(data)
    for line in data:
        for word in line:
            print(word, end=' ')
        print()

