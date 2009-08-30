
#definitions:
# totalpopulation = total population of the area under analysis
# baseyear = is the year at which analysis is conducted

import tripgenerationconstants
import transpomath

#variables to be inputed by the user:
#inflation rate calculated from local base year currency to 1990 USD, default = 1
currencyconversion = 1
#base year default value = 1990 corressponding with NCHRP 365
baseyear=1990

def urbanareasize(totalpopulation):
    """ this function determines the classification of area under analysis based on population
    based on ISTEA and NCHRP 365 classifications| Class System based on ISTEA and NCHRP 365
    50,000 < class1 < 199,999 |  200,000 < class2 < 499,999 | 500,000 < class3 < 999,999 | 1,000,000 < class4 """
    if totalpopulation < tripgenerationconstants.class1city:
        raise ValueError("This model only predicts areas with population greather than 50,000")
    if totalpopulation < tripgenerationconstants.class2city:
        return 1
    elif totalpopulation < tripgenerationconstants.class3city:
        return 2
    elif totalpopulation < tripgenerationconstants.class4city:
        return 3
    else:
        return 4

def convertincomevalues(currencyconversion, incometocompare):
    """ this function converts 1990 income values to base year analysis AND estimates if a value is low, medium, or highincome
    lowincome is less than 1990usd $20,000, midiumincome is between 20,000 and 40,000 | mediumincome is greater than 40,000 1990usd
    based on NCHRP 365 | lowincome = 1, mediumincome = 2, highincome = 3 """
    if incometocompare <= tripgenerationconstants.lowincome * currencyconversion:
        return 1
    elif incometocompare > tripgenerationconstants.lowincome  * currencyconversion and incometocompare< tripgenerationconstants.mediumincome * currencyconversion:
        return 2
    else:
        return 3

def tripproduction(population, households, avgincomeperhh, avgautosperhh, currencyconversion):
    """ this function estimates the number of trips produced per zone according to NCHRP 365 tables presented in tripgeneration constants.py
    population per zone, average household income per zone, average autos per hh, and currency conversion as explained earlier. 
    Analysis can be done based on population and houseolds, or pop household and avgincomeperhh and/or avgautoperphh"""
    # TODO interpolate between the y categories and not just the x
    
    if convertincomevalues(currencyconversion, avgincomeperhh) == 1:
        #do stuff
        return ''
    elif convertincomevalues(currencyconversion, avgincomeperhh) == 2:
        #do stuff
        return ''
    elif convertincomevalues(currencyconversion, avgincomeperhh) == 3:
        #do stuff
        return ''
    else:
        #do stuff
        return ''
    # step 2 calculate total trip productions
    
    #step 3 divide trips in HBW, HBO, and NHB
    

    return tripsproduced_HBW, tripsproduced_HBO, tripsproduced_NHB

def tripattraction():
    return ''

def balanceatractionsandproductions():
    return ''

class TripGeneration:
    pass

