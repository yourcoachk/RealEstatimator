# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:16:57 2020

@author: Kolby Kuratnick
"""

#Property Value Estimator 
#Takes in user input regarding all property details individually to compute the property estimate
#Square foot value is determined by the type of room (bedroom, kitchen, bathroom, etc and then the additional sq footage of the house is estimated as the basic sq ft value dependent on condition)

totalValue = 0

print("Welcome to the Property Value Estimator.....Please answer some questions!")
print("You will be asked about the condition of various aspects of your home. Here is some information to help you. \n Poor is 15% of homes, average is 50% of homes, good is 20% of homes, and excellent is 15% of homes. Typically excellent is reserved for new construction or very recently remodeled homes.")
print("Please enter your answers exactly how they are represented in the question.")
address = input("Enter the property's address (street address town, state zipcode): ") #VALUE STILL NEEDED
zipcode = input("Please confirm the property's zipcode: ")
while True:
    try:
        prop_type = input("Choose the property type:\n(0) Single Family Home\n(1) Duplex\n(2) Triplex\n(3) Manafactured\n(4) Townhouse\n(5) Condo\n(6) Mobile Home\n(7) Apartment\n\n") #VALUE STILL NEEDED
        if prop_type in range(8):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')



#WHAT'S THE DIFFERENCE BETWEEN INPUT AND input?


year_built = input("Enter the year the property was built: ")
if (year_built > 2000):
    year_built_value = (year_built-2000)*500
elif (year_built < 1975):
    year_built_value = (1975-year_built)*-500
    totalValue = totalValue + year_built_value
else:
    totalValue = totalValue



prop_sqft = input("Note: the basement is not counted in a property's square footage./nEnter the property square footage: ")
while True:
    try:
        prop_condition = input("Choose the current property condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
        if prop_type in range(3):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
    def switch_property_value(prop_condition):
        switcher_property = {
                0: prop_value == 100,
                1: prop_value == 125,
                2: prop_value == 150,
                3: prop_value == 165,
        }
        #print switcher_property.get(prop_condition, "Invalid, will not be considered")



lot_sqft = input("Enter the lot square footage: ")
while True:
    try:
        lot_condition = input("Choose the current lot condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
        if lot_condition in range(3):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
lot_sqft = lot_sqft - prop_sqft
totalValue = totalValue+(lot_sqft*3.55)



bedrooms = input("Enter total number of bedrooms: ")
for x in range(1, bedrooms+1):
    if(bedrooms == 0):
        break
    else:
        print ("Bedroom", x, ":")
        bedroom_x_sqft = input("Enter bedroom " + str(x) +" sqft: ")
        bedroom_total_sqft = bedroom_total_sqft+bedroom_x_sqft
        while True:
            try:
                bedroom_x_condition = input("Bedroom" + str(x) + " Choose the bedroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
                if bedroom_x_condition in range(4):                    #IN THE SECTION ABOVE THIS IS IN RANGE(3), WHICH IS IT?
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        def switch_bedroom_value(bedroom_x_condition):
            switcher_bedroom = {
                0: bedroom_x_value == bedroom_x_sqft*60,
                1: bedroom_x_value == bedroom_x_sqft*80,
                2: bedroom_x_value == bedroom_x_sqft*90,
                3: bedroom_x_value == bedroom_x_sqft*100,
            }
            bedroom_final_value = bedroom_final_value+bedroom_x_value
            #print switcher_bedroom.get(bedroom_x_condition, "Invalid, will not be considered")
totalValue = totalValue+bedroom_final_value

prop_sqft_remaining = prop_sqft - bedroom_total_sqft



half_bathrooms = input("Enter total number of half bathrooms: ") #VALUE STILL NEEDED
for x in range(1, half_bathrooms+1):
    if(half_bathrooms == 0):
        break
    else:
        print ("Half Bathroom", x, ":")
        hbath_x_sqft = input("Enter half bathroom " + str(x) +" sqft: ")
        hbath_total_sqft = hbath_total_sqft + hbath_x_sqft
        while True:
            try:
                hbath_x_condition = input("Half Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0)Poor\n(1)Average\n(2)Good\n(3)Excellent\n\n")
                if hbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                hbath_x_floor_material=input("Choose the half bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n")
                if hbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                hbath_x_ctop_material=input("Choose the half bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
                if hbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - hbath_total_sqft




full_bathrooms = input("Enter total number of full bathrooms: ") #VALUE STILL NEEDED
for x in range(1, full_bathrooms+1):
    if(full_bathrooms == 0):
        break
    else:
        print ("Full Bathroom", x, ":")
        fbath_x_sqft = input("Enter full bathroom " + str(x) +" sqft: ")
        fbath_total_sqft = fbath_total_sqft + fbath_x_sqft
        while True:
            try:
                fbath_x_condition = input("Full Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
                if fbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                fbath_x_floor_material=input("Choose the full bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n")
                if fbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                fbath_x_ctop_material=input("Choose the full bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
                if fbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - fbath_total_sqft



kitchen = input("Enter the square footage of the kitchen: ") #VALUE STILL NEEDED
while True:
    try:
        kitchen_floor_material=input("Choose the kitchen floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n(5) Wood/Butcher Block\n\n")
        if kitchen_floor_material in range(6):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
while True:
    try:
        kitchen_ctop_material=input("Choose the kitchen countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
        if kitchen_ctop_material in range(6):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - kitchen 





prop_sqft_final = prop_value*prop_sqft_remaining        #FINAL SQ FT






#basement = input("Is there a basement (yes or no): ")
#if(basement == "yes"):
#    basement_sqft = input("Enter the square footage of the basement: ")
#    basement_door = input("Is it a walk out basement (yes or no): ")
#    while True:
#     try:
#        basement_condition = input("Choose the current basement condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
#        if basement_condition in range(3):
#            break
#        except: #IT DOESN'T LIKE THIS EXCEPT FOR SOME REASON "INVALID SYTAX"
#            pass
#        basement_finished = input("Is the basement fully or partially finished (yes or no): ")
#        if(basement_finished == "yes"):
#            basement_finished_sqft = input("Enter the square footage of the finished basement: ")
#            def switch_basement_finished_value(basement_condition):
#                switcher_basement_finished = {
#                        0: basement_finished_value == basement_finished_sqft*30,
#                        1: basement_finished_value == basement_finished_sqft*45,
#                        2: basement_finished_value == basement_finished_sqft*60,
#                        3: basement_finished_value == basement_finished_sqft*75,
#                        }
#                #print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
#        basement_unfinished_sqft = basement_sqft-basement_finished_sqft
#        def switch_basement_unfinished_value(basement_condition):
#            switcher_basement_unfinished = {
#                0: basement_unfinished_value == basement_unfinished_sqft*10,
#                1: basement_unfinished_value == basement_unfinished_sqft*15,
#                2: basement_unfinished_value == basement_unfinished_sqft*20,
#                3: basement_unfinished_value == basement_unfinished_sqft*25,
#            }
#            #print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
#        basement_value = basement_unfinished_value+basement_finished_value
#        if (basement_door == yes):
#            basement_value = basement_value*1.2
#        else:
#                def switch_basement_finished_value(basement_condition):
#                    switcher_basement_finished = {
#                            0: basement_value == basement_sqft*10,
#                            1: basement_value == basement_sqft*15,
#                            2: basement_value == basement_sqft*20,
#                            3: basement_value == basement_sqft*25,
#                            }
#                    #print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
#        if (basement_door == yes):
#            basement_value = basement_value*1.2
#        else:
#            basement_value = basement_value

         
AC_type = input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n")         
if(AC_type == "5"):
    AC_other = input("Enter the AC type that the property contains: ")
def switch_AC(AC_type):
    switcher_AC = {
        0: totalValue == totalValue-500,
        1: totalValue == totalValue-400,
        2: totalValue == totalValue-0,
        3: totalValue == totalValue-0,
        4: totalValue == totalValue+500,
        5: totalValue == totalValue+0,
    }
#print switcher_AC.get(AC_type, "Invalid, will not be considered")



roof_age = input("How old is the roof (enter a number): ")
roof_type = input("Choose the roof type\n(0) Slate Tile\n(1) Clay Tile\n(2) Copper\n(3) Other Metals\n(4) Wood Shingle\n(5) Fiber Cement Shingles\n(6) Asphalt Shingles\n(7) Other\n\n")
if(roof_type == "7"):
    roof_other = input("Enter the roof type that the property contains: ")
if (roof_type == "0" or roof_type == "1" or roof_type == "2"):
    roof_sum = 80 - roof_age
elif (roof_type == "3"):
    roof_sum = 60 - roof_age
elif (roof_type == "4"):
    roof_sum = 30 - roof_age
elif (roof_type == "5"):
    roof_sum = 25 - roof_age
elif (roof_type == "6"):
    roof_sum = 20 - roof_age
elif (roof_type == "7"):
    roof_sum = 20 - roof_age
else:
    print ("Invalid, will not be considered")

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


appliances = input("Choose appliances sold with house (enter all that apply):\n(0) Washer\n(1) Dryer\n(2) Dishwasher\n(3) Fridge\n(4) Microwave\n(5) Stove\n\n") #HOW WILL WE ANALYZE IF MULTIPLE ARE ENTERED?
kitchen_appliances = input("Are all kitchen appliances color coordinated (yes or no)?: ")
wash_dry = input("Are the washer and dryer appliances color coordinated (yes or no)?: ")



#IT WOULD MAKE SOME SENSE TO ASK HERE IF THE PLACE COMES WITH ANY MAJOR FURNITURE



pool = input("Is there a pool installed? (yes or no): ")
if(pool == "yes"):
    pool_install = input("Enter if the pool is 'in-ground' or 'above-ground': ")
    pool_sqft = input("Enter the square footage of the pool: ")
    if (pool_sqft >= .6*lot_sqft):
        totalValue = totalValue - 1000
    else:
        if (pool_install == "above-ground"):
            totalValue = totalValue - 500
        elif (pool_install == "in-ground"):
            totalValue = totalValue + 500
        else:
            print ("Invalid, will not be considered")



hot_tub = input("Is there a pool installed? (yes or no): ")
if(hot_tub == "yes"):
    hot_tub_material = input("Choose the hot tub interior type\n(0) Inflatable\n(1) Custom Portable\n(2) Custom in-ground\n(3) Other\n\n")
    hot_tub_size = input("Enter how many people the hot tub is meant for: ")
    hot_tub_init_value = hot_tub_size*150
    def switch_hot_tub(hot_tub_material):
        switcher_hot_tub = {
            0: totalValue == totalValue + hot_tub_init_value - 500,
            1: totalValue == totalValue + hot_tub_init_value + 200,
            2: totalValue == totalValue + hot_tub_init_value + 500,
            3: totalValue == totalValue + hot_tub_init_value,
        }
        #print switcher_hot_tub.get(hot_tub_material, "Invalid, will not be considered")    





driveway = input("Is there a driveway?: ")
if(driveway == "yes"):
    driveway_sqft = input("Enter the driveway square footage: ")
    driveway_material = input("Choose the driveway material\n(0) Concrete\n(1) Brick\n(2) Rock\n(3) Asphalt\n\n")
    if (driveway_material == 0):
        driveway_value = 5*driveway_sqft
    elif (driveway_material == 1):
        driveway_value = 2*driveway_sqft
    elif (driveway_material == 2):
        driveway_value = driveway_sqft
    elif (driveway_material == 3):
        driveway_value = 3*driveway_sqft
    driveway_condition = input("Choose the current driveway condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
    def switch_driveway_value(driveway_condition):
        switcher_driveway = {
            0: driveway_value == driveway_value*.8,
            1: driveway_value == driveway_value,
            2: driveway_value == driveway_value*1.1,
            3: driveway_value == driveway_value*1.2,
        }
        #print switcher_driveway.get(driveway_condition, "Invalid, will not be considered")
totalValue = totalValue + driveway_value
    

garage = input("Is there a garage installed? (yes or no): ")
if(garage == "yes"):
    garage_install = input("Enter if garage is 'attached' or 'detached': ") #This actually doesn't matter much as the pros and cons tend to equal out and become dependent on the person
    garage_sqft = input("Enter the square footage of the garage: ")
    garage_condition = input("Choose the current garage condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
    garage_value = garage_sqft*10                #average 400 sq ft garage valued at $16k
    def switch_garage_value(garage_condition):
        switcher_garage = {
            0: garage_value == garage_value*.8,
            0: garage_value == garage_value,
            0: garage_value == garage_value*1.1,
            0: garage_value == garage_value*1.2,
        }
        #print switcher_garage.get(garage_condition, "Invalid, will not be condsidered")
totalValue = totalValue + garage_value    




AC_type = input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n")
if(AC_type == "5"):
    AC_other = input("Enter the AC type that the property contains: ")
def switch_AC(AC_type):
    switcher_AC = {
        0: totalValue == totalValue-500,
        1: totalValue == totalValue-400,
        2: totalValue == totalValue-0,
        3: totalValue == totalValue-0,
        4: totalValue == totalValue+500,
        5: totalValue == totalValue+0,
    }
    #print switcher_AC.get(AC_type, "Invalid, will not be considered")




heat_type = input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Standard Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n")
if(heat_type == "5"):
    heat_other = input("Enter the heat type that the property contains: ")
def switch_Heat(heat_type):
    switcher_heat = {
        0: totalValue == totalValue-500,
        1: totalValue == totalValue-350,
        2: totalValue == totalValue-0,
        3: totalValue == totalValue-0,
        4: totalValue == totalValue+500,
        5: totalValue == totalValue+0,
    }
    #print switcher_heat.get(heat_type, "Invalid, will not be considered")    
    
    
    
fireplaces = input("Enter the number of fireplaces if installed and 0 if not: ")
totalValue = totalValue+(fireplaces*800)



electric_system = input("Please enter if the electric system is 'fuse box' or a 'circuit breaker'")
if electric_system == str("fuse box"):
    totalValue = totalValue-500



#view_type = input("Choose all view types (enter as many letters as applicable):\n(0) River\n(1) Lake\n(2) Ocean\n(3) Golf Course\n(4) Mountain\n(5) Skyline\n(6) Standard\n\n") #VALUE STILL NEEDED
#In Bear, DE there isn't a very large difference in the type of view each house has. There's no ocean, lake, mountain, large hill, river, skyline in the area.


water_type = heat_type = input("Please enter if the water/sewage system is 'town' or a 'septic+well'")
if water_type == str(septic+well):
    totalValue = totalValue-1000



foundation_material = input("Choose the foundation material\n(0) Stone\n(1) Brick\n(2) Preservative treated lumber\n(3) Concrete Block\n(4) Poured Concrete\n(5) Other\n\n")
if(foundation_material == "5"):
    foundation_other = input("Enter the foundation material that the property contains: ")
def switch_foundation_material(foundation_material):
    switcher_foundation = {
        0: totalValue == totalValue-10000,
        1: totalValue == totalValue-3000,
        2: totalValue == totalValue-8000,
        3: totalValue == totalValue-500,
        4: totalValue == totalValue+0,
        5: totalValue == totalValue+0,
    }
    #print switcher_foundation.get(foundation_material, "Invalid, will not be considered")




porch = input("Is there a porch (yes or no)?: ") #VALUE STILL NEEDED
if(porch == "yes"):
    porch_num = input("Enter the number of porches: ")
    for x in range (1, porch_num+1):
        print ("Porch", x, ":")
        porch_x_sqft = input("Enter porch " + str(x) +" sqft: ")
        porch_total_sqft = porch_total_sqft + porch_x_sqft
        porch_x_material = input("Choose the porch material\n(0) Wood\n(1) Vinyl\n(2) Plastic Wood Composites\n(3) Other\n\n")
        if(porch_x_material == "3"):
            porch_other = input("Enter the porch material that the property contains: ")




patio = input("Is there a patio (yes or no)?: ") #VALUE STILL NEEDED
if(patio == "yes"):
    patio_num = input("Enter the number of patios: ")
    for x in range (1, patio_num+1):
        print ("Patio", x, ":")
        patio_x_sqft = input("Enter patio " + str(x) +" sqft: ")
        patio_total_sqft = patio_total_sqft + patio_x_sqft
        patio_x_material = input("Choose the patio material\n(0) Brick\n(1) Stone\n(2) Patio Pavers\n(3) Concrete\n(4) Gravel\n(5) Other\n\n")
        if(patio_x_material == "5"):
            patio_other = input("Enter the patio material that the property contains: ")




yard = input("Is there a yard fenced in (yes or no)?: ")
if(yard == "yes"):
    yard_material = input("Choose the fence material\n(0) Chain Link\n(1) Picket Fence\n(2) Synthetic\n(3) Aluminum\n(4) Privacy Vinyl\n(5) Composite\n(6) Privacy Wood\n(7) Other\n\n")
    if(yard_material == "7"):
        yard_other = input("Enter the fence material that the property contains: ")
def switch_yard_material(yard_material):
    switcher_yard_mat = {
        0: totalValue == totalValue+200,
        1: totalValue == totalValue+500,
        2: totalValue == totalValue+500,
        3: totalValue == totalValue+300,
        4: totalValue == totalValue+800,
        5: totalValue == totalValue+400,
        6: totalValue == totalValue+700,
        7: totalValue == totalValue+300,
    }
    #print switcher_yard_mat.get(yard_material, "Invalid, will not be considered")    




additional_factors = input("Are there any additional factor(s) that should be considered (yes or no)?: ")
if(additional_factors == "yes"):
    add_fac_yes = input("Please list the additional factors: ")

#AT THE END I THINK WE SHOULD PULL THE BEST AND CLOSEST COMPS AND THEN DO SOME FORM OF A COMPARATOR TO ADJUST OUR ESTIMATE BEFORE IT OUTPUTS.

print (totalValue)
