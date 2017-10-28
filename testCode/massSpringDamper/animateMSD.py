# import dynamicsMSD as dyn
# import showState as shs
# import MSDParam as P
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# plt.ion()
#
# state = [P.z0,P.zdot0]
# F = 3
#
# for i in range(0,P.steps):
#
#     shs.showState(state[0])
#     plt.pause(0.0001)
#     print(state)
#     state = dyn.dynamicsMSD(state[0],state[1],F)

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    c = i
    # x = np.linspace(0, 2, 1000)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    # line.set_data(x, y)
    return plt.fill([5+c, 5+c, 10+c,10+c, 5+c],[0, 5, 5, 0, 0],'r'),

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
