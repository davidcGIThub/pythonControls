#Dynamics of the mass spring damper, give the current state and returns the state of the next time step
import numpy as np
import vtolParam as P
import math

def vtolDynamics(z,zdot,theta,thetadot,h,hdot,F):

    tstep = P.tstep

    state = np.matrix([[z],[zdot],[theta],[thetadot],])


    #derivatives of z
    k1 = derivatives(state,F)         #k values for runga kutta
    k2 = derivatives(state + (tstep/2.0)*k1 , F)
    k3 = derivatives(state + (tstep/2.0)*k2 , F)
    k4 = derivatives(state + tstep*k3,F)
    #print(k4_theta)

    #runga kutta calculation
    temp = state + (tstep/6.0) * (k1 + 2*k2 + 2*k3 + k4)

    if z >= .5 and zdot >= 0:
        temp[0] = .5
        temp[1] = 0
    if z <= 0 and zdot <= 0:
        temp[0] = 0
        temp[1] = 0
    print(temp)

    newState = [temp.item(0),temp.item(1),temp.item(2),temp.item(3)]
    #print(state)
    return newState

def derivatives(state,force):
    z = state.item(0)
    zdot = state.item(1)
    theta = state.item(2)
    thetadot = state.item(3)

    g  = P.g
    L = P.L
    m1 = P.m1
    m2 = P.m2

    thetaddot = ( force*L*abs(math.cos(theta)) - 2*m1*z*thetadot*zdot - m1*g*z*math.cos(theta) - (m2*g*L/2)*math.cos(theta) ) / (m1*z*z + (m2*L*L)/3)
    zddot = z*thetadot*thetadot - g*math.sin(theta)

    return np.matrix([[zdot],[zddot],[thetadot],[thetaddot]])
