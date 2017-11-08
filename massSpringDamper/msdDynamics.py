#Dynamics of the mass spring damper, give the current state and returns the state of the next time step
import numpy as np
import msdParam as P


def msdDynamics(z,zdot,F):

    tstep = P.tstep

    state = np.matrix([[z],[zdot]])

    k1 = derivatives(state,F)
    #print(k1)
    k2 = derivatives(state + tstep/2*k1,F)
    #print(k2)
    k3 = derivatives(state + tstep/2*k2,F)
    #print(k3)
    k4 = derivatives(state + tstep*k3,F)
    #print(k4)

    temp = state + (tstep/6) * (k1 + 2*k2 + 2*k3 + k4)
    newState = [temp.item(0),temp.item(1)]
    #print(state)

    return newState

def derivatives(state, force):

    m = P.m
    b = P.b
    k = P.k
    z = state.item(0);
    zdot = state.item(1);
    zddot = (force - b*zdot - k*z) / m

    return np.matrix([[zdot],[zddot]])
