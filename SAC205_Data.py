import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

strain_rates = np.array([1E-3, 1E-4, 1E-5])
temp_array = np.array([25, 50, 75, 100, 125]) + 273.15
C_rate_1 = np.array([[27.1, 1493.8, 8.5, 266.1], [23.6, 1464.8, 7.5, 347.2], [20.1, 1435.9, 6.5, 428.4],
                     [16.5, 1406.9, 5.6, 509.5], [13, 1378, 4.6, 590.7]])
C_rate_2 = np.array([[19.4, 1875.7, 8.8, 408.2], [16.6, 1844.4, 7.7, 524.4], [13.8, 1813, 6.6, 640.6],
                     [11, 1781.7, 5.6, 756.8], [8.1, 1750.4, 4.5, 873]])
C_rate_3 = np.array([[15.7, 1953.8, 8.4, 517.8], [13.3, 1918.8, 7.3, 622.2], [10.8, 1883.8, 6.2, 726.5],
                     [8.3, 1848.8, 5.1, 830.8], [5.9, 1813.8, 3.9, 935.1]])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")



plt.xlabel(f"SAC205, strain rate: {strain_rates[0]} sec-1")
plt.ylabel("stress (MPa)")
plt.grid()
plt.legend()
plt.show()