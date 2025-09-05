import numpy as np
import matplotlib.pyplot as plt
import function as fct
Wavelength = np.arange(250, 502, 2)
Abs=np.array([0,0.203,0.404,0.613,0.849,0.904 ])
C=np.array([ 0,4,8,12,16,20])

coef = np.polyfit(C,Abs,1)
#print(slope)
poly1d_fn = np.poly1d(coef) 

plt.plot(C,Abs, 'yo',label="Points de mesure")
plt.plot(C, poly1d_fn(C),'--k',label="Fit") 
plt.grid()
plt.xlabel("Concentration méthyl orange [mg/L]") ; plt.ylabel("Absorbance (sans unité)")
plt.title("Courbe d'étalonnage")
plt.xlim(0, 22)
plt.legend()
plt.ylim(0, 1)