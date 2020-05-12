## Property Value Estimator 
## Takes in user int(input regarding all property details individually to compute the property estimate
## Square foot value is determined by the type of room (bedroom, kitchen, bathroom, etc and then the additional sq footage of the house is estimated as the basic sq ft value dependent on condition)
#
totalValue = 0
#
print("Welcome to the Property Value Estimator.....Please answer some questions!\n\n")
print("You will be asked about the condition of various aspects of your home. Here is some information to help you.\nPoor is 15% of homes, average is 50% of homes, good is 20% of homes, and excellent is 15% of homes. Typically excellent is reserved for new construction or very recently remodeled homes.\n\n")
print("Please enter your answers exactly how they are represented in the question.\n\n")
address = input("Enter the property's address (street address town, state zipcode): ") #VALUE STILL NEEDED
zipcode = int(input("Please confirm the property's zipcode: "))

while True:
    try:
        prop_type = int(input("Choose the property type:\n(0) Single Family Home\n(1) Duplex\n(2) Triplex\n(3) Manufactured\n(4) Townhouse\n(5) Condo\n(6) Mobile Home\n(7) Apartment\n\n"))
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
        elif (year_built < 1975):
            year_built_value = (1975-year_built)*-500
            totalValue = totalValue + year_built_value
            break
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
    prop_value = switch_property_value(prop_condition)
    return prop_val
#print (switch_property_value(prop_condition))
#END PROPERTY CONDITION
    



#PROPERTY SQUARE FOOTAGE
prop_sqft = int(input("Note: the basement is not counted in a property's square footage.\nEnter the property square footage: "))
while True:
    try:
        prop_condition = int(input("Choose the current property condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
        if prop_condition in range(4):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
#print (switch_property_value(prop_condition))
#END PROPERTY SQUARE FOOTAGE



#LOT SQUARE FOOTAGE
lot_sqft = int(input("Enter the lot square footage: "))
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
bedrooms = int(input("Enter total number of bedrooms: "))
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
       bedroom_x_sqft = int(input("Enter bedroom " + str(x) +" sqft: "))
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




#HALF BATHROOMS
half_bathrooms = int(input("Enter total number of half bathrooms: "))
for x in range(1, half_bathrooms+1):
    if(half_bathrooms == 0):
        break
    else:
        print ("Half Bathroom", x, ":")
        hbath_x_sqft = int(input("Enter half bathroom " + str(x) +" sqft: "))
        hbath_total_sqft = 0
        hbath_total_sqft = hbath_total_sqft + hbath_x_sqft
        hbath_total_value = 0
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
            hbath_x_ctop_sqft = int(input("Enter the counter's square footage: ")) #DIDN'T ASK THIS QUESTION
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




#FULL BATHROOMS
full_bathrooms = int(input("Enter total number of full bathrooms: "))
for x in range(1, full_bathrooms+1):
    if(full_bathrooms == 0):
        break
    else:
        print ("Full Bathroom", x, ":")
        fbath_x_sqft = int(input("Enter full bathroom " + str(x) +" sqft: "))
        fbath_total_sqft = 0
        fbath_total_sqft = fbath_total_sqft + fbath_x_sqft
        fbath_total_value = 0
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
            fbath_x_ctop_sqft = int(input("Enter the counter's square footage: ")) #NOT ASKING THIS QUESTION
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




#KITCHEN
kitchen_sqft = int(input("Enter the square footage of the kitchen: "))
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
    kitchen_ctop_sqft = int(input("Enter the counter's square footage: "))
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
prop_sqft_final = prop_value*prop_sqft_remaining        #FINAL SQ FT
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

basement = input("Is there a basement (yes or no): ")
if(basement == "yes"):
    basement_sqft = int(input("Enter the square footage of the basement: "))
    basement_finished = input("Is the basement fully or partially finished (yes or no): ")
    if(basement_finished == "yes"):
        basement_finished_sqft = int(input("Enter the square footage of the finished basement: "))
        while True:
            try:
                basement_condition = int(input("Choose the current basement condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
                if basement_condition in range(4):
                    break
            except: 
                pass
            print ('\nIncorrect input, try again!')
        basement_value = basement_value + switch_basement_finished_value(basement_condition)
        basement_unfinished_sqft = basement_sqft - basement_finished_sqft
        basement_value = basement_value + switch_basement_unfinished_value(basement_condition)
basement_door = input("Is it a walk out basement (yes or no): ")
if(basement_door == "yes"):
    basement_value = basement_value*1.2
totalValue = totalValue + basement_value
#END BASEMENT



#ROOF
roof_sum = 0
roof_age = int(input("How old is the roof (enter a number rounded to nearest year): "))
while True:
    try:
        roof_type = int(input("Choose the roof type\n(0) Slate Tile\n(1) Clay Tile\n(2) Copper\n(3) Other Metals\n(4) Wood Shingle\n(5) Fiber Cement Shingles\n(6) Asphalt Shingles\n(7) Other\n\n"))
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
#print(totalValue)
#END ROOF



#APPLIANCES
kitchen_appliances_value = 0
washer_dryer_value = 0   
washer = input("Does property come with a washer? (yes or no): ")
if (washer == "yes"):
    washer_dryer_value = 250
dryer = input("Does property come with a dryer? (yes or no): ")
if (dryer == "yes"):
    washer_dryer_value = washer_dryer_value + 185
dishwasher = input("Does property come with a dishwasher? (yes or no): ")
if (dishwasher == "yes"):
    kitchen_appliances_value = 175
fridge = input("Does property come with a fridge? (yes or no): ")
if (fridge == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 350
microwave = input("Does property come with a microwave? (yes or no): ")
if (microwave == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 20   
stove = input("Does property come with a ? (yes or no): ")
if (stove == "yes"):
    kitchen_appliances_value = kitchen_appliances_value + 250
kitchen_match = input("Do all of the kitchen appliances match in color? (yes or no): ")
if (kitchen_match == "yes"):
    kitchen_appliances_value = kitchen_appliances_value * 1.2
washer_dryer_match = input("Do the washer and dryer match in color? (yes or no): ")
if (washer_dryer_match == "yes"):
    washer_dryer_value = washer_dryer_value * 1.2
#END APPLIANCES


#IT WOULD MAKE SOME SENSE TO ASK HERE IF THE PLACE COMES WITH ANY MAJOR FURNITURE


#POOL
pool = input("Is there a pool installed? (yes or no): ")
if(pool == "yes"):
   pool_install = input("Enter if the pool is 'in-ground' or 'above-ground': ")
   pool_sqft = int(input("Enter the square footage of the pool: "))
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
hot_tub = input("Is there a hot tub installed? (yes or no): ")
if(hot_tub == "yes"):
    while True:
        try:
            hot_tub_material = int(input("Choose the hot tub interior type\n(0) Inflatable\n(1) Custom Portable\n(2) Custom in-ground\n(3) Other\n\n"))
            if hot_tub_material in range(4):
                break
        except:
            pass
        print('\nIncorrect input, try again!')
    hot_tub_size = int(input("Enter how many people the hot tub is meant for: "))
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
#print(totalValue)
#END HOT TUB


#DRIVEWAY
driveway = input("Is there a driveway? (yes or no): ")
if(driveway == "yes"):
    driveway_sqft = int(input("Enter the driveway square footage: "))
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
            0: 5,
            1: 2,
            2: 1,
            3: 3,
        }.get(driveway_material, "Invalid, will not be considered")
        return drive_mat_switcher
    driveway_value = driveway_sqft * switch_driveway_material(driveway_material)
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
                0: 0.8,
                1: 1,
                2: 1.1,
                3: 1.2
                }.get(driveway_condition, "Invalid, will not be considered")
        return driveway_val_switch
    driveway_value = driveway_value * switch_driveway_value(driveway_condition)
    totalValue = totalValue + driveway_value
#print(totalValue)
#END OF DRIVEWAY

   
#GARAGE
garage = input("Is there a garage installed? (yes or no): ")
if(garage == "yes"):
    garage_install = input("Enter if garage is 'attached' or 'detached': ") #This actually doesn't matter much as the pros and cons tend to equal out and become dependent on the person
    garage_sqft = int(input("Enter the square footage of the garage: "))
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
            0: 0.8,
            1: 1,
            2: 1.1,
            3: 1.2
        }.get(garage_condition, "Invalid, will not be considered")
        return garage_value_switch
    totalValue = totalValue + garage_value * switch_garage_value(garage_condition) 
#print(totalValue)  
#END GARAGE



#AC TYPE        
AC_type = int(input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n"))         
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
#print totalValue
#END AC TYPE


#HEAT TYPE
heat_type = int(input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Standard Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n"))
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
#print totalValue 
#END HEAT TYPE   
   
 
#FIREPLACES  
fireplaces = int(input("Enter the number of fireplaces if installed and 0 if not: \n"))
totalValue = totalValue+(fireplaces*800)
#END FIREPLACES


#ELECTRIC SYSTEM
electric_system = input("Please enter if the electric system is 'fuse box' or a 'circuit breaker'\n")
if (electric_system == "fuse box"):
   totalValue = totalValue-500
#END ELECTRIC SYSTEM


#view_type = int(input("Choose all view types (enter as many letters as applicable):\n(0) River\n(1) Lake\n(2) Ocean\n(3) Golf Course\n(4) Mountain\n(5) Skyline\n(6) Standard\n\n") #VALUE STILL NEEDED
#In Bear, DE there isn't a very large difference in the type of view each house has. There's no ocean, lake, mountain, large hill, river, skyline in the area.

#WATER TYPE
water_type = heat_type = input("Please enter if the water/sewage system is 'town' or a 'septic+well'\n")
if(water_type == "septic+well"):
   totalValue = totalValue-1000
#END WATER TYPE

#FOUNDATION MATERIAL
while True:
    try:
        foundation_material = int(input("Choose the foundation material\n(0) Stone\n(1) Brick\n(2) Preservative treated lumber\n(3) Concrete Block\n(4) Poured Concrete\n(5) Other\n\n"))
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
#print(totalValue)
#END FOUNDATION MATERIAL


#PORCH
porch = input("Is there a porch (yes or no)?: ")
if(porch == "yes"):
    porch_num = int(input("Enter the number of porches: "))
    for x in range (1, porch_num+1):
        print ("Porch", x, ":")
        porch_x_sqft = int(input("Enter porch " + str(x) +" sqft: "))
        porch_x_material = int(input("Choose the porch material\n(0) Wood\n(1) Concrete\n(2) Plastic Wood Composites\n(3) Other\n\n"))
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
patio = input("Is there a patio (yes or no)?: ")
if(patio == "yes"):
    patio_num = int(input("Enter the number of patios: "))
    for x in range (1, patio_num+1):
        print ("Patio", x, ":")
        patio_x_sqft = int(input("Enter patio " + str(x) +" sqft: "))
        patio_x_material = int(input("Choose the patio material\n(0) Brick\n(1) Stone\n(2) Patio Pavers\n(3) Concrete\n(4) Gravel\n(5) Other\n\n"))
        patio_total_value = 0
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
        totalValue = totalValue + patio_total_value
        if(patio_x_material == 5):
            patio_other = input("Enter the patio material that the property contains: ")
#END PATIO


#FENCED IN YARD
yard = input("Is there a yard fenced in (yes or no)?: ")
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
#print(totalValue)
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
    totalValue = totalValue * switch_prop_type(prop_type)
    return switcher_prop
#END ADJUST PREDICTION  BASED ON PROPERTY TYPE


    
    
    
    
#AT THE END I THINK WE SHOULD PULL THE BEST AND CLOSEST COMPS AND THEN DO SOME FORM OF A COMPARATOR TO ADJUST OUR ESTIMATE BEFORE IT OUTPUTS.

print (totalValue)
