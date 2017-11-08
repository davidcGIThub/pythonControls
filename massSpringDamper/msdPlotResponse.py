import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import msdParam as P
import msdDynamics as dyn
import msdController as contr



zdata = []
tdata = np.linspace(0,P.time,P.steps+1)
state = [P.z0,P.zdot0]
zprev = P.z0
Fdata = []

zd = 5 #position desired, m
Fdata.append(contr.msdController(zd,state[0],zprev))
zdata.append(P.z0)

for i in range(0,P.steps):

    F = contr.msdController(zd,state[0],zprev)
    Fdata.append(F)
    zprev = state[0] #save the previous position
    state = dyn.msdDynamics(state[0],state[1],F)
    zdata.append(state[0])

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
