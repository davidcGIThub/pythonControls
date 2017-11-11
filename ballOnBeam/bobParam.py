# Ball on Beam Parameters file
import numpy as np

# Physical parameters of the ball and beam system
m1 = 0.35  # Mass of ball, kg
m2 = 2.0 # Mass of beam, kg
L = .5 # Length of Beam, m
g = 9.8 # gravit constant, m/s^2

#Uncertain parameters
uncertian = True
sign = -1
if(np.random.rand() > .5 ):
    sign = 1
m1_ = m1 + .2*m1*np.random.rand()*sign
m2_ = m2 + .2*m2*np.random.rand()*sign
L_ = L + .2*L*np.random.rand()*sign
g_ = g + .2*g*np.random.rand()*sign

# parameters for animation
w = .01 # width of beam, m
D = .09

# Initial Conditions
theta0 =  0 # angle of beam, radians
thetadot0 = 0 # angular speed beam, radians/sec
z0 = L/2 # positon of ball, m
zdot0 = 0 # speed of the ball, m/s

# Simulation Parameters
tstep = 0.01 # time step size for simulation
time = 20.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation

# dirty derivative parameters
tr_In = 1
Zeta_In = .707
Wn_In = 2.2/tr_In
KpIn = Wn_In**2 * ( (m1*L**2)/4 + (m2*L**2)/3 ) / L # control theta
KdIn = 2*Zeta_In*Wn_In * ( (m1*L**2)/4 + (m2*L**2)/3 ) / L
KpIn = 126
KdIn = 9.77
#KdIn  = 1.9550 # derivatice gain
#KpIn = 5.06967  # proportional gain

tr_Out = 10*tr_In
Zeta_Out = .707
Wn_Out = 2.2/tr_Out
KdOut = 2*Zeta_Out*Wn_Out / (-g)
KpOut = (Wn_Out**2)/(-g)
KpOut = -.34
KdOut = -.03

#KdOut  = -.0528508 # derivatice gain
#KpOut = -.0137048# proportional gain

# saturation limits
saturated = True
upper = 15
lower = -15


#desired reference
amplitude = .15
frequency = .02
offset = .25
