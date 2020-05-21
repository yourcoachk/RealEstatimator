Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@yourcoachk 
yourcoachk
/
RealEstatimator
forked from lvpalaparthi/RealEstatimator
1
0
2
 Code
 Pull requests 1 Actions
 Projects 0
 Wiki
 Security 0
 Insights
 Settings
RealEstatimator/estimator.py /
@sromano1776 sromano1776 Update estimator.py
c9d899b 1 hour ago
@yourcoachk@sromano1776@lvpalaparthi
1685 lines (1486 sloc)  59.9 KB
  
import json
import numpy as np
import requests
import time
import pprint
import statistics
import os
from pathlib import Path
## Property Value Estimator 
## Takes in user int(input regarding all property details individually to compute the property estimate
## Square foot value is determined by the type of room (bedroom, kitchen, bathroom, etc and then the additional sq footage of the house is estimated as the basic sq ft value dependent on condition)

def get_estated_value(address):
	api_token='2nKlPnJIAiu3cGCgaWWAX6tqSZnRzC'
	punct='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	address_stripped=""
	for char in address:
		if char not in punct:
			address_stripped=address_stripped+char
	address_list=address_stripped.split()
	api_url_base='https://apis.estated.com/v4/property?token='+api_token
	api_ping="&combined_address="
	for x in range(len(address_list)-1):
		if x==0:
			api_ping=api_ping+str(address_list[x])
		else:
			api_ping=api_ping+' '+str(address_list[x])
	api_url=api_url_base+api_ping
	response=requests.get(api_url)
	data=json.loads(response.content.decode('utf-8'))
	value_list=[0,0,0]
	value_list[0]=data['data']['valuation']['low']
	value_list[1]=data['data']['valuation']['value']
	value_list[2]=data['data']['valuation']['high']
	return value_list



def get_by_zip(zip): #Returns properties within a zip code
	api_token='48ed381483aabf5758717c7aa023980f'
	api_url_base='https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/'
	headers = {'Accept': 'application/json', 'apikey': api_token}
	page_size=100
	api_ping='address?postalcode='+str(zip)+'&page=4&pagesize='+str(page_size)
	api_url=api_url_base+api_ping
	response=requests.get(api_url, headers=headers)
	property_list=[]
	if response.status_code==200:
		data=json.loads(response.content.decode('utf-8'))
		for x in range(page_size):
			property_list.append(data['property'][x]['identifier']['obPropId'])
		return property_list
	else:
		return response.status_code



def get_by_name(town): #Returns properties within a certain town name
	api_token='48ed381483aabf5758717c7aa023980f'
	api_url_base='https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/'
	headers = {'Accept': 'application/json', 'apikey': api_token}
	page_size=100
	api_ping='snapshot?cityname='+str(town)+'&page=1&pagesize='+str(page_size)
	api_url=api_url_base+api_ping
	property_list=[]
	response=requests.get(api_url, headers=headers)
	if response.status_code==200:
		data=json.loads(response.content.decode('utf-8'))
		for x in range(page_size):
			property_list.append(data['property'][x]['identifier']['obPropId'])
		return property_list
	else:
		return response.status_code



def get_property_info(prop_id): #Returns JSON object containing information on the current house
	prop_list=[]
	api_token='48ed381483aabf5758717c7aa023980f'
	api_url_base='https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/'
	headers = {'Accept': 'application/json', 'apikey': api_token}
	for x in range(len(prop_id)):
		if (x%10==0 and x!=0 and x!=len(prop_id)): #The API only allows 10 hits/min
							   #so a delay was needed
			print("We've Been Compromised! Beam Me Up Scotty!")
			time.sleep(1)
			print("Last Record Pulled: ")
			pprint.pprint(prop_list[x-1])
			print('/n')
			print('/n')
			time.sleep(75)
			print("Safe To Proceed. Resuming the Mission...")
		api_ping='detail?id='+str(prop_id[x])
		api_url=api_url_base+api_ping
		response=requests.get(api_url, headers=headers)
		if response.status_code==200:
			prop_list.append(json.loads(response.content.decode('utf-8')))
		else:
			prop_list.append(response.status_code)
	return prop_list



def get_crime_stats(zip): #Returns a crime score based on a given zip code. 100 is the national average and 200 is the highest score

	api_token='48ed381483aabf5758717c7aa023980f'
	api_url_base='https://api.gateway.attomdata.com/communityapi/v2.0.0/area/'
	headers = {'Accept': 'application/json', 'apikey': api_token}
	api_ping='full?AreaId=ZI'+str(zip)
	api_url=api_url_base+api_ping
	response=requests.get(api_url, headers=headers)
	if response.status_code==200:
		data=json.loads(response.content.decode('utf-8'))
		return data['response']['result']['package']['item'][0]['cocrmcytotc']
	else:
		return response.status_code



def create_dictionary(prop_list): #Uses the json objects returned from the API to create a dictionary of custom information that our program eneds

	custom_dictionary={}
	for x in range(len(prop_list)):
		dummy={}
		if(prop_list[x]['property'][0]['summary']['propclass']!="Exempt"):
			try:
				dummy['Address']=prop_list[x]['property'][0]['address']['oneLine']
			except:
				dummy['Address']='UNKNOWN'

			try:
				dummy['prop_type']=prop_list[x]['property'][0]['summary']['propclass']
			except:
				dummy['prop_type']=None

			try:
				dummy['year_built']=prop_list[x]['property'][0]['summary']['yearbuilt']
			except:
				dummy['year_built']=None

			try:
				dummy['prop_sqft']=prop_list[x]['property'][0]['building']['size']['livingsize']
			except:
				dummy['prop_sqft']=None

			try:
				dummy['prop_condition']=prop_list[x]['property'][0]['building']['construction']['condition']
			except:
				dummy['prop_condition']=None

			dummy['bedrooms']=prop_list[x]['property'][0]['building']['rooms']['beds']

			dummy['full_bathrooms']=prop_list[x]['property'][0]['building']['rooms']['bathsfull']

			dummy['half_bathrooms']=prop_list[x]['property'][0]['building']['rooms']['bathshalf']

			try:
				dummy['roof_type']=prop_list[x]['property'][0]['building']['construction']['roofcover']
			except:
				dummy['roof_type']=None

			try:
				dummy['pool']=prop_list[x]['property'][0]['lot']['pooltype']
			except:
				dummy['pool']=None

			try:
				dummy['garage_install']=prop_list[x]['property'][0]['building']['parking']['prkgType']
			except:
				dummy['garage_install']=None

			try:
				dummy['AC_type']=prop_list[x]['property'][0]['utilities']['coolingtype']
			except:
				dummy['AC_type']=None

			try:
				dummy['heat_type']=prop_list[x]['property'][0]['utilities']['heatingtype']
			except:
				dummy['heat_type']=None

			try:
				if (prop_list[x]['property'][0]['interior']['bsmtsize']!=0):
					dummy['basement']=prop_list[x]['property'][0]['interior']['bsmtsize']
				else:
					dummy['basement']=None
			except:
				dummy['basement']=None

			try:
				dummy['Siding Type']=prop_list[x]['property'][0]['building']['construction']['wallType']
			except:
				dummy['Siding Type']=None

			custom_dictionary[x]=dummy
	return custom_dictionary



def get_school_info(zip: str):
	coordinates=get_lat_long(zip)
	lat=coordinates[0]
	lon=coordinates[1]
	page_size=30
	api_token='48ed381483aabf5758717c7aa023980f'
	api_url_base='https://api.gateway.attomdata.com/propertyapi/v1.0.0/school/snapshot?'
	api_ping='latitude='+str(lat)+'&longitude=%20'+str(lon)+'&page=1&pagesize='+str(page_size)
	api_url=api_url_base+api_ping
	headers = {'Accept': 'application/json', 'apikey': api_token}
	response=requests.get(api_url, headers=headers)
	if response.status_code==200:
		ratings=[]
		data=json.loads(response.content.decode('utf-8'))
		for x in range(len(data['school'])):
			if (data['school'][x]['School']['GSTestRating']!=0):
				ratings.append(data['school'][x]['School']['GSTestRating'])
		ratings=sorted(ratings)
		return statistics.median(ratings)
	else:
		return response.status_code



def get_lat_long(zip): #Returns lat and long for API use based on ZIP code
	url='https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q='+str(zip)
	data=json.loads((requests.get(url)).content.decode('utf-8'))
	if (data['nhits']==0):
		return None
	else:
		return data['records'][0]['fields']['geopoint']
    


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

totalValue = 0

print("Welcome to the Property Value Estimator.....Please answer some questions!\n\n")
print("You will be asked about the condition of various aspects of your home. Here is some information to help you.\nPoor is 15% of homes, average is 50% of homes, good is 20% of homes, and excellent is 15% of homes. Typically excellent is reserved for new construction or very recently remodeled homes.\n\n")
print("Please enter your answers exactly how they are represented in the question.\n\n")
address = input("Enter the property's address (street address town, state zipcode): ") #VALUE STILL NEEDED
zipcode = int(input("Please confirm the property's zipcode: "))

while True:
    try:
        prop_type = int(input("Choose the property type:\n(0) Single Family Home\n(1) Duplex\n(2) Triplex\n(3) Manufactured\n(4) Townhouse\n(5) Condo\n(6) Mobile Home\n(7) Apartment\n\n"))
        prop_type_arr = ['Single Family Home','Duplex','Triplex','Manufactured', 'Townhouse','Condo', 'Mobile Home', 'Apartment']
        prop_type_str = prop_type_arr[prop_type]
        if prop_type in range(8):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')



#YEAR BUILT
while True:
    try:
        year_built = int(input("Enter the year the property was built: "))
        if (year_built >= 2000 and year_built <= 2020):
            year_built_value = (year_built-2000)*500
            totalValue = totalValue + year_built_value
            break
        elif (year_built < 1975 and year_built >=1800):
            year_built_value = (1975-year_built)*-500
            totalValue = totalValue + year_built_value
            break
        elif (year_built<1800):
            print('\nSorry this estimator cannot the value of houses built before 1800. Please try again!')
            pass
        else:
            totalValue = totalValue
            break
    except:
        pass
    print('\nIncorrect input, try again!')
#END YEAR BUILT
    

    
#PROPERTY CONDITION
while True:
    try:
        prop_condition = int(input("Choose the current property condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
        prop_cond_arr = ['Poor', 'Average', 'Good','Excellent']
        prop_type_str = prop_cond_arr[prop_condition]
        if prop_condition in range(4):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
prop_value = 0
def switch_property_value(prop_condition):
    prop_val = {
        0: 100,
        1: 125,
        2: 150,
        3: 165
    }.get(prop_condition, "Invalid, will not be considered")
    return prop_val
prop_value = switch_property_value(prop_condition)
#END PROPERTY CONDITION
    


#PROPERTY SQUARE FOOTAGE
while True:
    try:
        prop_sqft = int(input("Note: the basement is not counted in a property's square footage.\nEnter the total interior livable square footage: "))
        if prop_sqft>=0:
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
#END PROPERTY SQUARE FOOTAGE



#LOT SQUARE FOOTAGE
while True:
    try:
        lot_sqft = int(input("Enter the lot square footage: "))
        if lot_sqft>=0:
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
while True:
   try:
       lot_condition = int(input("Choose the current lot condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
       if lot_condition in range(4):
           break
   except:
       pass
   print ('\nIncorrect input, try again!')
lot_sqft = lot_sqft - prop_sqft
totalValue = totalValue+(lot_sqft*3.55)
#END LOT SQUARE FOOTAGE



#BEDROOMS
bedrooms=-1
while(bedrooms<0):
    try:
        bedrooms = int(input("Enter total number of bedrooms: "))
        if bedrooms<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
bedroom_total_sqft = 0
bedroom_final_value = 0
bedroom_x_value =0
def switch_bedroom_value(bedroom_x_condition):
    switcher_bedroom = {
        0: bedroom_x_sqft*60,
        1: bedroom_x_sqft*80,
        2: bedroom_x_sqft*90,
        3: bedroom_x_sqft*100,
        }.get(bedroom_x_condition, "Invalid, will not be considered")
    return switcher_bedroom

for x in range(1, bedrooms+1):
   if(bedrooms == 0):
       break
   else:
       print ("Bedroom", x, ":")
       bedroom_x_sqft=-1
       while(bedroom_x_sqft<1):
           bedroom_x_sqft = int(input("Enter bedroom " + str(x) +" sqft: "))
           if bedroom_x_sqft<1:
               print("\nIncorrect input, try again!")
       bedroom_total_sqft = bedroom_total_sqft+bedroom_x_sqft
       while True:
           try:
               bedroom_x_condition = int(input("Bedroom " + str(x) + " Choose the bedroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
               if bedroom_x_condition in range(4): 
                   bedroom_final_value = bedroom_final_value+ switch_bedroom_value(bedroom_x_condition)                 
                   break
           except:
               pass
           print ('\nIncorrect input, try again!')
totalValue = totalValue + bedroom_final_value
prop_sqft_remaining = prop_sqft - bedroom_total_sqft
#END BEDROOMS



#FULL BATHROOMS
fbath_total_sqft = 0
fbath_total_value = 0
full_bathrooms=-1
while(full_bathrooms<0):
    try:
        full_bathrooms = int(input("Enter total number of full bathrooms: "))
        if full_bathrooms<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
for x in range(1, full_bathrooms+1):
    if(full_bathrooms == 0):
        break
    else:
        print ("Full Bathroom", x, ":")
        fbath_x_sqft = -1
        while(fbath_x_sqft < 1):
            try:
                fbath_x_sqft = int(input("Enter full bathroom " + str(x) +" sqft: "))
                if fbath_x_sqft < 1:
                    print("\nIncorrect input, try again!")
            except:
                    print("\nIncorrect input, try again!")
                    continue
        fbath_total_sqft = fbath_total_sqft + fbath_x_sqft
        while True:
            try:
                fbath_x_condition = int(input("Full Bathroom " + str(x) + ": Choose the full bathroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
                if fbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        def switch_fbath_condition(fbath_x_condition):
            switcher_fbath_condition = {
                0: fbath_x_sqft*30,
                1: fbath_x_sqft*50,
                2: fbath_x_sqft*60,
                3: fbath_x_sqft*70,
            }.get(fbath_x_condition, "Invalid, will not be considered")
            return switcher_fbath_condition
        while True:
            try:
                fbath_x_floor_material=int(input("Choose the full bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n"))
                if fbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        def switch_fbath_floor_material(fbath_x_floor_material):
            switcher_fbath_floor_material = {
                0: 0,
                1: fbath_x_sqft*5,
                2: fbath_x_sqft*2,
                3: fbath_x_sqft*10,
                4: fbath_x_sqft*2,
            }.get(fbath_x_floor_material, "Invalid, will not be considered")
            return switcher_fbath_floor_material
        while True:
            try:
                fbath_x_ctop_material=int(input("Choose the full bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
                if fbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        fbath_x_ctop_sqft=-1
        while(fbath_x_ctop_sqft<1):
            try:
                fbath_x_ctop_sqft = int(input("Enter the counter's square footage: "))
                if fbath_x_ctop_sqft<1:
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        def switch_fbath_counter_material(fbath_x_ctop_material):
            switcher_fbath_counter_material = {
                0: fbath_x_ctop_sqft*40,
                1: fbath_x_ctop_sqft*40,
                2: fbath_x_ctop_sqft*70,
                3: fbath_x_ctop_sqft*55,
                4: fbath_x_ctop_sqft*20,
                5: fbath_x_ctop_sqft*10,
            }.get(fbath_x_ctop_material, "Invalid, will not be considered")
            return switcher_fbath_counter_material
        fbath_total_value = fbath_total_value + switch_fbath_counter_material(fbath_x_ctop_material) + switch_fbath_floor_material(fbath_x_floor_material) + switch_fbath_condition(fbath_x_condition)

prop_sqft_remaining = prop_sqft_remaining - fbath_total_sqft
totalValue = totalValue + fbath_total_value
#END FULL BATHROOMS



#HALF BATHROOMS
hbath_total_sqft = 0
hbath_total_value = 0
half_bathrooms=-1
while half_bathrooms<0:
    try:
        half_bathrooms = int(input("Enter total number of half bathrooms: "))
        if half_bathrooms<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
for x in range(1, half_bathrooms+1):
    if(half_bathrooms == 0):
        break
    else:
        print ("Half Bathroom", x, ":")
        hbath_x_sqft = -1
        while(hbath_x_sqft < 1):
            try:
                hbath_x_sqft = int(input("Enter half bathroom " + str(x) +" sqft: "))
                if hbath_x_sqft < 1:
                    print("\nIncorrect input, try again!")
            except:
                    print("\nIncorrect input, try again!")
                    continue
        
        hbath_total_sqft = hbath_total_sqft + hbath_x_sqft
        while True:
            try:
                hbath_x_condition = int(input("Half Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0)Poor\n(1)Average\n(2)Good\n(3)Excellent\n\n"))
                if hbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        def switch_hbath_condition(hbath_x_condition):
            switcher_hbath_condition = {
                0: hbath_x_sqft*30,
                1: hbath_x_sqft*50,
                2: hbath_x_sqft*60,
                3: hbath_x_sqft*70,
            }.get(hbath_x_condition, "Invalid, will not be considered")
            return switcher_hbath_condition
        while True:
            try:
                hbath_x_floor_material=int(input("Choose the half bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n"))
                if hbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        def switch_hbath_floor_material(hbath_x_floor_material):
            switcher_hbath_floor_material = {
                0: 0,
                1: hbath_x_sqft*5,
                2: hbath_x_sqft*2,
                3: hbath_x_sqft*10,
                4: hbath_x_sqft*2,
            }.get(hbath_x_floor_material, "Invalid, will not be considered")
            return switcher_hbath_floor_material
        while True:
            try:
                hbath_x_ctop_material=int(input("Choose the half bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
                if hbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        hbath_x_ctop_sqft=-1
        while(hbath_x_ctop_sqft<1):
            try:
                hbath_x_ctop_sqft = int(input("Enter the counter's square footage: ")) 
                if hbath_x_ctop_sqft<1:
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        def switch_hbath_counter_material(hbath_x_ctop_material):
            switcher_hbath_counter_material = {
                0: hbath_x_ctop_sqft*40,
                1: hbath_x_ctop_sqft*40,
                2: hbath_x_ctop_sqft*70,
                3: hbath_x_ctop_sqft*55,
                4: hbath_x_ctop_sqft*20,
                5: hbath_x_ctop_sqft*10,
            }.get(hbath_x_ctop_material, "Invalid, will not be considered")
            return switcher_hbath_counter_material
        hbath_total_value = hbath_total_value + switch_hbath_counter_material(hbath_x_ctop_material) + switch_hbath_floor_material(hbath_x_floor_material) + switch_hbath_condition(hbath_x_condition)
prop_sqft_remaining = prop_sqft_remaining - hbath_total_sqft
totalValue = totalValue + hbath_total_value
#END HALF BATHROOMS



#KITCHEN
kitchen_sqft=-1
while kitchen_sqft<0:
    try:
        kitchen_sqft = int(input("Enter the square footage of the kitchen: "))
        if kitchen_sqft<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
while True:
    try:
        kitchen_condition = int(input("Choose the kitchen condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
        if kitchen_condition in range(4):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
def switch_kitchen_condition(kitchen_condition):
    switcher_kitchen_condition = {
        0: kitchen_sqft*30,
        1: kitchen_sqft*50,
        2: kitchen_sqft*60,
        3: kitchen_sqft*70,
    }.get(kitchen_condition, "Invalid, will not be considered")
    return switcher_kitchen_condition
while True:
    try:
        kitchen_floor_material=int(input("Choose the kitchen floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n"))
        if kitchen_floor_material in range(5):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
def switch_kitchen_floor_material(kitchen_floor_material):
    switcher_kitchen_floor_material = {
        0: 0,
        1: kitchen_sqft*5,
        2: kitchen_sqft*2,
        3: kitchen_sqft*10,
        4: kitchen_sqft*2,
    }.get(kitchen_floor_material, "Invalid, will not be considered")
    return switcher_kitchen_floor_material
while True:
    try:
        kitchen_ctop_material=int(input("Choose the kitchen countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
        if kitchen_ctop_material in range(6):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
kitchen_ctop_sqft=-1
while(kitchen_ctop_sqft<1):
   try:
       kitchen_ctop_sqft = int(input("Enter the counter's square footage: "))
       if kitchen_ctop_sqft<1:
           print("\nIncorrect input, try again!")
   except:
       print("\nIncorrect input, try again!")
       continue
def switch_kitchen_counter_material(kitchen_ctop_material):
    switcher_kitchen_counter_material = {
        0: kitchen_ctop_sqft*40,
        1: kitchen_ctop_sqft*40,
        2: kitchen_ctop_sqft*70,
        3: kitchen_ctop_sqft*55,
        4: kitchen_ctop_sqft*20,
        5: kitchen_ctop_sqft*10,
    }.get(kitchen_ctop_material, "Invalid, will not be considered")
    return switcher_kitchen_counter_material

prop_sqft_remaining = prop_sqft_remaining - kitchen_sqft

totalValue = totalValue + switch_kitchen_condition(kitchen_condition) + switch_kitchen_floor_material(kitchen_floor_material) + switch_kitchen_counter_material(kitchen_ctop_material)
#END KITCHEN



#REMAINING SQUARE FOOTAGE
prop_sqft_final = prop_value*prop_sqft_remaining        #FINAL Remaining SQ FT. Represents Prop_SqFt - kitchen sqft - total bedroom sqft - bathroom sqft
#END REMAINING SQUARE FOOTAGE



#BASEMENT
basement_finished_sqft = 0
basement_value = 0
def switch_basement_finished_value(basement_condition):
    switcher_basement_finished_val={ 
        0: basement_finished_sqft*30,
        1: basement_finished_sqft*45,
        2: basement_finished_sqft*60,
        3: basement_finished_sqft*75
    }.get(basement_condition, "Invalid, will not be considered")
    return switcher_basement_finished_val
    
def switch_basement_unfinished_value(basement_condition):
    switcher_basement_unfinished = {
        0: basement_unfinished_sqft*10,
        1: basement_unfinished_sqft*15,
        2: basement_unfinished_sqft*20,
        3: basement_unfinished_sqft*25,
    }.get(basement_condition, "Invalid, will not be considered")
    return switcher_basement_unfinished

basement=""
while (basement!="yes" and basement!="none"):
    basement=""
    basement = input("Is there a basement (yes or none): ")
    if (str(basement)!="yes" and str(basement)!="none"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'none'")
if(basement == "yes"):
    while True:
        try:
            basement_condition = int(input("Choose the current basement condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
            if basement_condition in range(4):
                break
        except: 
            pass
            print ('\nIncorrect input, try again!')
    basement_sqft=-1
    while(basement_sqft<=0):
        try:
            basement_sqft = int(input("Enter the square footage of the basement: "))
            if basement_sqft<=0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    basement_finished=-1
    while(basement_finished<0 or basement_finished>100):
        try:
            basement_finished = int(input("Please enter the percentage of the basement that is finished (0 to 100): "))
            if (basement_finished<0 or basement_finished>100):
                print("\nIncorrect input, try again! Make sure to put the percentage from 0 to 100")
        except:
            print("\nIncorrect input, try again! Make sure to put the percentage from 0 to 100")
            continue
        basement_finished_sqft = basement_sqft*(basement_finished*.01)
        basement_value = basement_value + switch_basement_finished_value(basement_condition)
        basement_unfinished_sqft = basement_sqft - basement_finished_sqft
        basement_value = basement_value + switch_basement_unfinished_value(basement_condition)
        basement_door=""
    while (basement_door!="yes" and basement_door!="no"):
        basement_door=""
        basement_door = input("Is it a walk out basement (yes or no): ")
        if (str(basement_door)!="yes" and str(basement_door)!="no"):
            print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
    if(basement_door == "yes"):
        basement_value = basement_value*1.2
    totalValue = totalValue + basement_value
#END BASEMENT



#ROOF
roof_sum = 0
roof_age=-1
while(roof_age not in range(0,101)):
    try:
        roof_age = int(input("How old is the roof (enter a number rounded to nearest year): "))
        if(roof_age not in range(0,101)):
            print('\nIncorrect input, try again!')
    except:
        print('\nIncorrect input, try again!')
        continue
while True:
    try:
        roof_type = int(input("Choose the roof type\n(0) Slate Tile\n(1) Clay Tile\n(2) Copper\n(3) Other Metals\n(4) Wood Shingle\n(5) Fiber Cement Shingles\n(6) Asphalt Shingles\n(7) Other\n\n"))
        roof_arr = ['Slate Tile', 'Clay Tile', 'Copper', 'Other Metals', 'Wood Shingle', 'Fiber Cement Shingles','Asphalt Shingles', 'Other']
        roof_type_str = roof_arr[roof_type]
        if roof_type in range(8):
            break
    except:
        pass
    print('\nIncorrect input, try again!')
if(roof_type == 7):
    roof_other = input("Enter the roof type that the property contains: ")
def switch_roof(roof_type):
    roof_val ={
        0: 80 - roof_age,
        1: 80 - roof_age,
        2: 80 - roof_age,
        3: 60 - roof_age,
        4: 30 - roof_age,
        5: 25 - roof_age,
        6: 20 - roof_age,
        7: 20 - roof_age
    }.get(roof_type,"Invalid, will not be considered" )
    return roof_val
roof_sum = switch_roof(roof_type)
#print(roof_sum)
if (roof_sum > 12):
   totalValue = totalValue + roof_sum*100
elif (roof_sum > 7 and roof_sum < 12):
   totalValue = totalValue
elif (roof_sum > 4 and roof_sum <= 7):
   totalValue = totalValue - (8-roof_sum)*300
elif (roof_sum > 1 and roof_sum <= 4):
   totalValue = totalValue - (5-roof_sum)*1800
else:
   totalValue = totalValue - 10000 #cost of new roof
#END ROOF





# #APPLIANCES
kitchen_appliances_value = 0
washer_dryer_value = 0
washer=""
while (washer!="yes" and washer!="no"):
    washer=""
    washer = input("Does property come with a washer? (yes or no): ")
    if (str(washer)!="yes" and str(washer)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'") 
if (washer == "yes"):
    washer_dryer_value = 250


dryer=""
while (dryer!="yes" and dryer!="no"):
    dryer=""
    dryer = input("Does property come with a dryer? (yes or no): ")
    if (str(dryer)!="yes" and str(dryer)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (dryer == "yes"):
    washer_dryer_value = washer_dryer_value + 185


dishwasher=""
while (dishwasher!="yes" and dishwasher!="no"):
    dishwasher=""
    dishwasher = input("Does property come with a dishwasher? (yes or no): ")
    if (str(dishwasher)!="yes" and str(dishwasher)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (dishwasher == "yes"):
    kitchen_appliances_value = 175


fridge=""
while (fridge!="yes" and fridge!="no"):
    fridge=""
    fridge = input("Does property come with a fridge? (yes or no): ")
    if (str(fridge)!="yes" and str(fridge)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (fridge == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 350


microwave=""
while (microwave!="yes" and microwave!="no"):
    microwave=""
    microwave = input("Does property come with a microwave? (yes or no): ")
    if (str(microwave)!="yes" and str(microwave)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (microwave == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 20


stove=""
while (stove!="yes" and stove!="no"):
    stove=""
    stove = input("Does property come with a stove? (yes or no): ")
    if (str(stove)!="yes" and str(stove)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (stove == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 250


kitchen_match=""
while (kitchen_match!="yes" and kitchen_match!="no"):
    kitchen_match=""
    kitchen_match = input("Do all of the kitchen appliances match in color? (yes or no): ")
    if (str(kitchen_match)!="yes" and str(kitchen_match)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (kitchen_match == "yes"):
    kitchen_appliances_value = kitchen_appliances_value * 1.2


washer_dryer_match=""
while (washer_dryer_match!="yes" and washer_dryer_match!="no"):
    washer_dryer_match=""
    washer_dryer_match = input("Do the washer and dryer match in color? (yes or no): ")
    if (str(washer_dryer_match)!="yes" and str(washer_dryer_match)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if (washer_dryer_match == "yes"):
    washer_dryer_value = washer_dryer_value * 1.2

totalValue = totalValue + washer_dryer_value + kitchen_appliances_value
# #END APPLIANCES


#IN THE FUTURE, SOME FURNITURE QUESTIONS MAY BE ASKED HERE


#POOL
pool=""
while (pool!="yes" and pool!="none"):
    pool=""
    pool = input("Is there a pool installed? (yes or none): ")
    if (str(pool)!="yes" and str(pool)!="none"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'none'")
if(pool == "yes"):
   pool_install=""
   while (pool_install!="in-ground" and pool_install!="above-ground"):
        pool_install=""
        pool_install = input("Enter if the pool is 'in-ground' or 'above-ground': ")
        if (str(pool_install)!="in-ground" and str(pool_install)!="above-ground"):
            print("\nIncorrect Input! Plase be sure to type out the full word 'in-ground' or 'above-ground'")
   pool_sqft=-1
   while(pool_sqft<=0):
       try:
           pool_sqft = int(input("Enter the square footage of the pool: "))
           if pool_sqft<=0:
               print("\nIncorrect input, try again!")
       except:
           print("\nIncorrect input, try again!")
           continue
   if (pool_sqft >= .6*lot_sqft):
       totalValue = totalValue - 1000
   else:
       if (pool_install == "above-ground"):
           totalValue = totalValue - 500
       elif (pool_install == "in-ground"):
           totalValue = totalValue + 500
       else:
           print ("Invalid, will not be considered")
#END POOL
           
           

#HOT TUB
hot_tub=""
while (hot_tub!="yes" and hot_tub!="no"):
    hot_tub=""
    hot_tub = input("Is there a hot tub installed? (yes or no): ")
    if (str(hot_tub)!="yes" and str(hot_tub)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if(hot_tub == "yes"):
    while True:
        try:
            hot_tub_material = int(input("Choose the hot tub interior type\n(0) Inflatable\n(1) Custom Portable\n(2) Custom in-ground\n(3) Other\n\n"))
            if hot_tub_material in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    hot_tub_size=-1
    while(hot_tub_size<=0):
        try:
            hot_tub_size = int(input("Enter how many people the hot tub is meant for: "))
            if hot_tub_size<=0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    hot_tub_init_value = hot_tub_size*150
    def switch_hot_tub(hot_tub_material):
        switcher_hot_tub = {
            0:hot_tub_init_value - 500,
            1:hot_tub_init_value + 200,
            2:hot_tub_init_value + 500,
            3:hot_tub_init_value
        }.get(hot_tub_material, "Invalid, will not be considered")
        return switcher_hot_tub
    totalValue = totalValue + switch_hot_tub(hot_tub_material)
#END HOT TUB



#DRIVEWAY
driveway=""
while (driveway!="yes" and driveway!="none"):
    driveway=""
    driveway = input("Is there a driveway? (yes or none): ")
    if (str(driveway)!="yes" and str(driveway)!="none"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'none'")
if(driveway == "yes"):
    driveway_sqft=-1
    while(driveway_sqft<=0):
        try:
            driveway_sqft = int(input("Enter the driveway square footage: "))
            if driveway_sqft<=0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    while True:
        try:
            driveway_material = int(input("Choose the driveway material\n(0) Concrete\n(1) Brick\n(2) Rock\n(3) Asphalt\n\n"))
            if driveway_material in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    def switch_driveway_material(driveway_material):
        drive_mat_switcher = {
            0: driveway_sqft * 5,
            1: driveway_sqft * 2,
            2: driveway_sqft * 1,
            3: driveway_sqft * 3,
        }.get(driveway_material, "Invalid, will not be considered")
        return drive_mat_switcher
    driveway_value = switch_driveway_material(driveway_material)
    while True:
        try:
            driveway_condition = int(input("Choose the current driveway condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
            if driveway_condition in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    def switch_driveway_value(driveway_condition):
        driveway_val_switch = {
            0: driveway_value *0.8,
            1: driveway_value *1,
            2: driveway_value *1.1,
            3: driveway_value *1.2
        }.get(driveway_condition, "Invalid, will not be considered")
        return driveway_val_switch
    driveway_value =  switch_driveway_value(driveway_condition)
    totalValue = totalValue + driveway_value
#END OF DRIVEWAY



#GARAGE
garage=""
while (garage!="yes" and garage!="none"):
    garage=""
    garage = input("Is there a garage installed? (yes or none): ")
    if (str(garage)!="yes" and str(garage)!="none"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'none'")
if(garage == "yes"):
    garage_install=""
    while (garage_install!="attached" and garage_install!="detached"):
        garage_install=""
        garage_install = input("Enter if garage is 'attached' or 'detached': ") #This actually doesn't matter much as the pros and cons tend to equal out and become dependent on the person
        if (str(garage_install)!="attached" and str(garage_install)!="detached"):
            print("\nIncorrect Input! Plase be sure to type out the full word 'attached' or 'detached'")
    garage_sqft=-1
    while(garage_sqft<=0):
        try:
            garage_sqft = int(input("Enter the square footage of the garage: "))
            if garage_sqft<=0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    while True:
        try:
            garage_condition = int(input("Choose the current garage condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
            if garage_condition in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    garage_value = garage_sqft*10                #average 400 sq ft garage valued at $16k
    def switch_garage_value(garage_condition):
        garage_value_switch = {
            0: garage_value * 0.8,
            1: garage_value * 1,
            2: garage_value * 1.1,
            3: garage_value * 1.2
        }.get(garage_condition, "Invalid, will not be considered")
        return garage_value_switch
    totalValue = totalValue + switch_garage_value(garage_condition)   
#END GARAGE



#AC TYPE
AC_type=-1
while(AC_type not in range(0,6)):
    try:     
        AC_type = int(input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n"))
        if AC_type not in range(0,6):
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
AC_arr = ['Window Units','House Fan','Central Air','Ductless Mini-Split AC','Geothermal', 'Other']
AC_type_str = AC_arr[AC_type]         
if(AC_type == 5):
   AC_other = input("Enter the AC type that the property contains: ")
def switch_AC(AC_type):
    switcher_AC = {
            0: -500,
            1: -400,
            2: 0,
            3: 0,
            4: 500,
            5: 0
    }.get(AC_type,"Invalid, will not be considered")
    return switcher_AC
totalValue = totalValue + switch_AC(AC_type)
#END AC TYPE



#HEAT TYPE
heat_type=-1
while(heat_type not in range(0,6)):
    try:     
        heat_type = int(input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n"))
        if heat_type not in range(0,6):
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
heat_arr=['Boiler', 'Furnace', 'Standard Heat Pump', 'Mini Split Heat Pump', 'Geothermal', 'Other']
heat_type_str = heat_arr[heat_type]
if(heat_type == 5):
   heat_other = input("Enter the heat type that the property contains: ")
def switch_Heat(heat_type):
    totalValue_switch = {
        0: -500,
        1: -350,
        2: 0,
        3: 0,
        4: 500,
        5: 0
    }.get(heat_type,"Invalid, will not be considered")
    return totalValue_switch 
totalValue = totalValue + switch_Heat(heat_type)
#END HEAT TYPE   
   
 

#FIREPLACES 
fireplaces=-1
while(fireplaces<0):
    try:
        fireplaces = int(input("Enter the number of fireplaces if installed and 0 if none: \n"))
        if fireplaces<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
totalValue = totalValue+(fireplaces*800)
#END FIREPLACES



#ELECTRIC SYSTEM
electric_system=-1
while(electric_system!=0 and electric_system!=1):
    try:
        electric_system = int(input("Please enter 0 if the electric system is 'fuse box' or a 1 if it is 'circuit breaker'\n"))
        if electric_system<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
if (electric_system == 0):
   totalValue = totalValue-500
#END ELECTRIC SYSTEM



#view_type = int(input("Choose all view types (enter as many letters as applicable):\n(0) River\n(1) Lake\n(2) Ocean\n(3) Golf Course\n(4) Mountain\n(5) Skyline\n(6) Standard\n\n") #VALUE STILL NEEDED
#In Bear, DE there isn't a very large difference in the type of view each house has. There's no ocean, lake, mountain, large hill, river, skyline in the area.



#WATER TYPE
water_type=-1
while(water_type!=0 and water_type!=1):
    try:
        water_type =int(input("Please enter 0 if the water/sewage system is 'town' or 1 if it is 'septic+well'\n"))
        if electric_system<0:
            print("\nIncorrect input, try again!")
    except:
        print("\nIncorrect input, try again!")
        continue
if(water_type == 1):
   totalValue = totalValue-1000
#END WATER TYPE



#FOUNDATION MATERIAL
while True:
    try:
        foundation_material = int(input("Choose the foundation material\n(0) Stone\n(1) Brick\n(2) Preservative treated lumber\n(3) Concrete Block\n(4) Poured Concrete\n(5) Other\n\n"))
        foundation_arr = ['Stone', 'Brick', 'Preservative treated lumber', 'Concrete Block', 'Poured Concrete', 'Other']
        foundation_material_str = foundation_arr[foundation_material]
        if foundation_material in range(6):
            break
    except:
        pass
    print('\nIncorrect input, try again!')
if(foundation_material == 5):
   foundation_other = input("Enter the foundation material that the property contains: ")
def switch_foundation_material(foundation_material):
    foundation_switcher = {
        0: -10000,
        1: -3000,
        2: -8000,
        3: -500,
        4: 0,
        5: 0
    }.get(foundation_material,"Invalid, will not be considered")
    return foundation_switcher
totalValue = totalValue + switch_foundation_material(foundation_material)
#END FOUNDATION MATERIAL



#PORCH
porch=""
while (porch!="yes" and porch!="no"):
    porch=""
    porch = input("Is there a porch (yes or no)?: ")
    if (str(porch)!="yes" and str(porch)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if(porch == "yes"):
    porch_num=-1
    while(porch_num<0):
        try:
            porch_num = int(input("Enter the number of porches: "))
            if porch_num<0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    
    for x in range (1, porch_num+1):
        print ("Porch", x, ":")
        porch_x_sqft=-1
        while(porch_x_sqft<=0):
            try:
                porch_x_sqft = int(input("Enter porch " + str(x) +" sqft: "))
                if porch_x_sqft<0:
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        porch_x_material=-1
        while(porch_x_material not in range(0,4)):
            try:     
                porch_x_material = int(input("Choose the porch material\n(0) Wood\n(1) Concrete\n(2) Plastic Wood Composites\n(3) Other\n\n"))
                if porch_x_material not in range(0,6):
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        porch_total_value = 0
        def switch_porch_material(porch_x_material):
            porch_switcher = {
                    0: porch_x_sqft*5,
                    1: porch_x_sqft*3,
                    2: porch_x_sqft*4,
                    3: porch_x_sqft*2,
            }.get(porch_x_material,"Invalid, will not be considered")
            return porch_switcher
        porch_total_value = porch_total_value+switch_porch_material(porch_x_material)
        totalValue = totalValue + porch_total_value
        if(porch_x_material == "3"):
            porch_other = input("Enter the porch material that the property contains: ")
#END PORCH



#PATIO
patio_total_value = 0
patio=""
while (patio!="yes" and patio!="no"):
    patio=""
    patio = input("Is there a patio (yes or no)?: ")
    if (str(patio)!="yes" and str(patio)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if(patio == "yes"):
    patio_num=-1
    while(patio_num<0):
        try:
            patio_num = int(input("Enter the number of patios: "))
            if patio_num<0:
                print("\nIncorrect input, try again!")
        except:
            print("\nIncorrect input, try again!")
            continue
    for x in range (1, patio_num+1):
        print ("Patio", x, ":")
        patio_x_sqft=-1
        while(patio_x_sqft<=0):
            try:
                patio_x_sqft = int(input("Enter patio " + str(x) +" sqft: "))
                if patio_x_sqft<0:
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        patio_x_material=-1
        while(patio_x_material not in range(0,6)):
            try:     
                patio_x_material = int(input("Choose the patio material\n(0) Brick\n(1) Stone\n(2) Patio Pavers\n(3) Concrete\n(4) Gravel\n(5) Other\n\n"))
                if patio_x_material not in range(0,6):
                    print("\nIncorrect input, try again!")
            except:
                print("\nIncorrect input, try again!")
                continue
        def switch_patio_material(patio_x_material):
            patio_switcher = {
                    0: patio_x_sqft*4,
                    1: patio_x_sqft*6,
                    2: patio_x_sqft*3,
                    3: patio_x_sqft*4,
                    4: patio_x_sqft*1,
                    5: patio_x_sqft*1
            }.get(patio_x_material,"Invalid, will not be considered")
            return patio_switcher
        patio_total_value = patio_total_value+switch_patio_material(patio_x_material)
        if(patio_x_material == 5):
            patio_other = input("Enter the patio material that the property contains: ")
totalValue = totalValue + patio_total_value
#END PATIO



#FENCED IN YARD
yard=""
while (yard!="yes" and yard!="no"):
    yard=""
    yard = input("Is there a yard fenced in (yes or no)?: ")
    if (str(yard)!="yes" and str(yard)!="no"):
        print("\nIncorrect Input! Plase be sure to type out the full word 'yes' or 'no'")
if(yard == "yes"):
    while True:
        try:
            yard_material = int(input("Choose the fence material\n(0) Chain Link\n(1) Picket Fence\n(2) Synthetic\n(3) Aluminum\n(4) Privacy Vinyl\n(5) Composite\n(6) Privacy Wood\n(7) Other\n\n"))
            if yard_material in range(8):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    if(yard_material == 7):
        yard_other = input("Enter the fence material that the property contains: ")
    def switch_yard_material(yard_material):
        yard_switcher = {
            0: 200,
            1: 500,
            2: 500,
            3: 300,
            4: 800,
            5: 400,
            6: 700,
            7: 300
            }.get(yard_material, "Invalid, will not be considered")
        return yard_switcher
    totalValue = totalValue + switch_yard_material(yard_material)
#END FENCED IN YARD



#ADDITIONAL FACTORS
additional_factors = input("Are there any additional factor(s) that should be considered (yes or no)?: ")
if(additional_factors == "yes"):
    add_fac_yes = input("Please list the additional factors: ")
#END ADDITIONAL FACTORS
    
    
    
#ADJUST PREDICTION BASED ON PROPERTY TYPE
def switch_prop_type(prop_type):
    switcher_prop = {
        0: 1,
        1: .95,
        2: .9,
        3: .9,
        4: .8,
        5: .7,
        6: .5,
        7: .5,
        }.get(prop_type, "Invalid, will not be considered")
    return switcher_prop
totalValue = totalValue * switch_prop_type(prop_type)
#END ADJUST PREDICTION BASED ON PROPERTY TYPE



#Start Adjust Prediction Based on Crime
crime = get_crime_stats(zipcode)
if(int(crime)<12):
    totalValue=totalValue-(totalValue*0.06)
elif(int(crime)>=12 and int(crime) <25):
    totalValue=totalValue-(totalValue*0.04)
elif(int(crime)>=25 and int(crime)<50):
    totalValue=totalValue-(totalValue*0.02)
elif(int(crime)>=50 and int(crime)<100):
    totalValue=totalValue
elif(int(crime)>=100 and int(crime)<200):
    totalValue=totalValue+(totalValue*0.015)
elif(int(crime)>=200):
    totalValue=totalValue+(totalValue*0.03)
#End Adjust Prediction Based on Crime



#Start Adjust Prediction Based on Education
education=get_school_info(zipcode)
if(education==1):
    totalValue=totalValue-(totalValue*0.12)
elif(education==2):
    totalValue=totalValue-(totalValue*0.07)
elif(education==4):
    totalValue=totalValue+(totalValue*0.07)
elif(education==5):
    totalValue=totalValue+(totalValue*0.11) 
else:
    totalValue=totalValue
#End Adjust Prediction Based on Education



#START COMPARATOR
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

working_directory=os.path.abspath(os.path.dirname(__file__))
dict_path=Path(working_directory)
dict_path=dict_path / "dict.json"
with open(dict_path) as json_file:
    api_results = json.load(json_file)


common_year = dict()
input_year_built = input_results['Results'][0]['year_built']
for i in range (1,192):
    if (input_year_built-3) <= api_results[str(i)]['year_built'] and (input_year_built+3) >= api_results[str(i)]['year_built']:
        common_year[str(i)] = api_results[str(i)]['year_built']
common_prop_type = dict()                       #THIS WILL ALMOST NEVER MATCH BECAUSE OF THE DIFFERENT OUTPUT OPTIONS
for i in range (1,192):
    if input_results['Results'][0]['prop_type'] == api_results[str(i)]['prop_type']:
        common_prop_type[str(i)] = api_results[str(i)]['prop_type']
common_prop_sqft = dict()
input_prop_sqft = input_results['Results'][0]['prop_sqft']
for i in range (1,192):
    if  (input_prop_sqft-175) <= api_results[str(i)]['prop_sqft'] and (input_prop_sqft+175) >= api_results[str(i)]['prop_sqft']:
        common_prop_sqft[str(i)] = api_results[str(i)]['prop_sqft']
common_bedrooms = dict()
for i in range (1,192):
    if input_results['Results'][0]['bedrooms'] == api_results[str(i)]['bedrooms']:
        common_bedrooms[str(i)] = api_results[str(i)]['bedrooms']
common_full_bathrooms = dict()
for i in range (1,192):
    if input_results['Results'][0]['full_bathrooms'] == api_results[str(i)]['full_bathrooms']:
        common_full_bathrooms[str(i)] = api_results[str(i)]['full_bathrooms']
common_half_bathrooms = dict()
for i in range (1,192):
    if input_results['Results'][0]['half_bathrooms'] == api_results[str(i)]['half_bathrooms']:
        common_half_bathrooms[str(i)] = api_results[str(i)]['half_bathrooms']
common_roof_type = dict()                    #THIS WILL ALMOST NEVER MATCH BECAUSE OF THE DIFFERENT OUTPUT OPTIONS
for i in range (1,192):
    if input_results['Results'][0]['roof_type'] == api_results[str(i)]['roof_type']:
        common_roof_type[str(i)] = api_results[str(i)]['roof_type']
common_pool = dict()
for i in range (1,192):
    if input_results['Results'][0]['pool'] == api_results[str(i)]['pool']:
        common_pool[str(i)] = api_results[str(i)]['pool']
common_AC_type = dict()
for i in range (1,192):
    if input_results['Results'][0]['AC_type'] == api_results[str(i)]['AC_type']:
        common_AC_type[str(i)] = api_results[str(i)]['AC_type']
common_heat_type = dict()
for i in range (1,192):
    if input_results['Results'][0]['heat_type'] == api_results[str(i)]['heat_type']:
        common_heat_type[str(i)] = api_results[str(i)]['heat_type']
common_basement = dict()
for i in range (1,192):
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
    for b in range (0, 191):
        if (str(best_comp_list[0][a]) in api_results):
            best_comps_info[a] = api_results[str(best_comp_list[0][a])]
            


average_low = dict()
average_mean = dict()
average_high = dict()
single_low = dict()
single_mean = dict()
single_high = dict()

cannot_be_low = 1000000000000000000     #NO HOUSE HAS EVER SOLD FOR THIS AND AT THIS POINT, SOME BRUTE FORCING WAS DONE
cannot_be_high = 0                      #SEE ABOVE COMMENT


for a in range (0, len(best_comps_info)):
    if (best_comps_info[a]['eppraisal']!=None and best_comps_info[a]['zestimate']!=None):
        average_low[a] = (best_comps_info[a]['eppraisal']['low'] + best_comps_info[a]['zestimate']['low'])/2
        average_mean[a] = (best_comps_info[a]['eppraisal']['mean'] + best_comps_info[a]['zestimate']['mean'])/2
        average_high[a] = (best_comps_info[a]['eppraisal']['high'] + best_comps_info[a]['zestimate']['high'])/2
        average_low_sorted = sorted(average_low.values())
        average_high_sorted = sorted(average_high.values())
        low_average_low = average_low_sorted[0]
        high_average_high = average_high_sorted[len(average_high)-1]
        
        if (totalValue > high_average_high):
            totalValue = high_average_high
        elif (totalValue <= low_average_low):
            totalValue = low_average_low
        
    elif (best_comps_info[a]['eppraisal']!=None and best_comps_info[a]['zestimate'] == None):
        single_low[a] = best_comps_info[a]['eppraisal']['low']
        single_mean[a] = best_comps_info[a]['eppraisal']['mean']
        single_high[a] = best_comps_info[a]['eppraisal']['mean']
        single_low_sorted = sorted(single_low.values())
        single_high_sorted = sorted(single_high.values())
        low_single_low = single_low_sorted[0]
        high_single_high = single_high_sorted[len(single_high)-1]
        
        if (totalValue > high_single_high):
            totalValue = high_single_high
        elif (totalValue <= low_single_low):
            totalValue = low_single_low      
        
    elif (best_comps_info[a]['zestimate']!=None and best_comps_info[a]['eppraisal'] == None):
        single_low[a] = best_comps_info[a]['zestimate']['low']
        single_mean[a] = best_comps_info[a]['zestimate']['mean']
        single_high[a] = best_comps_info[a]['zestimate']['high']
        single_low_sorted = sorted(single_low.values())
        single_high_sorted = sorted(single_high.values())
        low_single_low = single_low_sorted[0]
        high_single_high = single_high_sorted[len(single_high)-1]

        if (totalValue > high_single_high):
            totalValue = high_single_high
        elif (totalValue <= low_single_low):
            totalValue = low_single_low
    else:
        continue       
#End of Comparator



#Start of Error Function
eppraisal_len = 0
for a in range (0, len(best_comps_info)):
    try:
        best_comps_info[a]['eppraisal']
        eppraisal_len = eppraisal_len +1
    except:
        eppraisal_len = eppraisal_len
average_mean_eppraisal = 0        
for a in range (0, eppraisal_len):
    average_mean_eppraisal = average_mean_eppraisal + best_comps_info[a]['eppraisal']['mean']
if eppraisal_len!=0:
    average_mean_eppraisal = average_mean_eppraisal/eppraisal_len
else:
    average_mean_eppraisal = None

zestimate_len = 0
for a in range (0, len(best_comps_info)):
    try:
        best_comps_info[a]['zestimate']
        zestimate_len = zestimate_len +1
    except:
        zestimate_len = zestimate_len
average_mean_zestimate = 0        
for a in range (0, zestimate_len):
    average_mean_zestimate = average_mean_zestimate + best_comps_info[a]['zestimate']['mean']
if zestimate_len!=0:
    average_mean_zestimate = average_mean_zestimate/zestimate_len
else:
    average_mean_zestimate = None

if average_mean_eppraisal != None:
    percent_diff_mean_eppraisal = (totalValue - average_mean_eppraisal)/average_mean_eppraisal *100
if average_mean_zestimate != None:
    percent_diff_mean_zestimate = (totalValue - average_mean_zestimate)/average_mean_zestimate *100
#End of Error Function    
    
    
formatted_value = "{:.2f}".format(totalValue)
print ("Thank you for filling in the details! The estimated total Value of the property: $", formatted_value)
if average_mean_zestimate != None:
    print ("Percent Error from Zillow's Mean Estimate: %", abs(round(percent_diff_mean_zestimate, 4)))
else:
    print("Percent Error from Zillow could not be found, as a suitable comparison to this house could not be found.")
if average_mean_eppraisal != None:
    print ("Percent Error from Eppraisal's Mean Estimate: %", abs(round(percent_diff_mean_eppraisal, 4)))
else:
    print("Percent Error from Eppraisal could not be found, as a suitable comparison to this house could not be found.")
