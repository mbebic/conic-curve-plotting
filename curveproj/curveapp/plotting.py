import numpy as np
import plotly.express as px
import json
import logging

## old function for testing, can be removed once ready.
# def plot_conic(a,b,c,d,e,f,Np=100):

#     logging.info("entered plot_conic")
#     theta = np.linspace(0, np.pi*2, Np)
#     x = np.random.rand()*50+20*np.cos(theta)
#     y = np.random.rand()*0.5+0.2*np.sin(theta)

#     temp = {'x': x.tolist(), 'y': y.tolist()}

#     return temp

def plot_conic(a,b,c,d,e,f,Np=100):
    logging.info("entering plot function")
    mx = np.array([[a,b/2],[b/2,c]])
    logging.info(mx)

    [lam1, lam2] = np.linalg.eig(mx)[0]
    logging.info(lam1,lam2)

    mx2 = np.array([[a,b/2,d/2],[b/2,c,e/2],[d/2,e/2,f]])
    logging.info(mx2)

    s = np.linalg.det(mx2)
    logging.info(s)

    a = np.sqrt(-s/(lam1**2*lam2))
    b = np.sqrt(-s/(lam1*lam2**2))
    logging.info(a,b)

    xc = -d*a**2/2
    yc = -e*b**2/2
    logging.info(xc,yc)

    theta = np.linspace(0,2*np.pi,200)
    x = xc+a*np.cos(theta)
    y = yc+b*np.sin(theta)

    logging.info(x,y)

    temp = {'x': x.tolist(), 'y': y.tolist()}

    return temp