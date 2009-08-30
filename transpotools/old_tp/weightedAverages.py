
# this class calculates the weighted average of the x and y centroids of a large zone system
# based on the weight distribution of the sub zones
# for example a city zone has 10 sub zones(areas)
# some areas have more residential activity than commercial for instance
# the housing weighted average will calculate the centroid of the city 
# based on housing (weight) distribution.

#defines vector Matrix
class Point( object ):
    def __init__( self, x, y, z ):
        self.x, self.y, self.z= x, y, z

#calculates centroid weight averages

def calc_weighted_avg(pts):
    CxNum = sum([pt.x * pt.z for pt in pts])
    CxDenom = sum([pt.z for pt in pts])
    Cx = CxNum / CxDenom
    print "Value of Cx: ", Cx
            

testCentroidWeightMatrix = [Point(1.5, 1.5, 2), Point(2.5,1.5,5), Point(3.5,1.5,1), Point(1.5,2.5,4), Point(2.5,2.5,9), Point(3.5,2.5,8)]
calc_weighted_avg(testCentroidWeightMatrix)
