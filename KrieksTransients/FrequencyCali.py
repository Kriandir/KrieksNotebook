import numpy as np
import math
import matplotlib.pyplot as plt


def Function(A0,err0,A1,err1,A2,err2,freq):
    return A0*np.power(10,(A1*math.log((freq/(150.*1e6)),10)))*np.power(10,(A2*math.log((freq/(150.*1e6)),10)**2))
    # return (np.log(A0)+A1*np.log(freq)+A2*np.power(np.log(freq),2))





A0 = 83.084
error0 =1.862
A1 = -0.699
error1 = 0.014
A2 = -0.110
error2 = 0.024
z = []
x = np.linspace(1,1000,100000)
for i in x:

    z.append(Function(A0,error0,A1,error1,A2,error2,float(i*1e6)))

plt.plot(x,z)
plt.title(r"Frequency dependence of measured Flux for 3c 196")
plt.xlabel(r"Frequency [MHz]")
plt.ylabel(r"Fluxdensity [Jy]")
plt.yscale('log')
plt.xscale('log')
plt.xlim(5,1000)
# plt.ylim(10,1000)
np.save('fluxlist',z)
np.save('freqlist',x)
plt.savefig("Freqdependency")
plt.show()
