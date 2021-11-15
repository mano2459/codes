import csv

with open ("pr14.csv") as f:
    w = csv.reader(f)
    for a in w:
        print(a)
    pass

w = csv.reader(f)
