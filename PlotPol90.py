import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray

#md = pd.read_csv(Polarisation90.csv)

a, I, E, n= np.genfromtxt('Polarisation90.txt', unpack = True, skip_header=1, skip_footer=2)

plt.plot(a,np.sqrt(I/1.4*10**(-4)), 'xr', markersize = 6 , label='Messdaten', alpha=1)

plt.xlabel(r'$\alpha \,/ \, \mathrm{°}$')
plt.ylabel(r'$\sqrt{(I/I_0)}$')
plt.grid(True)
plt.savefig('build/plot90Pol.pdf',bbox_inches = "tight")