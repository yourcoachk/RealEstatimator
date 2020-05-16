# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:21:37 2020

@author: Kolby Kuratnick
"""

zipcode = 19701                             #This is just a test example
prop_type_str = 'Single Family Home'
year_built = 1997
#prop_value = 133*2000
prop_sqft = 1775
lot_sqft = 7840
bedrooms = 3
full_bathrooms = 2
half_bathrooms = 1
kitchen_sqft = 500
basement = 'yes'
roof_type_str = 'Asphault Shingles'
washer = 'yes'
dryer = 'yes'
dishwasher = 'yes'
fridge = 'yes'
microwave = 'yes'
stove = 'yes'
#kitchen_match = 'yes'
#washer_dryer_match = 'yes'
pool = 'none'
hot_tub = 'no'
driveway = 'yes'
garage = 'yes'
#garage_install = 
AC_type_str = 'Central Air'
heat_type_str = 'Heat Pump'
fireplaces = 1
electric_system = 'circuit breaker'
water_type = 'town'
foundation_material_str = 'Poured Concrete'
porch = 'yes'
patio = 'yes'
yard = 'yes'
totalValue = 329900



import json
import numpy as np



def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list



data = {}
data['Results'] = []
data['Results'].append({
    "zipcode" : zipcode,
    "prop_type": prop_type_str,
    "year_built": year_built,
#   "property value": prop_value,
    "prop_sqft": prop_sqft,
    "lot sqft": lot_sqft,
    "bedrooms": bedrooms,
    "full_bathrooms": full_bathrooms,
    "half_bathrooms": half_bathrooms,
    "kitchen sqft": kitchen_sqft,
    "basement": basement,
    "roof_type": roof_type_str,
    "washer" : washer,
    "dryer" : dryer,
    "dishwasher" : dishwasher,
    "fridge": fridge,
    "microwave":microwave,
    "stove":stove,
#   "kicthen match": kitchen_match,
#   "washer dryer match":washer_dryer_match,
    "pool":pool,
#   "pool install":pool_install,
    "hot tub":hot_tub,
    "driveway" : driveway,
    "garage_install" : garage,
#   "Garage Type" : garage_install,
    "AC_type": AC_type_str,
    "heat_type": heat_type_str,
    "fireplaces": fireplaces,
    "electric system": electric_system,
    "water type": water_type,
    "foundation material" : foundation_material_str,
    "porch" : porch,
    "patio" : patio,
    "yard" : yard,
#   "additional factors" : additional_factors,
    "Total Value" : totalValue

})
    
    
    
with open("results.json", "w") as outfile:
    json.dump(data, outfile)
    input_results = data

with open("C://Users/Kolby Kuratnick/Documents/api_results.json") as json_file:
    api_results = json.load(json_file)



common_year = dict()
input_year_built = input_results['Results'][0]['year_built']
for i in range (1,200):
    if (input_year_built-2) <= api_results[str(i)]['year_built'] and (input_year_built+2) >= api_results[str(i)]['year_built']:
        common_year[str(i)] = api_results[str(i)]['year_built']
common_prop_type = dict()                       #THIS WILL ALMOST NEVER MATCH BECAUSE OF THE DIFFERENT OUTPUT OPTIONS
for i in range (1,200):
    if input_results['Results'][0]['prop_type'] == api_results[str(i)]['prop_type']:
        common_prop_type[str(i)] = api_results[str(i)]['prop_type']
common_prop_sqft = dict()
input_prop_sqft = input_results['Results'][0]['prop_sqft']
for i in range (1,200):
    if  (input_prop_sqft-150) <= api_results[str(i)]['prop_sqft'] and (input_prop_sqft+150) >= api_results[str(i)]['prop_sqft']:
        common_prop_sqft[str(i)] = api_results[str(i)]['prop_sqft']
common_bedrooms = dict()
for i in range (1,200):
    if input_results['Results'][0]['bedrooms'] == api_results[str(i)]['bedrooms']:
        common_bedrooms[str(i)] = api_results[str(i)]['bedrooms']
common_full_bathrooms = dict()
for i in range (1,200):
    if input_results['Results'][0]['full_bathrooms'] == api_results[str(i)]['full_bathrooms']:
        common_full_bathrooms[str(i)] = api_results[str(i)]['full_bathrooms']
common_half_bathrooms = dict()
for i in range (1,200):
    if input_results['Results'][0]['half_bathrooms'] == api_results[str(i)]['half_bathrooms']:
        common_half_bathrooms[str(i)] = api_results[str(i)]['half_bathrooms']
common_roof_type = dict()                    #THIS WILL ALMOST NEVER MATCH BECAUSE OF THE DIFFERENT OUTPUT OPTIONS
for i in range (1,200):
    if input_results['Results'][0]['roof_type'] == api_results[str(i)]['roof_type']:
        common_roof_type[str(i)] = api_results[str(i)]['roof_type']
common_pool = dict()
for i in range (1,200):
    if input_results['Results'][0]['pool'] == api_results[str(i)]['pool']:
        common_pool[str(i)] = api_results[str(i)]['pool']
common_AC_type = dict()
for i in range (1,200):
    if input_results['Results'][0]['AC_type'] == api_results[str(i)]['AC_type']:
        common_AC_type[str(i)] = api_results[str(i)]['AC_type']
common_heat_type = dict()
for i in range (1,200):
    if input_results['Results'][0]['heat_type'] == api_results[str(i)]['heat_type']:
        common_heat_type[str(i)] = api_results[str(i)]['heat_type']
common_basement = dict()
for i in range (1,200):
    if input_results['Results'][0]['basement'] == api_results[str(i)]['basement']:
        common_basement[str(i)] = api_results[str(i)]['basement']


common_year_list = getList(common_year)
common_prop_type_list = getList(common_prop_type)
common_prop_sqft_list = getList(common_prop_sqft)
common_bedrooms_list = getList(common_bedrooms)
common_full_bathrooms_list = getList(common_full_bathrooms)
common_half_bathrooms_list = getList(common_half_bathrooms)
common_roof_type_list = getList(common_roof_type)
common_pool_list = getList(common_pool)
common_AC_type_list = getList(common_AC_type)
common_heat_type_list = getList(common_heat_type)
common_basement_list = getList(common_basement)



best_comp_iter1 = np.intersect1d(common_bedrooms_list, common_full_bathrooms_list)
if (len(best_comp_iter1) > 5):
    best_comp_iter2 = np.intersect1d(best_comp_iter1, common_prop_sqft_list)
else:
    best_comp_iter2 = best_comp_iter1
if (len(best_comp_iter2) > 5):
    best_comp_iter3 = np.intersect1d(best_comp_iter2, common_year_list)
else:
    best_comp_iter3 = best_comp_iter2
if (len(best_comp_iter3) > 5):
    best_comp_iter4 = np.intersect1d(best_comp_iter3, common_half_bathrooms_list)
else:
    best_comp_iter4 = best_comp_iter3
if (len(best_comp_iter4) > 5):
    best_comp_iter5 = np.intersect1d(best_comp_iter4, common_prop_type_list)
else:
    best_comp_iter5 = best_comp_iter4



best_comp_array = np.array([best_comp_iter5])
best_comp_list = best_comp_array.tolist()

best_comps_info = [1]*len(best_comp_list[0])
for a in range (0, len(best_comps_info)):
    for b in range (0, 199):
        if (str(best_comp_list[0][a]) in api_results):
            best_comps_info[a] = api_results[str(best_comp_list[0][a])]
