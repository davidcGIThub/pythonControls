import numpy as py
import vtolParam as P

def vtolController(zd,z,z_prev,hd,h,h_prev,theta,theta_prev):
    tau = vtolLatOuterController(zd,z,z_prev,theta,theta_prev)
    force = vtolHController(hd,h,h_prev)

    left_force =  force/2 - tau/(2*P.d)
    right_force = force/2 + tau/(2*P.d)
    if(P.saturated):
        if(right_force > P.upper):
            right_force = P.upper
        if(left_force > P.upper):
            left_force = P.upper
        if(right_force < P.lower):
            right_force = P.lower
        if(left_force < P.lower):
            left_force = P.lower


    return [left_force,right_force]

def vtolLatOuterController(zd,z,z_prev,theta,theta_prev):
    error = zd - z
    deriv = (z - z_prev)/P.tstep
    theta_d = P.Kp_Lat_Out*error - P.Kd_Lat_Out*deriv
    tau = vtolLatInnerController(theta_d,theta,theta_prev)
    return tau


def vtolLatInnerController(thetad,theta,theta_prev):
    error = thetad - theta
    deriv = (theta - theta_prev)/P.tstep/10
    tau = P.Kp_Lat_In*error - P.Kd_Lat_In*deriv
    return tau

def vtolHController(hd,h,h_prev):
    error = hd - h
    deriv = (h - h_prev)/P.tstep
    F_tilde = error*P.Kp_H - deriv*P.Kd_H
    F_e = P.mt*P.g
    force = F_e + F_tilde
    return force
