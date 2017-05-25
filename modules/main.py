from datstruct import DataChain
import random

with open("Saved_data.txt", "rb") as f:
    Dat = DataChain()
    Dat.load(f.read())

year, year1 = str(random.randrange(2001, 2016)), str(random.randrange(2001, 2016))

formatedDat = list()
for item in Dat.search(year):
    if item._data[1][year]:
        formatedDat.append(item._data[1][year])

formatedDat1 = list()
for item in Dat.search(year1):
    if item._data[1][year1]:
        formatedDat1.append(item._data[1][year1])

print("Differense between years {} and {} is ".format(year,year1),abs(sum(formatedDat) - sum(formatedDat1)))

