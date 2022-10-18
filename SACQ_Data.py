import numpy as np
import pandas as pd
from math import *
import scipy as sp

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
yield_strengths = []

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    slope = find_slope(strain, stress)
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    df1[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df1[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")


for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    slope = find_slope(strain, stress)
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    df2[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")


for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    slope = find_slope(strain, stress)
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    df3[f'modulus T={temp_array[i]-273.15}'], line02 = slope
    df3[f'modulus T={temp_array[i]-273.15}'] = np.ones(len(strain))*yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    # plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")
    # plt.plot(strain, slope[1], label=f"T = {temp_array[i] - 273.15}")

yield_strengths = np.array(yield_strengths)


y02_1, T02_1 = yield_strengths[:8, 0], yield_strengths[:8, 1]
y02_2, T02_2 = yield_strengths[8:16, 0], yield_strengths[8:16, 1]
y02_3, T02_3 = yield_strengths[16:, 0], yield_strengths[16:, 1]

plt.scatter(T02_1, y02_1)
plt.scatter(T02_2, y02_2)
plt.scatter(T02_3, y02_3)
plt.xlabel("Temperature (K)")
plt.ylabel("Yield strength (MPa)")

lm1 = sp.stats.linregress(T02_1, y02_1)
slope1, intercept1 = lm1.slope, lm1.intercept
lm2 = sp.stats.linregress(T02_2, y02_2)
slope2, intercept2 = lm2.slope, lm2.intercept
lm3 = sp.stats.linregress(T02_3, y02_3)
slope3, intercept3 = lm3.slope, lm3.intercept


def linear_func1(x):
    y = slope1*x + intercept1
    return y
def linear_func2(x):
    y = slope2*x + intercept2
    return y
def linear_func3(x):
    y = slope3*x + intercept3
    return y

# FINDING YIELD STRENGTH AT 0K

T_range = np.arange(0, 500, 1)
y_lm1 = list(map(linear_func1, T_range))
y_lm2 = list(map(linear_func2, T_range))
y_lm3 = list(map(linear_func3, T_range))
plt.plot(T_range, y_lm1)
plt.plot(T_range, y_lm2)
plt.plot(T_range, y_lm3)
yieldT0 = sum([y_lm1[0], y_lm2[0], y_lm3[0]])/3


# FINDING 4 FITTING PARAMETERS

#CREATE COMBINATIONS OF T, STRAIN RATES

predictor_array = []

for sr in strain_rates:
    for temp in temp_array:
        predictor_array.append([sr, temp])

predictor_array = np.array(predictor_array)

# print(predictor_array)
# print(yield_strengths[:, 0])

p01 = np.array([1E5, 80000, 1.5, 0.5])
bounds1 = ([1E2, 1000, 1, 0], [1e7, 200000, 2, 1])

b1 = busso_stress(predictor_array, 1.7E5, 80000, 1.5, 0.5)
print(b1)



