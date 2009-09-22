import math

# constant dict
rates = {( 1, 5 ):9, ( 2, 5 ):8, ( 1, 6 ):7, ( 2, 6 ):6}
print rates
def interpolate( x, y ):
    x_1 = int( math.floor( x ) )
    x_2 = int( math.ceil( x ) )
    y_1 = int( math.floor( y ) )
    y_2 = int( math.ceil( y ) )

    z = ( ( x_2 - x_1 ) * ( y_2 - y_1 ) )

    result = ( ( ( rates[( x_1, y_1 )] ) * ( ( x_2 - x ) * ( y_2 - y ) ) / ( z ) )
    + ( ( rates[( x_2, y_1 )] ) * ( ( x - x_1 ) * ( y_2 - y ) ) / ( z ) )
    + ( ( rates[( x_1, y_2 )] ) * ( ( x_2 - x ) * ( y - y_1 ) ) / ( z ) )
    + ( ( rates[( x_2, y_2 )] ) * ( ( x - x_1 ) * ( y - y_1 ) ) / ( z ) ) )

    return result

print interpolate( 1.5, 5.5 )

