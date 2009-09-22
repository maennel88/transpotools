'''
@author: dassouki
@file: trip generation.py
@date: August, 31, 2009
@summary :
 This file is part of transpo tools, a QGIS plugin

    This is based on chapter 3 of NCHRP 365, Trip Generation balances trip 
    attractions and productions between different traffic analysis zones (TAZ)
    
    Analysis Guideline:
      1- Data Setup
        1.1- Provide proper urban population
        1.2- get currency levels to define low/medium/high incomes
        1.3- Type of Analysis
        1.4- return proper trip rates
      2- Trip Attractions
        2.1- develop the following attractions based on page 28 formulae
          HBW (Home Base Work
          HBO_CBD (HB other - central business district)
          HBO_NCBD (HBO Non CBD)
          NHB_CBD (non home based work)
          NHB_NCBD
      3- Trip ProductionS
        3.1- census data is interpolated to provide adequate trip rates for each
            zone
      4- Trip Balancing
        4-1- Trips are then balanced for the over all system. Note that external
          are considered in the external_trips.py module
'''

import math, numpy

# constants
base_low_income = 20000 # income < 20,000 - based on USD 1990, NCRHP page 23
base_medium_income = 39999 # 20,000 < income < 40,000 . High income > 40,000

# step 1.1 Type of urban area
''' this function returns the type of analysis based on population size '''
def get_population_stratification( urban_population ):
  if urban_population >= 0 and urban_population <= 199999:
    return 1
  elif urban_population >= 200000 and urban_population <= 499999:
    return 2
  elif urban_population >= 500000 and urban_population <= 999999:
    return 3
  elif urban_population >= 1000000:
    return 4

# step 1.2 convert to current level incomes
def income_levels( base_low_income, base_medium_income, currency_exchange_rate ):
  ''' this function converts money to a 1990 USD rate and generates low, medium, &
    high income values
  '''
  low_income = currency_exchange_rate * base_low_income
  medium_income = currency_exchange_rate * base_medium_income
  return ( low_income, medium_income ) # income_levels(params)[0]

# step 1-3 determine the analysis type
def get_analysis_type( bool_income = False, bool_vehicles = False, bool_pph = False ):
  ''' this function determins which variables are used to estimate the trip rates
    in this modeling exerise
    pph = persons per household
'''
  if bool_income and bool_vehicles and bool_pph:
    #table 5
    return 1
  elif bool_income and bool_vehicles and bool_pph:
    #table 6
    return 2
  elif bool_income and bool_vehicles and bool_pph:
    #table 7
    return 3

# step 1.4 return trip rates
def trip_rates( population_stratification, analysis_type, low_income, medium_income, high_income ):
  ''' this function returns the proper trip rate tuple to be used based on input 
    data 
    ADPT = Average Daily Person Trips per Household
    pph = person per household
    veh_hh = vehicles per household
    (param_1, param_2): ADPT
  '''
  li = low_income
  mi = medium_income
  hi = high_income
  # table 5 -
  if analysis_type == 1:
    if population_stratification == 1:
      rates = {( li, 1 ):3.6, ( li, 2 ):6.5, ( li, 3 ):9.1, ( li, 4 ):11.5, ( li, 5 ): 13.8,
               ( mi, 1 ):3.9, ( mi, 2 ):7.3, ( mi, 3 ):10.0, ( mi, 4 ):13.1, ( mi, 5 ): 15.9,
               ( hi, 1 ):4.5, ( hi, 2 ):9.2, ( hi, 3 ):12.2, ( hi, 4 ):14.8, ( hi, 5 ): 18.2}
      return rates
    if population_stratification == 2:
      rates = {
               ( li, 1 ):3.1, ( li, 2 ):6.3, ( li, 3 ):9.4, ( li, 4 ):12.5, ( li, 5 ): 14.7,
               ( mi, 1 ):4.8, ( mi, 2 ):7.2, ( mi, 3 ):10.1, ( mi, 4 ):13.3, ( mi, 5 ): 15.5,
               ( hi, 1 ):4.9, ( hi, 2 ):7.7, ( hi, 3 ):12.5, ( hi, 4 ):13.8, ( hi, 5 ): 16.7
              }
      return rates
    if population_stratification == 3: #TODO: input actual rate
      rates = {
               ( li, 1 ):3.6, ( li, 2 ):6.5, ( li, 3 ):9.1, ( li, 4 ):11.5, ( li, 5 ): 13.8,
               ( mi, 1 ):3.9, ( mi, 2 ):7.3, ( mi, 3 ):10.0, ( mi, 4 ):13.1, ( mi, 5 ): 15.9,
               ( hi, 1 ):4.5, ( hi, 2 ):9.2, ( hi, 3 ):12.2, ( hi, 4 ):14.8, ( hi, 5 ): 18.2
              }
      return rates
    if population_stratification == 4: #TODO: input actual rate
      rates = {
               ( li, 1 ):3.1, ( li, 2 ):6.3, ( li, 3 ):9.4, ( li, 4 ):12.5, ( li, 5 ): 14.7,
               ( mi, 1 ):4.8, ( mi, 2 ):7.2, ( mi, 3 ):10.1, ( mi, 4 ):13.3, ( mi, 5 ): 15.5,
               ( hi, 1 ):4.9, ( hi, 2 ):7.7, ( hi, 3 ):12.5, ( hi, 4 ):13.8, ( hi, 5 ): 16.7
              }
      return rates
  #table 6
  elif analysis_type == 2:
    if population_stratification == 1: #TODO: Change rates
      rates = {
               ( 0, 1 ):3.6, ( 0, 2 ):6.5, ( 0, 3 ):9.1, ( 0, 4 ):11.5, ( 0, 5 ): 13.8,
               ( 1, 1 ):3.9, ( 1, 2 ):7.3, ( 1, 3 ):10.0, ( 1, 4 ):13.1, ( 1, 5 ): 15.9,
               ( 2, 1 ):4.5, ( 2, 2 ):9.2, ( 2, 3 ):12.2, ( 2, 4 ):14.8, ( 2, 5 ): 18.2,
               ( 3, 1 ):4.5, ( 3, 2 ):9.2, ( 3, 3 ):12.2, ( 3, 4 ):14.8, ( 3, 5 ): 18.2
              }
      return rates
    if population_stratification == 2: #TODO: Change rates
      rates = {
               ( 0, 1 ):3.6, ( 0, 2 ):6.5, ( 0, 3 ):9.1, ( 0, 4 ):11.5, ( 0, 5 ): 13.8,
               ( 1, 1 ):3.9, ( 1, 2 ):7.3, ( 1, 3 ):10.0, ( 1, 4 ):13.1, ( 1, 5 ): 15.9,
               ( 2, 1 ):4.5, ( 2, 2 ):9.2, ( 2, 3 ):12.2, ( 2, 4 ):14.8, ( 2, 5 ): 18.2,
               ( 3, 1 ):4.5, ( 3, 2 ):9.2, ( 3, 3 ):12.2, ( 3, 4 ):14.8, ( 3, 5 ): 18.2
              }
      return rates
    if population_stratification == 3: #TODO: Change rates
      rates = {
               ( 0, 1 ):3.6, ( 0, 2 ):6.5, ( 0, 3 ):9.1, ( 0, 4 ):11.5, ( 0, 5 ): 13.8,
               ( 1, 1 ):3.9, ( 1, 2 ):7.3, ( 1, 3 ):10.0, ( 1, 4 ):13.1, ( 1, 5 ): 15.9,
               ( 2, 1 ):4.5, ( 2, 2 ):9.2, ( 2, 3 ):12.2, ( 2, 4 ):14.8, ( 2, 5 ): 18.2,
               ( 3, 1 ):4.5, ( 3, 2 ):9.2, ( 3, 3 ):12.2, ( 3, 4 ):14.8, ( 3, 5 ): 18.2
              }
      return rates
    if population_stratification == 4: #TODO: Change rates
      rates = {
               ( 0, 1 ):3.6, ( 0, 2 ):6.5, ( 0, 3 ):9.1, ( 0, 4 ):11.5, ( 0, 5 ): 13.8,
               ( 1, 1 ):3.9, ( 1, 2 ):7.3, ( 1, 3 ):10.0, ( 1, 4 ):13.1, ( 1, 5 ): 15.9,
               ( 2, 1 ):4.5, ( 2, 2 ):9.2, ( 2, 3 ):12.2, ( 2, 4 ):14.8, ( 2, 5 ): 18.2,
               ( 3, 1 ):4.5, ( 3, 2 ):9.2, ( 3, 3 ):12.2, ( 3, 4 ):14.8, ( 3, 5 ): 18.2
              }
      return rates
  # table 7
  elif analysis_type == 3:
    if population_stratification == 1: #TODO: input actual rate
      rates = {
               ( li, 0 ):3.6, ( li, 1 ):6.5, ( li, 2 ):9.1, ( li, 3 ):11.5,
               ( mi, 0 ):3.9, ( mi, 1 ):7.3, ( mi, 2 ):10.0, ( mi, 3 ):13.1,
               ( hi, 0 ):4.5, ( hi, 1 ):9.2, ( hi, 2 ):12.2, ( hi, 3 ):14.8
              }
      return rates
    if population_stratification == 2: #TODO: input actual rate
      rates = {
               ( li, 0 ):3.6, ( li, 1 ):6.5, ( li, 2 ):9.1, ( li, 3 ):11.5,
               ( mi, 0 ):3.9, ( mi, 1 ):7.3, ( mi, 2 ):10.0, ( mi, 3 ):13.1,
               ( hi, 0 ):4.5, ( hi, 1 ):9.2, ( hi, 2 ):12.2, ( hi, 3 ):14.8
              }
      return rates
    if population_stratification == 3: #TODO: input actual rate
      rates = {
               ( li, 0 ):3.6, ( li, 1 ):6.5, ( li, 2 ):9.1, ( li, 3 ):11.5,
               ( mi, 0 ):3.9, ( mi, 1 ):7.3, ( mi, 2 ):10.0, ( mi, 3 ):13.1,
               ( hi, 0 ):4.5, ( hi, 1 ):9.2, ( hi, 2 ):12.2, ( hi, 3 ):14.8
              }
      return rates
    if population_stratification == 4: #TODO: input actual rate
      rates = {
               ( li, 0 ):3.6, ( li, 1 ):6.5, ( li, 2 ):9.1, ( li, 3 ):11.5,
               ( mi, 0 ):3.9, ( mi, 1 ):7.3, ( mi, 2 ):10.0, ( mi, 3 ):13.1,
               ( hi, 0 ):4.5, ( hi, 1 ):9.2, ( hi, 2 ):12.2, ( hi, 3 ):14.8
              }
      return rates

def interpolate( population_stratification, analysis_type, low_income, medium_income, high_income, x, y ):
  #get rates dict
  rates = trip_rates( population_stratification, analysis_type, low_income, medium_income, high_income )


  # dealing with x parameters
  #when using income levels, x_1 and x_2 are li, mi, or hi
  if analysis_type == 1 or analysis_type == 2 or analsis_type == 4:
    if x < high_income and x >= medium_income:
      x_1 = medium_income
      x_2 = high_income
    elif x < medium_income:
      x_1 = low_income
      x_2 = medium_income
    else:
      x_1 = high_income
      x_2 = high_income
  if analysis_type == 3:
    if x >= 3:
      x_1 = 3
      x_2 = 3
    else:
      x_1 = int( math.floor( x ) )
      x_2 = int( math.ceil( x ) )

  # dealing with y parametrs
  #when using persons per household, max number y = 5
  if analysis_type == 1 or analysis_type == 4:
    if y >= 5:
      y_1 = 5
      y_2 = 5
    else:
      y_1 = int( math.floor( y ) )
      y_2 = int( math.ceil( y ) )
  elif analysis_type == 2 or analysis_type == 3:
    if y >= 5:
      y_1 = 5
      y_2 = 5
    else:
      y_1 = int( math.floor( y ) )
      y_2 = int( math.ceil( y ) )

  # denominator
  z = ( ( x_2 - x_1 ) * ( y_2 - y_1 ) )

  result = ( ( ( rates[( x_1, y_1 )] ) * ( ( x_2 - x ) * ( y_2 - y ) ) / ( z ) ) +
             ( ( rates[( x_2, y_1 )] ) * ( ( x - x_1 ) * ( y_2 - y ) ) / ( z ) ) +
             ( ( rates[( x_1, y_2 )] ) * ( ( x_2 - x ) * ( y - y_1 ) ) / ( z ) ) +
             ( ( rates[( x_2, y_2 )] ) * ( ( x - x_1 ) * ( y - y_1 ) ) / ( z ) ) )

  return result

#test
low_income = 20000 #this is calculated using exchange rates
medium_income = 40000 # this is calculated using exchange rates
high_income = 60000 # this is calculated using exchange rates
population_stratification = 1 #inputed by user
analysis_type = 1 #inputed by user
x = 35234.34 #test income
y = 3.5 # test pph

print interpolate( population_stratification, analysis_type, low_income, medium_income, high_income, x, y )
