import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
from Functions import *

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

strain_rates = np.array([1E-3, 1E-4, 1E-5])
temp_array = np.array([25, 50, 75, 100, 125, 150, 175, 200]) + 273.15
C_rate_1 = np.array([[43.3, 1284, 20.4, 183.9], [39.1, 1231.2, 18.2, 247.3], [35, 1178.4, 16.1, 310.8],[30.9, 1125.6, 13.9, 374.2],
                     [26.7, 1072.8, 11.7, 437.6], [22.6, 1020, 9.5, 501], [18.4, 967.2, 7.3, 564.4], [14.3, 914.4, 5.1, 627.8]])
C_rate_2 = np.array([[39.8, 1352.2, 16.5, 198.52], [35.5, 1294.9, 14.7, 227.04], [31.2, 1237.7, 12.9, 355.56], [26.9, 1180.4, 11.1, 434.08],
                     [22.5, 1123.2, 9.2, 512.6], [18.2, 1065.9, 7.4, 591.12], [13.9, 1008.7, 5.6, 669.64], [9.6, 951.4, 3.8, 748.16]])
C_rate_3 = np.array([[37.5, 1302.4, 10, 271.3], [32.7, 1249.5, 8.9, 371.7], [27.9, 1196.6, 7.8, 472], [23.1, 1143.7, 6.7, 572.4],
                     [18.3, 1090.9, 5.4, 672.7], [13.6, 1038, 4.6, 773.1], [9.3, 985.1, 3.5, 873.4], [5.2, 932.2, 2.4, 973.8]])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    slope = find_slope(strain, stress)
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    df1[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df1[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)

    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")


for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    slope = find_slope(strain, stress)
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    df2[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)

    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")


for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    slope = find_slope(strain, stress)
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    df3[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df3[f'modulus T={temp_array[i]-273.15}'] = np.ones(len(strain))*yield2percent(stress, line02)
    plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")
    plt.plot(strain, slope[1], label=f"T = {temp_array[i] - 273.15}")


plt.xlabel(f"SACQ, strain rate: {strain_rates[2]} sec-1")
plt.ylabel("stress (MPa)")
plt.xlim((0, 0.005))
plt.ylim((0, 70))
plt.grid()
plt.legend()
plt.show()
