import numpy as py
import bobParam as P

# the outer controller
def bobController(zd,z,z_prev,theta,theta_prev):
    error =  zd - z
    deriv = (z - z_prev)/P.tstep
    thetad =  error*P.KpOut - deriv*P.KdOut
    force_tilde = bobInnerController(thetad,theta,theta_prev)
    force_e = P.g*(P.m1*z/P.L + P.m2/2)
    F = force_tilde + force_e
    return F

def bobInnerController(thetad,theta,theta_prev):
    error =  thetad - theta
    deriv = (theta - theta_prev)/P.tstepInner
    force =  error*P.KpIn - deriv*P.KdIn
    return force
