import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    country_brand_dict = {}
    country_asian_dict = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            origin = row['Origin']
            brand = row['Brand']
            type = row['Type']

            brands = country_brand_dict.get(origin, [])
            brands.append(brand)
            country_brand_dict[origin] = brands
            country_asian_dict[origin] = True if type == 'asian' else False

    for key in country_brand_dict:
        dict = {
            'countryName': key,
            'asian': country_asian_dict[key],
            'numberOfBrands': len(country_brand_dict[key]),
            'brands': country_brand_dict[key]
        }
        jsonArray.append(dict)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=2)
        jsonf.write(jsonString)


csvFilePath = r'brands.csv'
jsonFilePath = r'brands.json'
csv_to_json(csvFilePath, jsonFilePath)
