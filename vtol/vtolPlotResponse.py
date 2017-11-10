import numpy as np
import matplotlib.pyplot as plt
import vtolController as contr
import numpy as np
import vtolParam as P
import vtolDynamics as dyn
import math

thetadata = []
zdata = []
hdata = []
tdata = np.linspace(0,P.time,P.steps+1)
state = [P.z0,P.zdot0,P.h0,P.hdot0,P.theta0,P.thetadot0]
fl = 0
fr = 0

z_prev = P.z0
h_prev = P.h0
theta_prev = P.theta0

zdata.append(P.z0)
hdata.append(P.h0)
thetadata.append(P.theta0)

zd = 1
hd = 2

for i in range(0,P.steps):
    [fl,fr] = contr.vtolController(zd,state[0],z_prev,hd,state[2],h_prev,state[4],theta_prev)
    z_prev = state[0]
    h_prev = state[2]
    theta_prev = state[4]
    state = dyn.vtolDynamics(state[0],state[1],state[2],state[3],state[4],state[5],fl,fr)
    zdata.append(state[0])
    hdata.append(state[2])
    thetadata.append(state[4])

plt.figure(1)
plt.clf()
plt.plot(tdata,zdata)
plt.title("Vtol Response")
plt.ylabel("Z position (m)")
plt.xlabel("Time t (sec)")
plt.show()

plt.figure(2)
plt.clf()
plt.plot(tdata,hdata)
plt.title("Vtol Response")
plt.ylabel("h position (m)")
plt.xlabel("Time t (sec)")
plt.show()

plt.figure(3)
plt.clf()
plt.plot(tdata,thetadata)
plt.title("Vtol Response")
plt.ylabel("Angle theta (radians)")
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
