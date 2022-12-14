import numpy as np
from math import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from Functions import *

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

# DIFFERENT FITTING CONSTANTS FOR EACH STRAIN RATE AND TEMPERATURE


strain_rates = np.array([1E-3, 1E-4, 1E-5])
temp_array = np.array([25, 50, 75, 100, 125, 150, 175, 200]) + 273.15
C_rate_1 = np.array([[27.8, 1470.2, 9.7, 125], [24.8, 1414.3, 8.5, 196.9], [21.9, 1358.3, 7.4, 268.8], [18.9, 1302.4, 6.3, 340.7],     #rows = tempertaure, columns = C1,C2,C3,C4
                     [15.9, 1246.4, 5.1, 412.6], [13, 1190.5, 4, 484.5], [10, 1134.5, 2.8, 556.4], [7, 1078.6, 1.7, 628.3]])
C_rate_2 = np.array([[22.8, 1862.8, 9.8, 232.8], [20.3, 1727.1, 8.6, 324], [17.8, 1591.5, 7.3, 415.2], [15.3, 1455.8, 6.1, 506.3],
                     [12.8, 1320.1, 4.8, 597.5], [10.3, 1184.4, 3.5, 688.7], [7.8, 1048.7, 2.3, 779.9], [5.4, 913, 1, 871.1]])
C_rate_3 = np.array([[19.8, 1975.3, 6.8, 478.2], [17.4, 1830.9, 6.1, 532.9], [15.1, 1686.4, 5.4, 587.7], [12.7, 1541.9, 4.7, 642.4],
                     [10.4, 1397.5, 4, 697.2], [8, 1253, 3.3, 751.9], [5.7, 1108.5, 2.6, 806.7], [3.3, 964.1, 1.9, 861.4]])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

yield_strengths = []
E_moduli = []

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    slope = find_slope(strain, stress)
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df1[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    E_modulus = slope[0][1]
    E_moduli.append([E_modulus, temp_array[i]])
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    slope = find_slope(strain, stress)
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    E_modulus = slope[0][1]
    E_moduli.append([E_modulus, temp_array[i]])
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    slope = find_slope(strain, stress)
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    E_modulus = slope[0][1]
    E_moduli.append([E_modulus, temp_array[i]])
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    # plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")
    # plt.plot(strain, slope[1], label=f"T = {temp_array[i] - 273.15}")
    # plt.xlim((0, 0.004))
    # plt.ylim((0, 70))
    # plt.grid()
    # plt.legend()
    #plt.show()

E_moduli = np.array(E_moduli)
x_fit, y_fit = E_moduli[:8, 1].reshape((-1, 1)), E_moduli[:8, 0]
model = LinearRegression().fit(x_fit, y_fit)
E_slope, E_intercept = model.coef_, model.intercept_ #DEPENCENCE OF E_MODULUS ON T
print(E_slope, E_intercept)


plt.scatter(E_moduli[:8, 1], E_moduli[:8, 0])



# plt.title(f"SAC305, strain rate: {strain_rates[0]} sec-1")
# plt.grid()
# plt.xlabel("strain (-)")
# plt.ylabel("stress (MPa)")
# plt.legend()
plt.show()