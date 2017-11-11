# Vtol Parameters file
import numpy as np

# Physical parameters of the vtol system
mc = 1  # Mass of the center, kg
mr = .25 # Mass of the right side, kg
ml = .25 # Mass of the left side, kg
mt = mc + ml + mr # Total Mass, kg
Jc = 0.0042 # inertia, kg m^2
d = 0.3 # distance force exerted from center of mass, m
mew = 0.1 # drag coeficient, kg/s
g = 9.8 # gravity constant, m/s^2

# uncertain parameters
uncertain = True
sign = -1
if(np.random.rand() > .5 ):
    sign = 1
mc_ = mc + .2*mc*np.random.rand()*sign
mr_ = mr
ml_ = ml
mt = mc_ + mr_ + ml
Jc_ = Jc + .2*Jc*np.random.rand()*sign
d_ = d + .2*d*np.random.rand()*sign
mew_ = mew + .2*mew*np.random.rand()*sign
g_ = g 

# parameters for animation
center_width = d*2/5
motor_length = d * 2 / 3
motor_width = center_width /2
target_width = center_width/2

# Initial Conditions
z0 = 4
zdot0 = 0
h0 = 2.5
hdot0 = 0
theta0 = 0
thetadot0 = 0
zt0 = 4;
ztdot0 = 0;

# Simulation Parameters

tstep = 0.01  # time step size for simulation
time = 2.0 # time in seconds of simulation
steps = int(time/tstep) # number of steps in simulation
# dirty derivative parameters

Kp_H = .113437#height control - Force
Kd_H = .5832

Kp_Lat_In = .372075# Theta Control - Tau
Kd_Lat_In = .191314

Kp_Lat_Out = -.032076 # Z control - theta
Kd_Lat_Out = -.007716

# saturation limits
saturated = True
upper = 10
lower = -10

#desired reference
amplitude_z = 2.5
frequency_z = .08
offset_z = 3

amplitude_h = 0
frequency_h = 1
offset_h = 0
