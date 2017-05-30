import numpy as np
def KL(a, b):
    """Calculate the Kullback Leibler divergence between a and b """
    D_KL = np.nansum(np.multiply(a, np.log(np.divide(a, b+np.spacing(1)))))
    return D_KL


def calc_information(probTgivenXs, PYgivenTs, PXs, PYs):
    """Calculate the MI - I(X;T) and I(Y;T)"""
    PTs = np.nansum(probTgivenXs*PXs, axis=1)
    Ht = np.nansum(-np.dot(PTs, np.log2(PTs)))
    Htx = - np.nansum((np.dot(np.multiply(probTgivenXs, np.log2(probTgivenXs)), PXs)))
    Hyt = - np.nansum(np.dot(PYgivenTs*np.log2(PYgivenTs+np.spacing(1)), PTs))
    Hy = np.nansum(-PYs * np.log2(PYs+np.spacing(1)))
    IYT = Hy - Hyt
    ITX = Ht - Htx
    return ITX, IYT

def calc_information_1(probTgivenXs, PYgivenTs, PXs, PYs, PTs):
    """Calculate the MI - I(X;T) and I(Y;T)"""
    #PTs = np.nansum(probTgivenXs*PXs, axis=1)
    Ht = np.nansum(-np.dot(PTs, np.log2(PTs+np.spacing(1))))
    Htx = - np.nansum((np.dot(np.multiply(probTgivenXs, np.log2(probTgivenXs+np.spacing(1))), PXs)))
    Hyt = - np.nansum(np.dot(PYgivenTs*np.log2(PYgivenTs+np.spacing(1)), PTs))
    Hy = np.nansum(-PYs * np.log2(PYs+np.spacing(1)))
    IYT = Hy - Hyt
    ITX = Ht - Htx
    return ITX, IYT

def calc_information(probTgivenXs, PYgivenTs, PXs, PYs, PTs, probTgivenXs_n, PYgivenTs_n, PXs_n, PTs_n, type):
    """Calculate the MI - I(X;T) and I(Y;T)"""
    #PTs = np.nansum(probTgivenXs*PXs, axis=1)
    t_indeces = np.nonzero(PTs)
    Ht = np.nansum(-np.dot(PTs, np.log2(PTs+np.spacing(1))))
    Htx = - np.nansum((np.dot(np.multiply(probTgivenXs, np.log2(probTgivenXs)), PXs)))
    Hyt = - np.nansum(np.dot(PYgivenTs*np.log2(PYgivenTs+np.spacing(1)), PTs))
    Hy = np.nansum(-PYs * np.log2(PYs+np.spacing(1)))

    Ht_n = np.nansum(-np.dot(PTs_n, np.log2(PTs_n+np.spacing(1))))
    Htx_n = - np.nansum((np.dot(np.multiply(probTgivenXs_n, np.log2(probTgivenXs_n)), PXs_n)))
    Hyt_n = - np.nansum(np.dot(PYgivenTs_n * np.log2(PYgivenTs_n + np.spacing(1)), PTs_n))
    if type==0:
        IYT = Hy - Hyt
        ITX = Ht - Htx
    elif type==1:
        IYT = Hy - Hyt_n
        ITX = Ht_n - Htx_n
    elif type == 2:
        IYT = Hy - Hyt_n
        ITX = Ht - Htx_n
    elif type == 3:
        IYT = Hy - Hyt_n
        ITX = Ht_n - Htx
    elif type == 4:
        IYT = Hy - Hyt
        ITX = Ht_n - Htx_n
    elif type == 5:
        IYT = Hy - Hyt
        ITX = Ht_n - Htx
    elif type == 6:
        IYT = Hy - Hyt
        ITX = Ht - Htx_n
    return ITX, IYT


def t_calc_information(p_x_given_t, PYgivenTs, PXs, PYs):
    """Calculate the MI - I(X;T) and I(Y;T)"""
    Hx = np.nansum(-np.dot(PXs, np.log2(PXs)))
    Hxt = - np.nansum((np.dot(np.multiply(p_x_given_t, np.log2(p_x_given_t)), PXs)))
    Hyt = - np.nansum(np.dot(PYgivenTs*np.log2(PYgivenTs+np.spacing(1)), PTs))
    Hy = np.nansum(-PYs * np.log2(PYs+np.spacing(1)))
    IYT = Hy - Hyt
    ITX = Hx - Hxt
    return ITX, IYT