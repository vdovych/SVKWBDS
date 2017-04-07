import wbpy
from pprint import pprint

api = wbpy.IndicatorAPI()

iso_country_codes = ["GB", "FR", "JP"]
total_population = "SP.POP.TOTL"

dataset = api.get_dataset(total_population, iso_country_codes, date="2010:2012")

print(dataset,dataset.as_dict(),dataset.api_url,dataset.indicator_name,dataset.countries)
