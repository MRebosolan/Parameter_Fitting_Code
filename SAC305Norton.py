import numpy as np
from math import *
from scipy.optimize import curve_fit
from Functions import *
import pandas as pd

def recreatecurves(strain, C1, C2, C3, C4):
    stress = C1 * np.tanh(C2*strain) + C3 * np.tanh(C4*strain)
    return stress

def Garofalo(pred_array, C1, C4, n, Ea):
    stress, T = pred_array[0, :], pred_array[1, :]
    ecr = C1*(np.sinh(C4*stress))**n * np.exp(-Ea/(8.314*T))
    return ecr

def Norton(pred_array, C1, n, Q):
    stress, T = pred_array[0, :], pred_array[1, :]
    ecr = C1 * stress**n * np.exp(-Q/(8.314*T))
    return ecr

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
stress_array = []
strain_array = []
temp_array2 = []

yield_strengths = []

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_1[i, :])
    strain_array.append(strain)
    stress_array.append(stress)
    for j in range(len(strain)):
        temp_array2.append(temp_array[i])
    slope = find_slope(strain, stress)
    df1["strain"] = strain
    df1[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df1[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_2[i, :])
    strain_array.append(strain)
    stress_array.append(stress)
    for j in range(len(strain)):
        temp_array2.append(temp_array[i])
    slope = find_slope(strain, stress)
    df2["strain"] = strain
    df2[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])
    #plt.plot(strain, stress, label=f"T = {temp_array[i] - 273.15}")

for i in range(len(temp_array)):
    strain = np.arange(0, 0.02, 0.00001)
    stress = recreatecurves(strain, *C_rate_3[i, :])
    strain_array.append(strain)
    stress_array.append(stress)
    for j in range(len(strain)):
        temp_array2.append(temp_array[i])
    slope = find_slope(strain, stress)
    df3["strain"] = strain
    df3[f'stress T={temp_array[i]-273.15}'] = stress
    line02 = slope[1]
    df2[f'modulus T={temp_array[i] - 273.15}'] = np.ones(len(strain)) * yield2percent(stress, line02)
    yield_strengths.append([yield2percent(stress, line02), temp_array[i]])

#GENERATE STRESS/TEMPERATURE PREDICTOR ARRAY
stress_array = np.array(stress_array)
predictor_array = []

stress_array2 = []
for z in stress_array:
    for elem in z:
        stress_array2.append(elem)

strain_array2 = []
for w in strain_array:
    for elem in w:
        strain_array2.append(elem)


prt = int(len(stress_array2)/3)
strain_rate_array = np.hstack((np.ones(prt)*strain_rates[0], np.ones(prt)*strain_rates[1], np.ones(prt)*strain_rates[2]))
predictor_array = np.vstack((stress_array2, temp_array2))
nortonbounds = ([0, 0, 0], [1000, 40, 300000])
garofalop0 = np.array([1.78e12, 0.023, 12.1, 10856*8.314])
garofalobounds = ([0, 0, 0, 0], [2e15, 10, 40, 300000])
popt, cov = curve_fit(Norton, predictor_array, strain_rate_array, bounds=nortonbounds)
print(popt)
popt2, cov2 = curve_fit(Garofalo, predictor_array, strain_rate_array, p0=garofalop0, bounds=garofalobounds)   #PREDICTS Q, NOT Q/R
print(popt2)
