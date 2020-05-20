"""
Created on Wed May 20 14:03:55 2020

@author: Kolby Kuratnick
"""

# RealEstatimator


#1. Download estimator.py and dict.json

#2. Go to line 1508 in estimator.py and change path to the path you downloaded the dict.json file.

#3. Begin running estimator.py and inputting answers to questions asked
#
#
#More detailed version and info about the code setup below.
#
#For this project, you will need to download the dict.json file. This json file
#is information gathered about 196 houses in the town of Bear, DE.
#
#Once downloaded, scroll to line 1508 in the estimator.py file and update the 
#path where the dict.json file is located.
#
#At this point, you are ready to run the estimator.py file. You will get some
#introduction information printed out to the console before you begin answering
#questions for the estimation.
#
#In the estimator.py file, there are numerous sections. The first section is all
#the functions that we wrote and use. After these, each feature of a house has
#its own section denoted by the "start" and "end" comments.
#
#The features were research to determine the value that each one has on a house
#appraisal. Some features were able to be estimated specifically on the value
#they have in Bear, DE. Otherwise were general to Delaware, the Northeast, and
#the United States. We looked for as precise of a value as possible.
#
#One of the most important aspects of appraising a house is finding a recently
#sold comparison to adjust all of the values of the features. For example, in
#upstate NY, a basement is very common. Conversely, a lot of houses in Delaware
#don't have basements. For this reason, a "comparator" was implemented after
#the value of the features were implemented. The "comparator" looks for the 
#1-5 most comparable houses in Bear, DE and compares the value of that house
#to the value of the house input by the user. If comparable, the estimation of 
#the house stays the same. If the estimation is outside a reasonable range, then
#the "comparator" will adjust the estimation.
#
#Finally, there is a function that determines the error of the estimation
#compared to "eppraisal" and zillow's "zestimate." These appraisal companies
#report accuracy of upwards of 1.8%, but if you go through and compare by hand
#zillow's estimates are often off by more than 5% 63% of the time. For this
#reason, we felt pretty successful if we could be around 5% off or better 50%
#of the time.
