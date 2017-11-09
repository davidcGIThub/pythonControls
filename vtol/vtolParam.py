# Vtol Parameters file
import numpy as np

# Physical parameters of the vtol system
mc = 1  # Mass of the center, kg
mr = .25 # Mass of the right side, kg
ml = .25 # Mass of the left side, kg
mt = mc + ml + mr # Total Mass, kg
Jc = 0.0042 # inertia, kg m^2
d = 0.3 # distance force exerted from center of mass, m
L = .5 # Length of Beam, m
mew = 0.1 # drag coeficient, kg/s
g = 9.8 # gravity constant, m/s^2

# parameters for animation
center_width = d*2/5
motor_length = d * 2 / 3
motor_width = center_width /2
target_width = center_width/2

# Initial Conditions
z0 = 2.5
zdot0 = 0
h0 = 1.25
hdot0 = 0
theta0 = 0
thetadot0 = 0
zt0 = 2.5;
ztdot0 = 0;

# Simulation Parameters

tstep = 0.01  # time step size for simulation
time = 2.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation
# dirty derivative parameters


# saturation limits
