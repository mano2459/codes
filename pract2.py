import pickle
with open("practical/compu.dat","wb") as f:
    stri = "hello yahan aapani marzi se koch bhi likh lo"
    pickle.dump(stri,f)
    pass


with open("practical/compu.dat", 'rb') as f:
    data = pickle.load(f)
    print(data)
    dicti = {}
    for a in data:
        try:
            dicti[a] +=1
        except:
            dicti[a]=1
    print(dicti)


    
    pass
