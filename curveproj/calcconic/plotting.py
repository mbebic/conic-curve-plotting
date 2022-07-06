import numpy as np
import logging

# folows 
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

    aa = np.sqrt(-s/(lam1**2*lam2))
    bb = np.sqrt(-s/(lam1*lam2**2))
    logging.info(aa,bb)

    xc = -d*a**2/2
    yc = -e*b**2/2
    logging.info(xc,yc)

    theta = np.linspace(0,2*np.pi,Np)
    x = xc+aa*np.cos(theta)
    y = yc+bb*np.sin(theta)

    temp = {'x': x.tolist(), 'y': y.tolist()}

    return temp