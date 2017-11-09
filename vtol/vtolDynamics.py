#Dynamics of the vtol, give the current state and returns the state of the next time step
import numpy as np
import vtolParam as P
import math

def vtolDynamics(z,zdot,h,hdot,theta,thetadot,fl,fr):

    tstep = P.tstep

    state = np.matrix([[z],[zdot],[h],[hdot],[theta],[thetadot]])

    #derivatives of z
    k1 = derivatives(state,fl,fr)         #k values for runga kutta
    k2 = derivatives(state + (tstep/2.0)*k1 , fl,fr)
    k3 = derivatives(state + (tstep/2.0)*k2 , fl,fr)
    k4 = derivatives(state + tstep*k3,fl,fr)
    #print(k4_theta)

    #runga kutta calculation
    temp = state + (tstep/6.0) * (k1 + 2*k2 + 2*k3 + k4)

    newState = [temp.item(0),temp.item(1),temp.item(2),temp.item(3),temp.item(4),temp.item(5)]
    #print(state)
    return newState

def derivatives(state,fl,fr):
    z = state.item(0)
    zdot = state.item(1)
    h = state.item(2)
    hdot = state.item(3)
    theta = state.item(4)
    thetadot = state.item(5)

    mc = P.mc
    mr = P.mr
    ml = P.ml
    Jc = P.Jc
    d = P.d
    L = P.L
    mew = P.mew
    g = P.g

    zddot = (-(fr + fl)*math.sin(theta) - mew*zdot)/(mc + mr + ml)
    hddot = (-(mc+2*mr)*g + (fr + fl)*math.cos(theta))/(mc+mr+ml)
    thetaddot = d*(fr-fl)/(Jc+2*mr*d**2)


    return np.matrix([[zdot],[zddot],[hdot],[hddot],[thetadot],[thetaddot]])
