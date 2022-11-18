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

def Garofalo(pred_array, C1, C4, n, Ea):
    stress, T = pred_array[0, :], pred_array[1, :]
    ecr = C1*(np.sinh(C4*stress))**n * np.exp(-Ea/(8.314*T))
    return ecr

const_array = [0.5, 0.5, 2.28, 2.075, 2.075, 0.745]
yratios = [0.83, 0.83, 1, 1.12, 1.12, 1.08]

#DEFINE a CONSTANTS
const_array_1 = np.zeros(6)
const_array_1[0] = (1/yratios[1]**2)+(1/yratios[2]**2)-(1/yratios[0]**2)
const_array_1[1] = (1/yratios[2]**2)+(1/yratios[0]**2)-(1/yratios[1]**2)
const_array_1[2] = (1/yratios[0]**2)+(1/yratios[1]**2)-(1/yratios[2]**2)
const_array_1[3] = 2/yratios[5]**2
const_array_1[4] = 2/yratios[4]**2
const_array_1[5] = 2/yratios[3]**2

s = [0, 0, 5, 0, 0, 0]
hill = HillStress(*s, const_array)
hill2 = HillStress2(*s, const_array_1)
vm2 = VMStress(*s)
print(hill, hill2, vm2)
grad = np.zeros(6)
aa = const_array_1

seqv = hill2
#CALCULATE HILL GRADIENT

grad[0] = ((aa[1]+aa[2])*s[0]-aa[1]*s[2]-aa[2]*s[1])/(2*seqv)
grad[1] = ((aa[0]+aa[2])*s[1]-aa[0]*s[2]-aa[2]*s[0])/(2*seqv)
grad[2] = ((aa[0]+aa[1])*s[2]-aa[0]*s[1]-aa[1]*s[0])/(2*seqv)
grad[3] = 1.5*(aa[3]*s[3])/seqv
grad[4] = 1.5*(aa[4]*s[4])/seqv
grad[5] = 1.5*(aa[5]*s[5])/seqv

#CALCULATE EQUIVALENT CREEP STRAIN

ladida = np.array([seqv, 125+273.15]).reshape((-1, 1))
gar_constants = [1.08e12, 0.00783, 8.045, 66061.47]
cr_eq = Garofalo(ladida, *gar_constants)

strrate_vector = grad*cr_eq
print(f'The strain rate vector is: {strrate_vector}')