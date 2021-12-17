# program 2
with open("practical/data.txt") as f:

    data = f.read()

    lst = data.split()

    for a in lst:
        vov = 0
        con = 0
        for b in a:
            if b in "aeiouAEIOU":
                vov += 1
            else:
                con += 1
        print("word : ", a, ", vovels : ", vov, ",cons : ", con)
        pass
