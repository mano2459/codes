# WAP to input total no of sections, section num

no_of_sec = int(input("no of sections : "))
cls = {}
for a in range(no_of_sec):
    sec_name = input("name of sections : ")
    cls[a] = sec_name

print("class\t", "sec\t", "stream")
for a in cls:

    print("12\t", a, "\t", cls[a])
