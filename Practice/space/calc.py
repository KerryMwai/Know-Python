def planet_mass(gravity, radiius):
    mass=(gravity*radiius**2)/(6.67*10**-11)
    return  mass

def planet_vol(radius):
    volume=(4*3.142*radius**2)/3
    return  volume