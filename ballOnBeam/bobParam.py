# Ball on Beam Parameters file
import numpy as np

# Physical parameters of the ball and beam system
m1 = 0.35  # Mass of ball, kg
m2 = 2.0 # Mass of beam, kg
L = .5 # Length of Beam, m
g = 9.8 # gravit constant, m/s^2

# parameters for animation
w = .01 # width of beam, m
D = .09

# Initial Conditions
theta0 =  -.1 # angle of beam, radians
thetadot0 = 0 # angular speed beam, radians/sec
z0 = L/2 # positon of ball, m
zdot0 = 0 # speed of the ball, m/s

# Simulation Parameters
tstep = 0.1 # time step size for simulation
tstepInner = tstep/10
time = 20.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation

# dirty derivative parameters
KdIn  = 1.9550 # derivatice gain
KpIn = 5.06967  # proportional gain

KdOut  = -.0528508 # derivatice gain
KpOut = -.0137048# proportional gain

# saturation limits
