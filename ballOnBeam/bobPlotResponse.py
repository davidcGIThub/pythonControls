import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import bobParam as P
import bobDynamics as dyn
import bobController as contr

zdata = []
thetadata = []
tdata = np.linspace(0,P.time,P.steps+1)
state = [P.z0,P.zdot0,P.theta0,P.thetadot0]
theta_prev = P.theta0
z_prev = P.z0
zd = 5 #z desired, m
F = contr.bobController(zd,state[0],z_prev,state[2],theta_prev)

Fdata = []
Fdata.append(F)
zdata.append(P.z0)
thetadata.append(P.theta0)

for i in range(0,P.steps):
    z_prev = state[0]
    theta_prev = state[2]
    state = dyn.bobDynamics(state[0],state[1],state[2],state[3],F)
    F = contr.bobController(zd,state[0],z_prev,state[2],theta_prev)
    Fdata.append(F)
    thetadata.append(state[2])
    zdata.append(state[0])
    print F

plt.figure(1)
plt.clf()
plt.plot(tdata,thetadata)
plt.title("Ball On Beam Response")
plt.ylabel("Angle theta (rad)")
plt.xlabel("Time t (sec)")
plt.show()

plt.figure(2)
plt.clf()
plt.plot(tdata,zdata)
plt.title("Ball On Beam Response")
plt.ylabel("Z position (m)")
plt.xlabel("Time t (sec)")
plt.show()

plt.figure(3)
plt.clf()
plt.plot(tdata,Fdata)
plt.title("Ball On Beam Force Input")
plt.ylabel("Force (N)")
plt.xlabel("Time t (sec)")
plt.show()




#find the rise time
# t = tdata[-1]
# for l in range(0,len(zdata)-1):
#     if abs(zdata[l] - zdata[-1]*.9) < .01:
#         t = tdata[l]
#         break
#
# print(t) # print the rise timeB
