#Dynamics of the mass spring damper, give the current state and returns the state of the next time step
import numpy as np
import msdParam as P

def msdDynamics(z,zdot,F):


    m = P.m
    b = P.b
    k = P.k
    tstep = P.tstep

    zddot = (F - b*zdot - k*z) / m

    deriv = np.matrix([[zdot],[zddot]]) #derivatives
    k1 = deriv
    #print(k1)
    k2 = deriv + tstep/2*k1
    #print(k2)
    k3 = deriv + tstep/2*k2
    #print(k3)
    k4 = deriv + tstep*k3
    #print(k4)

    temp = np.matrix([[z],[zdot]]) + (tstep/6) * (k1 + 2*k2 + 2*k3 + k4)
    state = [temp.item(0),temp.item(1)]
    #print(state)

    return state
