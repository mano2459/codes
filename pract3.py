# wap to insert list data in csv file and print it

import csv

lst = ["hello","world",1,2]

with open("data.csv","w") as f:
    w = csv.writer(f)
    w.writerow(lst)

with open("data.csv","r") as f:
    r = csv.reader(f)
    for a in r:
        print(a)
