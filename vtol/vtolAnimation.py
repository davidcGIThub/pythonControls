import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import animation
import vtolParam as P
import vtolDynamics as dyn
import math
import vtolController as contr
import reference as ref

#Setting Things up
center_width = P.center_width
motor_length = P.motor_length
motor_width = P.motor_width
target_width = P.target_width
fig = plt.figure()
plt.axes().set_aspect('equal')
ax = fig.add_subplot(111)
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
# center vtol
x_ = P.z0 - center_width*math.cos(0)/2
y_ = P.h0 - center_width/2
center = patches.Rectangle((x_,y_),center_width,center_width,fc = 'red',ec = 'black')
#left motor
x_ = P.z0 - P.d*math.cos(P.theta0)
y_ = P.h0 - P.d*math.sin(P.theta0)
rmotor = patches.Ellipse(xy=[x_,y_],width = motor_length, height = motor_width, angle = P.theta0)
#right motor
x_ = P.z0 + P.d*math.cos(P.theta0)
y_ = P.h0 + P.d*math.sin(P.theta0)
lmotor = patches.Ellipse(xy=[x_,y_],width = motor_length, height = motor_width, angle = P.theta0)
#target
target = patches.Rectangle((P.zt0,0),target_width,target_width,fc = 'red',ec = 'black')
#left and right panel
line1, = ax.plot([], [], lw=P.d, color = 'black')
line2, = ax.plot([], [], lw=P.d, color = 'black')
#Initialize the states
state = [P.z0,P.zdot0,P.h0,P.hdot0,P.theta0,P.thetadot0]
#Initialize the previous states
z_prev = P.z0
theta_prev = P.theta0
h_prev = P.h0
#Initialize the desired positions
zd = ref.reference_z(0)
hd = ref.reference_h(0)
#initialize counter
k = 0
def init():
    ax.add_patch(center)
    ax.add_patch(lmotor)
    ax.add_patch(rmotor)
    ax.add_patch(target)
    line1.set_data([], [])
    line2.set_data([], [])
    return center,lmotor,rmotor,target,line1,line2

def animate(i):
    global state
    global z_prev
    global theta_prev
    global h_prev
    global zd
    global hd
    global k
    #update the desired locations
    zd = ref.reference_z(P.tstep*k)
    hd = ref.reference_h(P.tstep*k)
    print ("zd: ", zd, "hd: ", hd)
    #Compute the forces from the controller
    [fl,fr] = contr.vtolController(zd,state[0],z_prev,hd,state[2],h_prev,state[4],theta_prev)
    #Save the previous states
    z_prev = state[0]
    h_prev = state[2]
    theta_prev = state[4]
    #plots stuff
    z_ = state[0]
    h_ = state[2]
    theta_ = state[4]
    #left panel
    line1.set_data([z_,z_-P.d*math.cos(theta_)],[h_,h_-P.d*math.sin(theta_)])
    #right panel
    line2.set_data([z_,z_+P.d*math.cos(theta_)],[h_,h_+P.d*math.sin(theta_)])
    #center
    x_ = z_ - center_width*math.cos(theta_)/2 + center_width*math.cos(math.pi/2-theta_)/2
    y_ = h_ - center_width*math.sin(theta_)/2 - center_width*math.sin(math.pi/2-theta_)/2
    center.set_xy([x_,y_])
    center._angle = theta_*180/math.pi
    #left motor
    lmotor.set_visible(True)
    x_ = z_ - P.d*math.cos(theta_)
    y_ = h_ - P.d*math.sin(theta_)
    lmotor.center = x_,y_
    lmotor.angle = theta_*180/math.pi
    #right motor
    rmotor.set_visible(True)
    x_ = z_ + P.d*math.cos(theta_)
    y_ = h_ + P.d*math.sin(theta_)
    rmotor.center = x_,y_
    rmotor.angle = theta_*180/math.pi
    #target
    target.set_xy([P.zt0,0]) #doesnt move right now
    #Find the new States
    state = dyn.vtolDynamics(state[0],state[1],state[2],state[3],state[4],state[5],fl,fr)
    #update counter
    k = k + 1

    return center,lmotor,rmotor,target,line1,line2

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=True)
plt.show()
