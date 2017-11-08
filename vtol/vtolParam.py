# Vtol Parameters file
import numpy as np

# Physical parameters of the vtol system
mc = 1  # Mass of the center, kg
ms = .25 # Mass of the sides, kg
Jc = 0.0042 # inertia, kg m^2
d = 0.3 # distance force exerted from center of mass, m
L = .5 # Length of Beam, m
mew = 0.1 # drag coeficient, kg/s
g = 9.8 # gravity constant, m/s^2

# parameters for animation


# Initial Conditions


# Simulation Parameters

tstep = 0.01  # time step size for simulation
time = 2.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation
# dirty derivative parameters


# saturation limits
