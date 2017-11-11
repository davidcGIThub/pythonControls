import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import msdParam as P
import msdDynamics as dyn
import msdController as contr

#Set things up

#position desired, m
zd = 5
#initialize the states
state = [P.z0,P.zdot0]
zprev = P.z0
#Set up Data Arrays
Fdata = []
zdata = []
tdata = np.linspace(0,P.time,P.steps+1)
Fdata.append(contr.msdController(zd,state[0],zprev))
zdata.append(P.z0)

for i in range(0,P.steps):
    #Find force neccesary from controller
    F = contr.msdController(zd,state[0],zprev)
    #save the previous position
    zprev = state[0]
    #Find the new states
    state = dyn.msdDynamics(state[0],state[1],F)
    #Append Data to the arrays
    zdata.append(state[0])
    Fdata.append(F)

plt.figure(1)
plt.clf()
plt.plot(tdata,zdata)
plt.title("Mass Spring Damper Response")
plt.ylabel("Position Z (m)")
plt.xlabel("Time t (sec)")
plt.show()

plt.figure(2)
plt.clf()
plt.plot(tdata,Fdata)
plt.title("Mass Spring Damper Force Input")
plt.ylabel("Force (N)")
plt.xlabel("Time t (sec)")
plt.show()

#find the rise time
t = tdata[-1]
for l in range(0,len(zdata)-1):
    if abs(zdata[l] - zdata[-1]*.9) < .01:
        t = tdata[l]
        break

print(t) # print the rise timeB
