import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import animation
import bobParam as P
import bobDynamics as dyn
import bobController as contr
import math
from signalGenerator import signalGenerator

fig = plt.figure()
plt.axes().set_aspect('equal')
ax = fig.add_subplot(111)
ax.set_xlim(-1, 1)
ax.set_ylim(-.75, .75)
# beam
rectangle = patches.Rectangle((0,0),P.L,P.w,fc = 'blue',ec = 'black')
#ball
yb_init = P.D/2+P.w # initial y position of ball when beam is horizontal
circle = patches.Circle((.25, yb_init), radius=P.D/2, fc='red')

state = [P.z0,P.zdot0,P.theta0,P.thetadot0]
zprev = state[0]
thetaprev = state[2]

reference = signalGenerator(amplitude=.15, frequency=0.01, y_offset=.25)
zd = reference.square(0)[0]  #position desired, m


def init():
    ax.add_patch(rectangle)
    ax.add_patch(circle)
    return rectangle,circle

def animate(i):
    #damper
    global state
    global yb_init
    global zd
    global zprev
    global thetaprev
    #ball position
    xball = state[0]*math.cos(state[2])-P.D/2*math.sin(state[2])
    yball = state[0]*math.sin(state[2])+P.D/2*math.cos(state[2])
    #ball
    circle.center = (xball,yball)
    #beam
    rectangle.set_xy([0,0])
    rectangle._angle = state[2]*180/math.pi
    #F = contr.msdController(zd,state[0],zprev)
    #zprev = state[0] #save the previous position
    zprev = state[0]
    thetaprev = state[2]

    F = contr.bobController(zd,state[0],zprev,state[2],thetaprev)
    state = dyn.bobDynamics(state[0],state[1],state[2],state[3],F)
    zd = reference.square(i * P.tstep)[0]
    print("zd = ", zd, " time= ", i * P.tstep)

    return rectangle,circle

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=True)
plt.show()
