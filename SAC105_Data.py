import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

strain_rates = np.array([1E-3, 1E-4, 1E-5])
temp_array = np.array([25, 50, 75, 100, 125]) + 273.15
C_rate_1 = np.array([[19.9, 1664.3, 6.9, 226.4], [17.6, 1606, 6.3, 340.1], [15.3, 1547.6, 5.6, 453.7],
                     [13, 1489.3, 4.9, 567.4], [10.7, 1431, 4.2, 681.1]])
C_rate_2 = np.array([[16.3, 1864.1, 5.7, 308.5], [14.2, 1810.7, 4.9, 435.5], [12.1, 1757.3, 4.1, 562.4],
                     [10., 1703.9, 3.3, 689.3], [8, 1650.6, 2.5, 816.2]])
C_rate_3 = np.array([[14, 1911.3, 5.2, 494.5], [11.8, 1864.4, 4.5, 610.5], [9.6, 1817.6, 3.8, 726.7],
                     [7.4, 1770.7, 3.1, 842.6], [5.1, 1723.9, 2.4, 958.7]])

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



plt.xlabel(f"SAC105, strain rate: {strain_rates[0]} sec-1")
plt.ylabel("stress (MPa)")
plt.grid()
plt.legend()
plt.show()