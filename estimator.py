# #Property Value Estimator 
# #Takes in user input regarding all property details individually to compute the property estimate
# #Square foot value is determined by the type of room (bedroom, kitchen, bathroom, etc and then the additional sq footage of the house is estimated as the basic sq ft value dependent on condition)

# totalValue = 0

# print("Welcome to the Property Value Estimator.....Please answer some questions!")
# print("You will be asked about the condition of various aspects of your home. Here is some information to help you. \n Poor is 15% of homes, average is 50% of homes, good is 20% of homes, and excellent is 15% of homes. Typically excellent is reserved for new construction or very recently remodeled homes.")
# print("Please enter your answers exactly how they are represented in the question.")
# address = raw_input("Enter the property's address (street address town, state zipcode): ") #VALUE STILL NEEDED
# zipcode = raw_input("Please reenter the property's zipcode: ")
# while True:
#     try:
#         prop_type = input("Choose the property type:\n(0) Single Family Home\n(1) Duplex\n(2) Triplex\n(3) Manafactured\n(4) Townhouse\n(5) Condo\n(6) Mobile Home\n(7) Apartment\n\n") #VALUE STILL NEEDED
#         if prop_type in range(8):
#             break
#     except:
#         pass
#     print '\nIncorrect input, try again!'



# year_built = raw_input("Enter the year the property was built: ")
# if year_built > 2000
# 	(year_built-2000)*500 = year_built_value
# elif year_built < 1975
# 	(1975-year_built)*-500 = year_built_value
# 	totalValue = totalValue + year_built_value
# else
# 	totalValue = totalValue



prop_sqft = raw_input("Enter the property square footage: ")
while True:
    try:
        prop_condition = raw_input("Choose the current property condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
        if prop_type in range(3):
            break
    except:
        pass
    print '\nIncorrect input, try again!'
def switch_property_value(prop_condition):
	switcher_property = {
		0: prop_value = prop_sqft*100,
		1: prop_value = prop_sqft*125,
		2: prop_value = prop_sqft*150,
		3: prop_value = prop_sqft*165,
	}
	print switcher_property.get(prop_condition, "Invalid, will not be considered")



# lot_sqft = raw_input("Enter the lot square footage: ")
# while True:
#     try:
#         lot_condition = raw_input("Choose the current lot condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
#         if lot_type in range(3):
#             break
#     except:
#         pass
#     print '\nIncorrect input, try again!'
# totalValue = totalValue+(lot_sqft*3.55)



# bedrooms = input("Enter total number of bedrooms: ")
# for x in range(1, bedrooms+1):
#     if(bedrooms == 0):
#         break
#     else:
#         print "Bedroom", x, ":"
#         bedroom_x_sqft = input("Enter bedroom " + str(x) +" sqft: ")
#         while True:
#             try:
#                 bedroom_x_condition = input("Bedroom" + str(x) + " Choose the bedroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
#                 if bedroom_x_condition in range(4):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'
# 		def switch_bedroom_value(bedroom_x_condition);
# 			switcher_bedroom = {
# 				0: bedroom_x_value = bedroom_x_sqft*60,
# 				1: bedroom_x_value = bedroom_x_sqft*80,
# 				2: bedroom_x_value = bedroom_x_sqft*90,
# 				3: bedroom_x_value = bedroom_x_sqft*100,
# 			}
# 			bedroom_final_value = bedroom_final_value+bedroom_x_value
# 			print switcher_bedroom.get(bedroom_x_condition, "Invalid, will not be considered")
# totalValue = totalValue+bedroom_final_value



# half_bathrooms = input("Enter total number of half bathrooms: ") #VALUE STILL NEEDED
# for x in range(1, half_bathrooms+1):
#     if(half_bathrooms == 0):
#         break
#     else:
#         print "Half Bathroom", x, ":"
#         hbath_x_sqft = input("Enter half bathroom " + str(x) +" sqft: ")
#         while True:
#             try:
#                 hbath_x_condition = input("Half Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0)Poor\n(1)Average\n(2)Good\n(3)Excellent\n\n")
#                 if hbath_x_condition in range(4):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'
#         while True:
#             try:
#                 hbath_x_floor_material=input("Choose the half bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n")
#                 if hbath_x_floor_material in range(5):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'
#         while True:
#             try:
#                 hbath_x_ctop_material=input("Choose the half bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
#                 if hbath_x_ctop_material in range(6):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'



# full_bathrooms = input("Enter total number of full bathrooms: ") #VALUE STILL NEEDED
# for x in range(1, full_bathrooms+1):
#     if(full_bathrooms == 0):
#         break
#     else:
#         print "Full Bathroom", x, ":"
#         fbath_x_sqft = input("Enter full bathroom " + str(x) +" sqft: ")
#         while True:
#             try:
#                 fbath_x_condition = input("Full Bathroom " + str(x) + ": Choose the half bathroom condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
#                 if fbath_x_condition in range(4):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'
#         while True:
#             try:
#                 fbath_x_floor_material=input("Choose the full bath floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n\n")
#                 if fbath_x_floor_material in range(5):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'
#         while True:
#             try:
#                 fbath_x_ctop_material=input("Choose the full bath countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
#                 if fbath_x_ctop_material in range(6):
#                     break
#             except:
#                 pass
#             print '\nIncorrect input, try again!'



# kitchen = input("Enter the square footage of the kitchen: ") #VALUE STILL NEEDED
# while True:
#     try:
#         kitchen_floor_material=input("Choose the kitchen floor material:\n(0) Carpet\n(1) Hardwood\n(2) Linoleum/Vinyl\n(3) Tile(Rock, Ceramic, Porcelain)\n(4) Laminate\n(5) Wood/Butcher Block\n\n")
#         if kitchen_floor_material in range(6):
#             break
#     except:
#         pass
#     print '\nIncorrect input, try again!'
# while True:
#     try:
#         kitchen_ctop_material=input("Choose the kitchen countertop material:\n(0) Granite\n(1) Marble\n(2) Soapstone\n(3) Quartz\n(4) Ceramic Tile\n(5) Laminate\n\n")
#         if kitchen_ctop_material in range(6):
#             break
#     except:
#         pass
#     print '\nIncorrect input, try again!'



# basement = raw_input("Is there a basement (yes or no): ")
# if(basement == "yes"):
#     basement_sqft = input("Enter the square footage of the basement: ")
# 	basement_door = raw_input("Is it a walk out basement (yes or no): ")
# 	while True:
#      try:
# 		basement_condition = raw_input("Choose the current basement condition:\n(0) Poor\n(1) Average\n(2) Good\n(3) Excellent\n\n")
# 		if basement_condition in range(3):
# 			break
# 	except:
# 		pass
#     basement_finished = raw_input("Is the basement finished (yes or no): ")
#     if(basement_finished == "yes"):
#         basement_finished_sqft = input("Enter the square footage of the finished basement: ")
# 		def switch_basement_finished_value(basement_condition);
# 			switcher_basement_finished = {
# 				0: basement_finished_value = basement_finished_sqft*30,
# 				1: basement_finished_value = basement_finished_sqft*45,
# 				2: basement_finished_value = basement_finished_sqft*60,
# 				3: basement_finished_value = basement_finished_sqft*75,
# 			}
# 			print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
# 	elif
# 		basement_unfinished_sqft = basement_sqft-basement_finished_sqft
# 		def switch_basement_unfinished_value(basement_condition);
# 			switcher_basement_unfinished = {
# 				0: basement_unfinished_value = basement_unfinished_sqft*10,
# 				1: basement_unfinished_value = basement_unfinished_sqft*15,
# 				2: basement_unfinished_value = basement_unfinished_sqft*20,
# 				3: basement_unfinished_value = basement_unfinished_sqft*25,
# 			}
# 			print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
# 		basement_value = basement_unfinished_value+basement_finished_value
# 		if (basement_door == yes)
# 			basement_value = basement_value*1.2
# 	else
# 		def switch_basement_finished_value(basement_condition);
# 			switcher_basement_finished = {
# 				0: basement_value = basement_sqft*10,
# 				1: basement_value = basement_sqft*15,
# 				2: basement_value = basement_sqft*20,
# 				3: basement_value = basement_sqft*25,
# 			}
# 			print switcher_basement_finished.get(basement_condition, "Invalid, will not be considered")
# 			if (basement_door == yes)
# 				basement_value = basement_value*1.2
	
		 
		 
		 
# AC_type = raw_input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n")		 
# 	def switch_AC(AC_type):
# 		switcher_AC = {
# 			0: totalValue = totalValue-500,
# 			1: totalValue = totalValue-400,
# 			2: totalValue = totalValue-0,
# 			3: totalValue = totalValue-0,
# 			4: totalValue = totalValue+500,
# 			5: totalValue = totalValue+0,
# 		}
# 	print switcher_AC.get(AC_type, "Invalid, will not be considered")
# #AC NEEDS AN "OTHER" OPTION CODE PART


# roof_age = input("How old is the roof (enter a number): ") #VALUE STILL NEEDED
# roof_type = raw_input("Choose the roof type\n(0) Slate Tile\n(1) Clay Tile\n (2)Copper\n (3)Other Metals\n (4)Wood Shingle\n (5)Fiber Cement Shingles\n (6)Asphalt Shingles\n (7)Other\n\n")
# if(roof_type == "7"):
#     roof_other = raw_input("Enter the roof type that the property contains: ")
# def switch_roof(roof_type):
# 	switcher_roof = {
# 		0: usability = totalValue-500,
# 		1: totalValue = totalValue-400,
# 		2: totalValue = totalValue-0,
# 		3: totalValue = totalValue-0,
# 		4: totalValue = totalValue+500,
# 		5: totalValue = totalValue+0,
# 		6: totalValue = totalValue+500,
# 		7: totalValue = totalValue+0,
# 		}
# 	print switcher_roof.get(roof_type, "Invalid, will not be considered")


# appliances = raw_input("Choose appliances sold with house (enter all letters that apply):\n(0) Washer\n(1) Dryer\n(2) Dishwasher\n(3) Fridge\n(4) Microwave\n(5) Stove\n\n") #VALUE STILL NEEDED
# kitchen_appliances = raw_input("Are all kitchen appliances color coordinated (yes or no)?: ")
# wash_dry = raw_input("Are the washer and dryer appliances color coordinated (yes or no)?: ")



# pool = raw_input("Is there a pool installed? (yes or no): ") #VALUE STILL NEEDED
# if(pool == "yes"):
#     pool_install = raw_input("Enter if the pool is 'in-ground' or 'above-ground': ")
#     pool_sqft = input("Enter the square footage of the pool: ")



# hot_tub = input("Enter the square footage of the hot tub if installed and 0 if not: ") #VALUE STILL NEEDED




# driveway = raw_input("Is there a driveway?: ") #VALUE STILL NEEDED
# if(driveway == "yes"):
#     driveway_space = input("Enter the number of parking spaces: ")
#     driveway_material = raw_input("Choose the driveway material\n(0) Concrete\n(1) Brick\n(2) Rock\n(3) Asphalt\n\n")




# garage = raw_input("Is there a garage installed? (yes or no): ") #VALUE STILL NEEDED
# if(garage == "yes"):
#     garage_install = raw_input("Enter if garage is 'attached' or 'detached': ")
#     garage_sqft = input("Enter the square footage of the garage: ")




# AC_type = raw_input("Choose the AC type\n(0) Window Units\n(1) House Fan\n(2) Central Air\n(3) Ductless Mini-Split AC\n(4) Geothermal\n(5) Other\n\n")
# if(AC_type == "5"):
#     AC_other = raw_input("Enter the AC type that the property contains: ")
# def switch_AC(AC_type):
# 	switcher_AC = {
# 		0: totalValue = totalValue-500,
# 		1: totalValue = totalValue-400,
# 		2: totalValue = totalValue-0,
# 		3: totalValue = totalValue-0,
# 		4: totalValue = totalValue+500,
# 		5: totalValue = totalValue+0,
# 	}
# 	print switcher_AC.get(AC_type, "Invalid, will not be considered")




# heat_type = raw_input("Choose the heat type\n(0) Boiler\n(1) Furnace\n(2) Standard Heat Pump\n(3) Mini Split Heat Pump\n(4) Geothermal\n(5) Other\n\n")
# if(heat_type == "5"):
#     heat_other = raw_input("Enter the heat type that the property contains: ")
# def switch_Heat(heat_type):
# 	switcher_heat = {
# 		0: totalValue = totalValue-500,
# 		1: totalValue = totalValue-350,
# 		2: totalValue = totalValue-0,
# 		3: totalValue = totalValue-0,
# 		4: totalValue = totalValue+500,
# 		5: totalValue = totalValue+0,
# 	}
# 	print switcher_heat.get(heat_type, "Invalid, will not be considered")	
	
	
	
# fireplaces = input("Enter the number of fireplaces if installed and 0 if not: ")
# totalValue = totalValue+(fireplaces*800)



# electric_system = raw_input("Please enter if the electric system is 'fuse box' or a 'circuit breaker'")
# if electric_system == str(fuse box)
# 	totalValue = totalValue-500



# #view_type = raw_input("Choose all view types (enter as many letters as applicable):\n(0) River\n(1) Lake\n(2) Ocean\n(3) Golf Course\n(4) Mountain\n(5) Skyline\n(6) Standard\n\n") #VALUE STILL NEEDED



# water_type = heat_type = raw_input("Please enter if the water/sewage system is 'town' or a 'septic+well'")
# if water_type == str(septic+well)
# 	totalValue = totalValue-1000



# foundation_material = raw_input("Choose the foundation material\n(0) Stone\n(1) Brick\n(2) Preservative treated lumber\n(3) Concrete Block\n(4) Poured Concrete\n(5) Other\n\n")
# if(foundation_material == "5"):
#     foundation_other = raw_input("Enter the foundation material that the property contains: ")
# def switch_foundation_material(foundation_material):
# 	switcher_foundation = {
# 		0: totalValue = totalValue-10000,
# 		1: totalValue = totalValue-3000,
# 		2: totalValue = totalValue-8000,
# 		3: totalValue = totalValue-500,
# 		4: totalValue = totalValue+0,
# 		5: totalValue = totalValue+0,
# 	}
# 	print switcher_foundation.get(foundation_material, "Invalid, will not be considered")




# porch = raw_input("Is there a porch (yes or no)?: ") #VALUE STILL NEEDED
# if(porch == "yes"):
#     porch_num = input("Enter the number of porches: ")
#     for x in range (1, porch_num+1):
#         print "Porch", x, ":"
#         porch_sqft = input("Enter porch " + str(x) +" sqft: ")
#         porch_material = raw_input("Choose the porch material\n(0) Wood\n(1) Vinyl\n(2) Plastic Wood Composites\n\n")
# #PORCH NEEDS AN "OTHER" OPTION CODE PART




# patio = raw_input("Is there a patio (yes or no)?: ") #VALUE STILL NEEDED
# if(patio == "yes"):
#     patio_num = input("Enter the number of patios: ")
#     for x in range (1, patio_num+1):
#         print "Patio", x, ":"
#         patio_sqft = input("Enter patio " + str(x) +" sqft: ")
#         patio_material = raw_input("Choose the patio material\n(0) Brick\n(1) Stone\n(2) Patio Pavers\n(3) Concrete\n(4) Gravel\n\n")
# #PATIO NEEDS AN "OTHER" OPTION CODE PART




# yard = raw_input("Is there a yard fenced in (yes or no)?: ") #VALUE STILL NEEDED
# if(yard == "yes"):
#     yard_material = raw_input("Choose the fence material\n(0) Chain Link\n(1) Picket Fence\n(2) Synthetic\n(3) Aluminum\n(4) Vinyl\n(5) Composite\n(6) Other\n\n")
#     if(yard_material == "6"):
#         yard_other = raw_input("Enter the fence material that the property contains: ")





# additional_factors = raw_input("Are there any additional factor(s) that should be considered (yes or no)?: ")
# if(additional_factors == "yes"):
#     add_fac_yes = raw_input("Please list the additional factors: ")



# print totalValue
