import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import animation
import bobParam as P
import bobDynamics as dyn
import bobController as contr
import math
import reference as ref

#set up
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
#states
state = [P.z0,P.zdot0,P.theta0,P.thetadot0]
#initialize previous states
zprev = state[0]
thetaprev = state[2]
#initialize desired location
zd = ref.reference(0)


def init():
    ax.add_patch(rectangle)
    ax.add_patch(circle)
    return rectangle,circle

def animate(i):
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
    #controller
    F = contr.bobController(zd,state[0],zprev,state[2],thetaprev)
    #save the previous states
    zprev = state[0]
    thetaprev = state[2]
    #dynamics
    state = dyn.bobDynamics(state[0],state[1],state[2],state[3],F)
    #new desired reference
    zd = ref.reference(i * P.tstep)

    print("zd = ", zd, " time= ", i * P.tstep)

    return rectangle,circle

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=2,
                               blit=True)
plt.show()
