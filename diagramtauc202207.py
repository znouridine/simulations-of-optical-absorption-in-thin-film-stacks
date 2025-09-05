import numpy as np
import matplotlib.pyplot as plt
Wavelength = np.arange(300, 420, 1)
from scipy.integrate import simps
from scipy.interpolate import make_interp_spline
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import make_interp_spline
from numpy import trapz
import numpy as np
import function as fct


Wavelength = np.arange(300,420, 1)
name="hv07"
first="ahv07"
file=fct.Openfile(name)
file1=fct.Openfile(first)
s=list(file)
t=list(file1)
ss=np.array(s)
tt=np.array(t)


plt.grid()
plt.plot(ss,tt,label='Tauc')

plt.title("Diagramme de Tauc")
plt.xlabel("hv en eV")
plt.ylabel("ahv en eV.m-1")
#plt.xlim([2.96,5])
#plt.ylim([0,0.8])
plt.legend()
plt.show()