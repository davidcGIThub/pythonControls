# Mass Spring Damper Parameters file
import numpy as np

# Physical parameters of the arm known to the controller
m = 5.0     # Mass, kg
k = 3.0 # spring constant, N/m
b = 0.5 # damper coeficient, N-sec/m

w = 5.0 # width of mass, m
h = 5.0 # hieght of the mass, m
# parameters for animation

# Initial Conditions
z0 =  0 # meters
zdot0 = 0 # meters/sec

# Simulation Parameters

tstep = 0.1  # time step size for simulation
time = 10.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation
# dirty derivative parameters

Kd  = 5.0 # derivatice gain
Kp = 3.0# proportional gain

# saturation limits
