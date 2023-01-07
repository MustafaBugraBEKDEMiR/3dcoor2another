import numpy as np  #calling neccessary libraries.NumPy and Math.
import math as m    #

X,Y,Z,ang,ax=(1, 2, 3, 2, 3 )   # Determining inputs
                                    #as (X,Y,Z), Rotation Angle, Rotation Axis
v=np.array((X,Y,Z)) #Converting X,Y,Z input to matrix.
                    #Python tries it is a list.

z=np.radians(ang)   #Converting degree to radian. Library works with radian.

rx=np.matrix([[ 1, 0           , 0           ],         #
                   [ 0, m.cos(z),-m.sin(z)],            #X Rotation Matrix
                   [ 0, m.sin(z), m.cos(z)]])           #

ry=np.matrix([[ m.cos(z), 0, m.sin(z)],                 #
                   [ 0           , 1, 0           ],    #Y Rotation Matrix
                   [-m.sin(z), 0, m.cos(z)]])           #

rz=np.matrix([[ m.cos(z), -m.sin(z), 0 ],               #
                   [ m.sin(z), m.cos(z) , 0 ],          #Z Rotation Matrix
                   [ 0           , 0            , 1 ]]) #

if ax == 1:             #
                        #If rotation axis is X, Multiply input with 
    print((rx).dot(v))  #x rotation matrix

elif ax == 2:           #
                        #If rotation axis is Y, Multiply input with
    print(ry.dot(v))    #y rotation matrix

elif ax==3:             #
                        #If rotation axis is Z, Mulitply input with
    print(rz.dot(v))    #z rotation matrix
