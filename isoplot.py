#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def isoplot(z1,z2,legend1,legend2, zone=[60,25,-65,50], scale=[0,1]):
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    
    z1 = ( z1 * (scale[1]-scale[0]) + scale[0] ) / 100
    z2 = ( z2 * (scale[1]-scale[0]) + scale[0] ) / 100

    x_vals = np.linspace(zone[2], zone[3], z1.shape[1])
    y_vals = np.linspace(zone[1], zone[0], z1.shape[0])
    x, y = np.meshgrid(x_vals, y_vals)

    fig = plt.figure(figsize=(12,4))
    ax = fig.add_axes([left, bottom, width, height]) 
    cp1 = plt.contour( x, y, z1[::-1]/1000., colors='red')
    cp2 = plt.contour( x, y, z2[::-1]/1000., colors='blue')
    
    ax.clabel(cp1, inline=True, fontsize=10)
    ax.clabel(cp2, inline=True, fontsize=10)
    ax.set_title('MSLP')
    ax.set_xlabel('degrees')
    ax.set_ylabel('degrees')
    
    h1,_ = cp1.legend_elements()
    h2,_ = cp2.legend_elements()
    ax.legend([h1[0], h2[0]], [legend1, legend2])

    plt.show()

if __name__ == "__main__":
    x=np.load("data/data.npy")
    z=np.load("data/zone.npy")
    s=np.load("data/scale.npy")
    x0=x[24,:,:,0]
    x1=x[25,:,:,0]
    isoplot(x1,x0,"test","test",z,s[0])