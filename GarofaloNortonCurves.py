import matplotlib.pyplot as plt
import numpy as np
from Functions import *

def Garofalo(stress, T, C3=1.08172894e+12, C4=7.83785734e-03, n=8.04264041, EaKb=6.60614753e+04/8.314):
    ecr = C3*(np.sinh(C4*stress))**n * np.exp(-EaKb/T)
    return ecr

def Norton(stress, T, C1=1.34e-4, n=3.92, R=8.314, Q=32807.1):
    ecr = C1 * stress**n * np.exp(-Q/(R*T))
    return ecr


stress_array = np.arange(0, 50, 1)
temp_array = np.arange(25+273.15, 175+273.15, 25)
for temp in temp_array:
    g_list = []
    n_list = []
    for stress in stress_array:
        g_list.append(Garofalo(stress, temp))
        n_list.append(Norton(stress, temp))
    plt.plot(stress_array, n_list, "r")
    plt.plot(stress_array, g_list, "b")
    plt.xlim(0, 30)
    plt.ylim(0, 0.001)
    plt.grid()
    plt.title(f"T={temp-273.15} C")
    plt.show()

# plt.plot(stress_array, g_list, "r")
# plt.plot(stress_array, n_list, "b")

