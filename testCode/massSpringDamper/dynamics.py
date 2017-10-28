import plot_msd as msd
import numpy as np
import matplotlib.pyplot as plt

m = 5 # kg
k = 3 # N/m
b = 0.5 # N-sec/m
F = 3 # N
zdot0 = 0; # m/s, initial conditions
z0 = 0; # m, initial conditions
tstep = .1
t = np.linspace(0,5,num = 50)
state = [z0;zdot0]
zp = t * 0;

for i in range(0,len(t)):
    zp[i] = state[0]
    z = state[0]
    #print(state[0])
    zdot = state[1]
    print(state[1])
    zddot = (F - b*zdot - k*z) / m

    k1 = np.matrix([[zdot],
                     [zddot]])
    #print(k1)
    k2 = np.matrix([[zdot+tstep/2*k1.item(0)],
                    [zddot+tstep/2*k1.item(1)]])
    #print(k2)
    #print(k2.item(0))
    #print(k2.item(1))
    k3 = np.matrix([[zdot+tstep/2*k2.item(0)],
                    [zddot+tstep/2*k2.item(1)]])
    #print(k3)
    k4 = np.matrix([[zdot+tstep*k3.item(0)],
                    [zddot+tstep*k3.item(1)]])
    #print(k4)

    #print("state0: " , state[0] , " tstep: " , tstep , " k1[0]: " , k1[0] , " k2[0]: " , k2[0] , " k3[0]: " , k3[0] , " k4[0]: " , k4[0] )
    state[0] = z + (tstep/6) * (k1.item(0) + 2*k2.item(0) + 2*k3.item(0) + k4.item(0))
    #print(state[0])
    print("state1: " , state[1] , " tstep: " , tstep , " k1[1]: " , k1[1] , " k2[1]: " , k2[1] , " k3[1]: " , k3[1] , " k4[1]: " , k4[1] )
    state[1] = zdot + (tstep/6) * (k1.item(1) + 2*k2.item(1) + 2*k3.item(1) + k4.item(1))
    d        = zdot + (tstep/6) * (k1.item(1) + 2*k2.item(1) + 2*k3.item(1) + k4.item(1))
    print("d ", d)
    print(state[1])
plt.plot(t,zp)
plt.show()
