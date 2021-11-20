# 11WAP A PROGRAM TO INPUT THE NAME OF N COUNTRIES AND
#  THEIR CAPITAL,CURRENCY AND DISPLAY IN A TABULAR FORM.
d = {}
e = int(input("Enter the number of counrties:"))
i = 1
while i <= e:
    co = input("enter the country name:")
    cap = input("Enter the capital name :")
    curre = input("enter the currency name:")
    d[co] = [cap, curre]
    i += 1
l = d.keys()
print("\ncountry\t\t", "capital\t", "currency")
for i in d:
    
    print(i, "\t\t", d[i][0],"\t\t", d[i][1])
