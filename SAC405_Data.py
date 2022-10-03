import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
from Functions import *

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

strain_rates = np.array([1E-3, 1E-4, 1E-5])
temp_array = np.array([25, 50, 75, 100, 125]) + 273.15
C_rate_1 = np.array([[32.2, 1442.6, 14.4, 130.6], [28.9, 1397.4, 12.4, 175.1], [25.5, 1352.2, 10.3, 219.5],
                     [22.2, 1307, 8.2, 264], [18.9, 1261.8, 6.2, 308.5]])
C_rate_2 = np.array([[28.7, 1499.7, 9.1, 236.2], [25.4, 1458.7, 7.9, 271.2], [22, 1417.7, 6.7, 306.2],
                     [18.7, 1376.7, 5.5, 341.2], [15.4, 1335.7, 4.3, 376.2]])
C_rate_3 = np.array([[27.5, 1495.7, 5.6, 253], [23.6, 1434.1, 4.9, 294.8], [19.6, 1372.5, 4.3, 336.6],
                     [15.7, 1310.8, 3.6, 378.4], [11.8, 1249.2, 3, 420.2]])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
yield_strengths = []

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    slope = find_slope(strain, stress)
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df1[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    slope = find_slope(strain, stress)
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.0001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    slope = find_slope(strain, stress)
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")
    plt.plot(strain, slope[1], label=f"T = {temp_array[i] - 273.15}")
    plt.xlim((0, 0.004))
    plt.ylim((0, 70))
    plt.grid()
    plt.legend()
    plt.show()


yield_strengths = np.array(yield_strengths)

# y02_1, T02_1 = yield_strengths[:8, 0], yield_strengths[:8, 1]
# y02_2, T02_2 = yield_strengths[8:16, 0], yield_strengths[8:16, 1]
# y02_3, T02_3 = yield_strengths[16:, 0], yield_strengths[16:, 1]
#
# plt.plot(T02_1, y02_1)
# plt.plot(T02_2, y02_2)
# plt.plot(T02_3, y02_3)
