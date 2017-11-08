import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import bobParam as P
import bobDynamics as dyn
#import bobController as contr

thetadata = []
tdata = np.linspace(0,P.time,P.steps+1)
state = [P.z0,P.zdot0,P.theta0,P.thetadot0]
#thetaprev = P.theta0
#Fdata = []
F = 5
#thetad = 1 #theta desired, m
#Fdata.append(contr.bobController(zd,state[0],zprev))
thetadata.append(P.theta0)

for i in range(0,P.steps):

    #F = contr.msdController(zd,state[0],zprev)
    #Fdata.append(F)
    #zprev = state[0] #save the previous position

    state = dyn.bobDynamics(state[0],state[1],state[2],state[3],F)
    thetadata.append(state[2])

plt.figure(1)
plt.clf()
plt.plot(tdata,thetadata)
plt.title("Ball On Beam Response")
plt.ylabel("Angle theta (rad)")
plt.xlabel("Time t (sec)")
plt.show()

# plt.figure(2)
# plt.clf()
# plt.plot(tdata,Fdata)
# plt.title("Mass Spring Damper Force Input")
# plt.ylabel("Force (N)")
# plt.xlabel("Time t (sec)")
# plt.show()




#find the rise time
# t = tdata[-1]
# for l in range(0,len(zdata)-1):
#     if abs(zdata[l] - zdata[-1]*.9) < .01:
#         t = tdata[l]
#         break
#
# print(t) # print the rise timeB
