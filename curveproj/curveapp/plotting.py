import numpy as np
import json
import logging

def plot_conic(a,b,c,d,e,f,Np=100):

    logging.error("entered plot_conic")
    theta = np.linspace(0, np.pi*2, Np)
    x = np.random.rand()*50+20*np.cos(theta)
    y = np.random.rand()*0.5+0.2*np.sin(theta)

    temp = {'x': x.tolist(), 'y': y.tolist()}

    return temp

