

#classes as defined by ISTEA and NCHRP 365 page 22
class1area=50000
class2area=200000
class3area=500000
class4area=1000000

#income threshholds as identified in NCHRP 365 page 23
lowincome=20000
mediumincome=40000
#not used, but in here for reference purposes:
highincome=50000

# Step 1:  get the average trips per household PTPHH = personal trips per household | LI = low income MI = medium | HI = highincome

##Step1.a these rates are based on NCHRP 365 page 24  and should only be used incase no other data is available (Bakc of the envelope type calcas | hh = household
class1ptphh=9.2
class2ptphh=9.0
class3ptphh=8.6
class4ptphh=8.5

# {'table5': [{'li': (3.6, 6.5, ....), 'mi':
#              (3.9, 7.3, ...), 'hi': (4.5, 9.2, ...)}, {'li': (3.1, 6.3, ...),
#             'mi': ....}], 'table6': ....}
# yourData['table5'][0]['li']

##step1.b NCHRP table 5 page 25 "Average daily person trips per household by persons per household and income
#number after ptphh represents persons per household
class1li = (3.6, 6.5, 9.1, 11.5, 13.8)
class1mi = (3.9, 7.3, 10.0, 13.1, 15.9)
class1hi = (4.5, 9.2, 12.2, 14.8, 18.2)

class2li = (3.1, 6.3, 9.4, 12.5, 14.7)
class2mi = (4.8, 7.2, 10.1, 13.3, 15.5)
class2hi = (4.9, 7.7, 12.5, 13.8, 16.7)

class3li = (3.6, 7.1, 9.0, 12.0, 14.0)
class3mi = (4.8, 7.1, 9.8, 12.7, 14.6)
class3hi = (4.8, 7.8, 11.5, 13.6, 16.6)

class4li = (3.7, 6.3, 8.1, 10.0, 11.8)
class4mi = (4.9, 7.6, 9.1, 12.3, 15.1)
class4hi = (5.4, 7.9, 10.3, 12.4, 15.3)

##step1.c NCHRP table 6 page 26 "Average daily person trips per household and auto ownership persons per household and income
#number of after autos referes too average vehicles per household
class1auto0 = (2.6, 4.8, 7.4, 9.2, 11.2)
class1auto1 = (4.0, 6.7, 9.2, 11.5, 13.7)
class1auto2 = (4.0, 8.1, 10.6, 13.3, 16.7)
class1auto3plus = (4.0, 8.4, 11.9, 15.1, 18.0)

class2auto0 = (2.1, 4.0, 6.0, 7.0, 8.0)
class2auto1 = (4.3, 6.3, 8.8, 11.2, 13.2)
class2auto2 = (4.3, 7.5, 10.6, 13.0, 15.4)
class2auto3plus = (4.3, 7.5, 13.0, 15.3, 18.3)

class3auto0 = (2.5, 4.4, 5.6, 6.9, 8.2)
class3auto1 = (4.6, 6.7, 8.8, 11.0, 12.8)
class3auto2 = (4.6, 7.8, 10.4, 13.0, 15.4)
class3auto3plus = (4.6, 7.8, 12.1, 14.6, 17.2)

class4auto0 = (3.1, 4.9, 6.6, 7.8, 9.4)
class4auto1 = (4.6, 6.7, 8.2, 10.5, 12.5)
class4auto2 = (4.6, 7.8, 9.3, 11.8, 14.7)
class4auto3plus = (4.6, 7.8, 10.5, 13.3, 16.2)

## step 1.d  Table 7 page 27, "Average daily person trips by income and autos owned"
class1liauto = (3.4, 5.3, 8.7, 10.6)
class1miauto = (5.3, 7.0, 10.1, 12.1)
class1hiauto = (7.1, 8.9, 12.4, 14.6)

class2liauto = (2.8, 4.9, 8.6, 11.5)
class2miauto = (4.0, 7.1, 10.0, 13.4)
class2hiauto = (5.2, 8.4, 11.2, 14.0)

class2liauto = (3.2, 5.5, 9.2, 11.8)
class2miauto = (4.0, 7.0, 10.0, 11.9)
class2hiauto = (4.9, 8.1, 11.0, 13.8, 11.5)

class2liauto = (3.7, 5.0, 7.9, 9.8)
class2miauto = (5.8, 7.1, 9.8, 12.0)
class2hiauto = (6.8, 8.3, 10.4, 12.1)

# step 2: divide the trips into Home Base Work (HBW), NonHBW and NHB Table 0 page 29-30 "trip estimation variables by urban size"
## order is HBW , HBO, NHB
class1liclassification = (0.16, 0.60, 0.24)
class1miclassification = (0.21, 0.56, 0.23)
class1hiclassification = (0.20, 0.55, 0.25)
class1hh1classification = (0.50, 0.54, 0.26)
class1hh2classification = (0.22, 0.54, 0.24)
class1hh3classification = (0.19, 0.56, 0.25)
class1hh4classification = (0.19, 0.58, 0.23)
class1hh5plusclassification = (0.17, 0.62, 0.21)

class2liclassification = (0.17, 0.60, 0.23)
class2miclassification = (0.20, 0.56, 0.24)
class2hiclassification = (0.23, 0.52, 0.25)
class2hh1classification = (0.20, 0.56, 0.24)
class2hh2classification = (0.23, 0.53, 0.24)
class2hh3classification = (0.22, 0.54, 0.24)
class2hh4classification = (0.18, 0.61, 0.21)
class2hh5plusclassification = (0.19, 0.59, 0.22)

class3liclassification = (0.18, 0.59, 0.23)
class3miclassification = (0.23, 0.55, 0.22)
class3hiclassification = (0.22, 0.54, 0.24)
class3hh1classification = (0.23, 0.54, 0.23)
class3hh2classification = (0.24, 0.53, 0.23)
class3hh3classification = (0.23, 0.54, 0.23)
class3hh4classification = (0.21, 0.57, 0.22)
class3hh5plusclassification = (0.18, 0.62, 0.20)

class4liclassification = (0.16, 0.62, 0.22)
class4miclassification = (0.21, 0.56, 0.23)
class4hiclassification = (0.24, 0.51, 0.25)
class4hh1classification = (0.23, 0.50, 0.27)
class4hh2classification = (0.25, 0.52, 0.23)
class4hh3classification = (0.25, 0.52, 0.23)
class4hh4classification = (0.21, 0.59, 0.20)
class4hh5plusclassification = (0.19, 0.62, 0.19)
