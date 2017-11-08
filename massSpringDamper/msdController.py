import numpy as py
import msdParam as P
def msdController(zd,z,z_prev):

    error =  zd - z
    deriv = (z - z_prev)/P.tstep
    force =  error*P.Kp - deriv*P.Kd

    #if abs(force) > 2:
    #    force = 2

    return force
