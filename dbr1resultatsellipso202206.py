import numpy as np
import matplotlib.pyplot as plt
import function as fct
Wavelength = np.arange(250, 502, 2)
Abs=np.array([0,0.203,0.404,0.613,0.849,0.904 ])
C=np.array([ 0,4,8,12,16,20])

coef = np.polyfit(C,Abs,1)
poly1d_fn = np.poly1d(coef) 

plt.plot(C,Abs, 'yo', C, poly1d_fn(C), '--k') 
plt.grid()
plt.xlabel("Concentration méthyl orange") ; plt.ylabel("Absorbance")
plt.title("Courbe d'étalonnage")
plt.legend() 
plt.xlim(0, 22)
plt.ylim(0, 1)