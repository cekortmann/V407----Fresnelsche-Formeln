import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

def n(a, I, E):
    return np.sqrt(0.5*((E+E*np.sqrt(140/I))/(E-E*np.sqrt(140/I))*1/np.cos(a))**2+np.sqrt(0.25*((E+E*np.sqrt(140/I))/(E-E*np.sqrt(140/I))*1/np.cos(a))**4-(E+E*np.sqrt(140/I))/(E-E*np.sqrt(140/I))**2*(tan(a))**2))

uI = ufloat(0.5, 0.1)
ul = ufloat(0.102, 0.005)

print(n(uI, ul))