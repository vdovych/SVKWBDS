import wbpy
from dattype import Data
from datstruct import DataChain
api = wbpy.IndicatorAPI()

iso_country_codes = ["GB", "FR", "JP"]
total_population = "SP.POP.TOTL"

dataset = api.get_dataset(total_population,date="2000:2017")
Dat = DataChain()
dataset = dataset.as_dict()
for elem in dataset:
    Dat.add(Data((elem, dataset[elem])))

with open("Saved_data.txt","wb") as f:
    f.write(Dat.serialize())