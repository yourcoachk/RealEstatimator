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
        prop_type = int(input("Choose the property type:\n(0) Single Family Home\n(1) Duplex\n(2) Triplex\n(3) Manufactured\n(4) Townhouse\n(5) Condo\n(6) Mobile Home\n(7) Apartment\n\n")) #VALUE STILL NEEDED
        if prop_type in range(8):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')

while True:
    try:
        year_built = int(input("Enter the year the property was built: "))
        if (year_built >= 2000 and year_built <= 2020):
            year_built_value = (year_built-2000)*500
            totalValue = totalValue + year_built_value
            break
        elif (year_built < 1975):
            year_built_value = (1975-year_built)*-500
            totalValue = totalValue - year_built_value  #CHECK MATH
            break
    except:
        pass
    print('\nIncorrect input, try again!')


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
    prop_value = prop_val
    return prop_val
#print (switch_property_value(prop_condition))

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



half_bathrooms = int(input("Enter total number of half bathrooms: ")) #VALUE STILL NEEDED
for x in range(1, half_bathrooms+1):
    if(half_bathrooms == 0):
        break
    else:
        print ("Half Bathroom", x, ":")
        hbath_x_sqft = int(input("Enter half bathroom " + str(x) +" sqft: "))
        hbath_total_sqft = 0
        hbath_total_sqft = hbath_total_sqft + hbath_x_sqft
        while True:
            try:
                hbath_x_condition = int(input("Half Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0)Poor\n(1)Average\n(2)Good\n(3)Excellent\n\n"))
                if hbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                hbath_x_floor_material=int(input("Choose the half bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n"))
                if hbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                hbath_x_ctop_material=int(input("Choose the half bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
                if hbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - hbath_total_sqft




full_bathrooms = int(input("Enter total number of full bathrooms: ")) #VALUE STILL NEEDED
for x in range(1, full_bathrooms+1):
    if(full_bathrooms == 0):
        break
    else:
        print ("Full Bathroom", x, ":")
        fbath_x_sqft = int(input("Enter full bathroom " + str(x) +" sqft: "))
        fbath_total_sqft = 0
        fbath_total_sqft = fbath_total_sqft + fbath_x_sqft
        while True:
            try:
                fbath_x_condition = int(input("Full Bathroom " + str(x) + ": Choose the full bathroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
                if fbath_x_condition in range(4):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                fbath_x_floor_material=int(input("Choose the full bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n"))
                if fbath_x_floor_material in range(5):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')
        while True:
            try:
                fbath_x_ctop_material=int(input("Choose the full bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
                if fbath_x_ctop_material in range(6):
                    break
            except:
                pass
            print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - fbath_total_sqft




kitchen = int(input("Enter the square footage of the kitchen: ")) #VALUE STILL NEEDED
while True:
    try:
        kitchen_floor_material=int(input("Choose the kitchen floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n(5) Wood/Butcher Block\n\n"))
        if kitchen_floor_material in range(6):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')
while True:
    try:
        kitchen_ctop_material=int(input("Choose the kitchen countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n"))
        if kitchen_ctop_material in range(6):
            break
    except:
        pass
    print ('\nIncorrect input, try again!')

prop_sqft_remaining = prop_sqft_remaining - kitchen 





prop_sqft_final = prop_value*prop_sqft_remaining        #FINAL SQ FT





basement = input("Is there a basement (yes or no): ")
if(basement == "yes"):
    basement_sqft = int(input("Enter the square footage of the basement: "))
    basement_door = input("Is it a walk out basement (yes or no): ")
   
    while True:
        try:
            basement_condition = int(input("Choose the current basement condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n"))
            if basement_condition in range(4):
                break
        except: 
            pass
        print ('\nIncorrect input, try again!')

    basement_finished = input("Is the basement fully or partially finished (yes or no): ")
    if(basement_finished == "yes"):
        basement_finished_sqft = int(input("Enter the square footage of the finished basement: "))
        def switch_basement_finished_value(basement_condition):
            switcher_basement_finished_val={ 
                0: basement_finished_sqft*30,
                1: basement_finished_sqft*45,
                2: basement_finished_sqft*60,
                3: basement_finished_sqft*75
                }
            basement_finished_value = switcher_basement_finished_val
            return switcher_basement_finished_val
                
   
        basement_unfinished_sqft = basement_sqft-basement_finished_sqft
        def switch_basement_unfinished_value(basement_condition):
            switcher_basement_unfinished = {
                0: basement_unfinished_sqft*10,
                1: basement_unfinished_sqft*15,
                2: basement_unfinished_sqft*20,
                3: basement_unfinished_sqft*25,
            }
            basement_unfinished_value = switcher_basement_unfinished
            basement_value = basement_unfinished_value+basement_finished_value
        if (basement_door == "yes"):
            basement_value = basement_value*1.2
    else:
        def switch_basement_unfinished_value(basement_condition):
            switcher_basement_unfinished = {
                    0: basement_value == basement_sqft*10,
                    1: basement_value == basement_sqft*15,
                    2: basement_value == basement_sqft*20,
                    3: basement_value == basement_sqft*25,
                    }
        if (basement_door == "yes"):
            basement_value = basement_value*1.2
        else:
            basement_value = basement_value





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


# appliances = int(input("Choose appliances sold with house (enter all that apply):\n(0) Washer\n(1) Dryer\n(2) Dishwasher\n(3) Fridge\n(4) Microwave\n(5) Stove\n\n")) #HOW WILL WE ANALYZE IF MULTIPLE ARE ENTERED?)
# kitchen_appliances = input("Are all kitchen appliances color coordinated (yes or no)?: ")
# wash_dry = input("Are the washer and dryer appliances color coordinated (yes or no)?: ")



#IT WOULD MAKE SOME SENSE TO ASK HERE IF THE PLACE COMES WITH ANY MAJOR FURNITURE



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
            0: driveway_sqft*5,
            1: driveway_sqft*2,
            2: driveway_sqft,
            3: driveway_sqft*3
        }.get(driveway_material, "Invalid, will not be considered")
        return drive_mat_switcher
driveway_value = switch_driveway_material(driveway_material) #CURRENTLY SWITCH_DRIVEWAY_VALUE IS NOT DEFINED?
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
                0: driveway_value*.8,
                1: driveway_value,
                2: driveway_value*1.1,
                3: driveway_value*1.2
                }.get(driveway_condition, "Invalid, will not be considered")
        return driveway_val_switch
driveway_value = switch_driveway_value(driveway_condition)
totalValue = totalValue + driveway_value
print(totalValue)
   

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
            0: garage_value*.8,
            1: garage_value,
            2: garage_value*1.1,
            3: garage_value*1.2
        }.get(garage_condition, "Invalid, will not be considered")
        return garage_value_switch
totalValue = totalValue + garage_value  
#print(totalValue)  


        
AC_type = int(input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n"))         
if(AC_type == 5):
   AC_other = input("Enter the AC type that the property contains: ")
def switch_AC(AC_type):
   switcher_AC = {
       0: totalValue-500,
       1: totalValue-400,
       2: totalValue-0,
       3: totalValue-0,
       4: totalValue+500,
       5: totalValue+0
   }.get(AC_type,"Invalid, will not be considered")
   return switcher_AC
totalValue = switch_AC(AC_type)
#print totalValue


heat_type = int(input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Standard Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n"))
if(heat_type == 5):
   heat_other = input("Enter the heat type that the property contains: ")
def switch_Heat(heat_type):
    totalValue_switch = {
        0: totalValue-500,
        1: totalValue-350,
        2: totalValue-0,
        3: totalValue-0,
        4: totalValue+500,
        5: totalValue+0
    }.get(heat_type,"Invalid, will not be considered")
    return totalValue_switch 
totalValue = switch_Heat(heat_type)
#print totalValue 
   
   
   
fireplaces = int(input("Enter the number of fireplaces if installed and 0 if not: \n"))
totalValue = totalValue+(fireplaces*800)



electric_system = input("Please enter if the electric system is 'fuse box' or a 'circuit breaker'\n")
if (electric_system == "fuse box"):
   totalValue = totalValue-500



#view_type = int(input("Choose all view types (enter as many letters as applicable):\n(0) River\n(1) Lake\n(2) Ocean\n(3) Golf Course\n(4) Mountain\n(5) Skyline\n(6) Standard\n\n") #VALUE STILL NEEDED
#In Bear, DE there isn't a very large difference in the type of view each house has. There's no ocean, lake, mountain, large hill, river, skyline in the area.


water_type = heat_type = input("Please enter if the water/sewage system is 'town' or a 'septic+well'\n")
if(water_type == "septic+well"):
   totalValue = totalValue-1000



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
        0: totalValue-10000,
        1: totalValue-3000,
        2: totalValue-8000,
        3: totalValue-500,
        4: totalValue+0,
        5: totalValue+0
    }.get(foundation_material,"Invalid, will not be considered")
    return foundation_switcher
totalValue = switch_foundation_material(foundation_material)
#print(totalValue)




porch = input("Is there a porch (yes or no)?: ") #VALUE STILL NEEDED
if(porch == "yes"):
    porch_num = int(input("Enter the number of porches: "))
    for x in range (1, porch_num+1):
        print ("Porch", x, ":")
        porch_x_sqft = int(input("Enter porch " + str(x) +" sqft: "))
        porch_total_sqft = 0
        porch_total_sqft = porch_total_sqft + porch_x_sqft
        porch_x_material = int(input("Choose the porch material\n(0) Wood\n(1) Vinyl\n(2) Plastic Wood Composites\n(3) Other\n\n"))
        if(porch_x_material == "3"):
            porch_other = input("Enter the porch material that the property contains: ")




patio = input("Is there a patio (yes or no)?: ") #VALUE STILL NEEDED
if(patio == "yes"):
    patio_num = int(input("Enter the number of patios: "))
    for x in range (1, patio_num+1):
        print ("Patio", x, ":")
        patio_x_sqft = int(input("Enter patio " + str(x) +" sqft: "))
        patio_total_sqft = 0
        patio_total_sqft = patio_total_sqft + patio_x_sqft
        patio_x_material = int(input("Choose the patio material\n(0) Brick\n(1) Stone\n(2) Patio Pavers\n(3) Concrete\n(4) Gravel\n(5) Other\n\n"))
        if(patio_x_material == "5"):
            patio_other = input("Enter the patio material that the property contains: ")




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
if(yard_material == "7"):                               #CURRENTLY SAYS "YARD_MATERIAL" NOT DEFINED
    yard_other = input("Enter the fence material that the property contains: ")
def switch_yard_material(yard_material):
    yard_switcher = {
        0: totalValue+200,
        1: totalValue+500,
        2: totalValue+500,
        3: totalValue+300,
        4: totalValue+800,
        5: totalValue+400,
        6: totalValue+700,
        7: totalValue+300
    }.get(yard_material, "Invalid, will not be considered")
    return yard_switcher
totalValue = switch_yard_material(yard_material)
#print(totalValue)



additional_factors = input("Are there any additional factor(s) that should be considered (yes or no)?: ")
if(additional_factors == "yes"):
    add_fac_yes = input("Please list the additional factors: ")

#AT THE END I THINK WE SHOULD PULL THE BEST AND CLOSEST COMPS AND THEN DO SOME FORM OF A COMPARATOR TO ADJUST OUR ESTIMATE BEFORE IT OUTPUTS.

print (totalValue)
