import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import bobParam as P
import bobDynamics as dyn
import bobController as contr
import reference as ref

#initialize states
state = [P.z0,P.zdot0,P.theta0,P.thetadot0]
theta_prev = P.theta0
#initialize previous states
z_prev = P.z0
#initialize desired reference
zd = ref.reference(0)
#initialize input force
F = contr.bobController(zd,state[0],z_prev,state[2],theta_prev)
#initialize the arrays containing data
Fdata = []
zdata = []
thetadata = []
Fdata.append(F)
zdata.append(P.z0)
thetadata.append(P.theta0)
tdata = np.linspace(0,P.time,P.steps+1)

for i in range(0,P.steps):
    #desired reference position
    zd = ref.reference(i*P.tstep)
    # use controller to get force
    F = contr.bobController(zd,state[0],z_prev,state[2],theta_prev)
    #save the previous states
    z_prev = state[0]
    theta_prev = state[2]
    #assign new states from the dynamics
    state = dyn.bobDynamics(state[0],state[1],state[2],state[3],F)
    #append data
    Fdata.append(F)
    thetadata.append(state[2])
    zdata.append(state[0])

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
