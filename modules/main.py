from datstruct import DataChain

with open("Saved_data.txt","rb") as f:
    Dat = DataChain()
    Dat.load(f.read())


formatedDat = list()
for item in Dat.search('2012'):
    if item._data[1]["2012"]:
        formatedDat.append(item._data[1]["2012"])
formatedDat.sort()
for it in formatedDat:
    if(it>1000000000 and it.is_integer()):
        print(it)
print("12123412314212432314")
formatedDat1 = list()
for item in Dat.search('2002'):
    if item._data[1]["2002"]:
        formatedDat1.append(item._data[1]["2002"])
formatedDat1.sort()
for it in formatedDat1:
    if(it>1000000000 and it.is_integer()):
        print(it)