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
theta0 =  0 # angle of beam, radians
thetadot0 = 0 # angular speed beam, radians/sec
z0 = .25 # positon of ball, m
zdot0 = 0 # speed of the ball, m/s

# Simulation Parameters

tstep = 0.01  # time step size for simulation
time = 2.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation
# dirty derivative parameters

Kd  = 5.0 # derivatice gain
Kp = 3.0# proportional gain

# saturation limits
