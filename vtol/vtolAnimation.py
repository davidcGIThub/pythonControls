import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import animation
import vtolParam as P
import vtolDynamics as dyn
import math

center_width = P.center_width
motor_length = P.motor_length
motor_width = P.motor_width
target_width = P.target_width

fig = plt.figure()
plt.axes().set_aspect('equal')
ax = fig.add_subplot(111)
ax.set_xlim(0, 5)
ax.set_ylim(0, 2.5)

# center vtol
x_ = P.z0 - center_width*math.cos(0)/2
y_ = P.h0 - center_width/2
center = patches.Rectangle((x_,y_),center_width,center_width,fc = 'red',ec = 'black')

#left motor
x_ = P.z0 - P.d*math.cos(P.theta0)
y_ = P.h0 - P.d*math.sin(P.theta0)
rmotor = patches.Ellipse(xy=[x_,y_],width = motor_length, height = motor_width, angle = P.theta0)

#left panel
line1 = ax.plot([], [], lw=P.d, color = 'black')

#right motor
x_ = P.z0 + P.d*math.cos(P.theta0)
y_ = P.h0 + P.d*math.sin(P.theta0)
lmotor = patches.Ellipse(xy=[x_,y_],width = motor_length, height = motor_width, angle = P.theta0)

#right panel
line2 = ax.plot([], [], lw=P.d, color = 'black')

#target
target = patches.Rectangle((P.zt0,0),target_width,target_width,fc = 'red',ec = 'black')

#rectangle = patches.Rectangle((0,0),P.L,P.w,fc = 'blue',ec = 'black')
#ball
#yb_init = P.D/2+P.w # initial y position of ball when beam is horizontal
#circle = patches.Circle((.25, yb_init), radius=P.D/2, fc='red')
state = [P.z0,P.zdot0,P.h0,P.hdot0,P.theta0,P.thetadot0]


def init():
    ax.add_patch(center)
    ax.add_patch(lmotor)
    ax.add_patch(rmotor)
    ax.add_patch(target)
    line1.set_data([], [])
    line2.set_data([], [])
    return center,lmotor,rmotor,target #,line1,line2

def animate(i):
    #damper
    global state
    z_ = state[0]
    h_ = state[2]
    theta_ = state[4]
    #center
    x_ = z_ - center_width*math.cos(theta_)/2
    y_ = h_ - center_width/2
    center.set_xy([x_,y_])
    center._angle = theta_*180/math.pi
    #left motor
    x_ = z_ - P.d*math.cos(theta_)
    y_ = h_ - P.d*math.sin(theta_)
    lmotor.xy = [x_,y_]
    lmotor._angle = theta_*180/math.pi
    #right motor
    x_ = z_ + P.d*math.cos(theta_)
    y_ = h_ + P.d*math.sin(theta_)
    lmotor.xy = [x_,y_]
    lmotor._angle = theta_*180/math.pi
    #left panel
    line1.set_data([z_,h_],[z_-P.d*math.cos(theta_),h_-P.d*math.sin(theta_)])
    #right panel
    line2.set_data([z_,h_],[z_+P.d*math.cos(theta_),h_+P.d*math.sin(theta_)])
    #target
    target.set_xy([P.zt0,0]) #doesnt move right now
    return center,lmotor,rmotor,target #,line1,line2

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=True)
plt.show()