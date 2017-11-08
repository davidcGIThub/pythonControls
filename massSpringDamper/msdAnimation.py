import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import animation
import msdParam as P
import msdDynamics as dyn
import msdController as contr

fig = plt.figure()
plt.axes().set_aspect('equal')
ax = fig.add_subplot(111)
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
rectangle = patches.Rectangle((P.z0,0),P.w,P.h,fc = 'red',ec = 'black')
#circle = patches.Circle((0, 0), radius=0.75, fc='y')
#damper
line1, = ax.plot([], [], lw=1, color = 'blue')
line2, = ax.plot([], [], lw=1, color = 'blue')
line3, = ax.plot([], [], lw=1, color = 'blue')
line4, = ax.plot([], [], lw=1, color = 'blue')
#spring
line5, = ax.plot([], [], lw=1, color = 'green')

state = [P.z0,P.zdot0]
zprev = state[0]
global zd
zd = 5 #position desired, m


def init():
    ax.add_patch(rectangle)
    #ax.add_patch(circle
    #damper initialization
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    #spring initialization
    line5.set_data([], [])

    return line1,line2,line3,line4,line5,rectangle

def animate(i):
    #damper
    global state
    global zd
    global zprev

    c = state[0]
    line1.set_data([0,2.25+c/2],[1,1])
    line2.set_data([2.75+c/2,5+c], [1,1])
    line3.set_data([2.75+c/2,c/2+2.25,2.25+c/2,2.75+c/2], [.5,.5,1.5,1.5])
    line4.set_data([2.75+c/2,2.75+c/2], [.75,1.25])
    #spring
    line5.set_data([0,1.5,1.75+c*(.5/4),2.25+c*(1.5/4),2.75+c*(2.5/4),3.25+c*(3.5/4),3.5+c,5+c], [4,4,4.5,3.5,4.5,3.5,4,4])

    rectangle.set_xy([c+5,0])
    #circle.center = (7,c)
    F = contr.msdController(zd,state[0],zprev)
    zprev = state[0] #save the previous position
    state = dyn.msdDynamics(state[0],state[1],F)
    return line1,line2,line3,line4,line5,rectangle

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=True)
plt.show()
