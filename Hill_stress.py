import numpy as np
import matplotlib.pyplot as plt
from math import *

def HillStress(sigma11, sigma22, sigma33, sigma12, sigma23, sigma13, const_array):
    F, G, H, L, M, N = const_array
    hill = np.sqrt(F*(sigma22-sigma33)**2 + G*(sigma33-sigma11)**2 + H*(sigma11-sigma22)**2 + 2*L*sigma23**2 + 2*M*sigma13**2 + 2*N*sigma12**2)
    return hill

def HillStress2(sigma11, sigma22, sigma33, sigma12, sigma23, sigma13, const_array):             #WITH YIELD RATIOS
    a1, a2, a3, a4, a5, a6 = const_array
    hill = np.sqrt(a1*(sigma22-sigma33)**2 + a2*(sigma33-sigma11)**2 + a3*(sigma11-sigma22)**2 + 3*a4*sigma13**2 + 3*a5*sigma23**2 + 3*a6*sigma12**2)/(sqrt(2))
    return hill

def VMStress(sigma11, sigma22, sigma33, sigma12, sigma23, sigma13):
    vm = np.sqrt(0.5*((sigma11-sigma22)**2 + (sigma22-sigma33)**2 + (sigma11-sigma33)**2 + 6*(sigma12**2 + sigma23**2 + sigma13**2)))
    return vm


const_array = [0.5, 0.5, 2.28, 2.075, 2.075, 0.745]
yratios = [0.59976, 0.59976, 1, 0.85023, 0.85023, 1.41895]


const_array_1 = np.zeros(6)
const_array_1[0] = (1/yratios[1]**2)+(1/yratios[2]**2)-(1/yratios[0]**2)
const_array_1[1] = (1/yratios[2]**2)+(1/yratios[0]**2)-(1/yratios[1]**2)
const_array_1[2] = (1/yratios[0]**2)+(1/yratios[1]**2)-(1/yratios[2]**2)
const_array_1[3] = 2/yratios[5]**2
const_array_1[4] = 2/yratios[4]**2
const_array_1[5] = 2/yratios[3]**2
print(const_array_1)

hill = HillStress(0, 0, 5, 0, 0, 0, const_array)
hill2 = HillStress2(0, 0, 5, 0, 0, 0, const_array_1)
vm2 = VMStress(0, 0, 5, 0, 0, 0)
print(hill, hill2, vm2)
