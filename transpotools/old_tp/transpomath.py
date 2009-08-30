#math equations
def interpolate(x1, y1, x2, y2, x3):
    y3 = ((y2 - y1) * ((x3 - x1)/(x2-x1))) + y1
    return y3