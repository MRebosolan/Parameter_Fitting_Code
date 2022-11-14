import numpy as np
import matplotlib.pyplot as plt
from Functions import *


def floweq(stress, T, s, A, Q, xi, m, R=8.314):
    comp1 = A * np.exp(-Q/(R*T))
    comp2 = (np.sinh((xi*stress)/s))**(1/m)
    ein = comp1 * comp2
    return ein


def s_star(T, ein, s_hat, A, Q, n, R=8.314):
    s_star = s_hat*((ein/A)*np.exp(Q/(R*T)))**n
    return s_star


def stress_strain_response(str_rate, strain, T, xi, A, Q, m, s_hat, n, s_0, a, h0, R=8.314):
    comp1 = (1/xi) * np.arcsinh(((str_rate/A)*np.exp(Q/(R*T)))**m)
    comp2 = s_hat*((str_rate/A)*np.exp(Q/(R*T)))**n
    comp3 = (s_hat*((str_rate/A)*np.exp(Q/(R*T)))**n - s_0)**(1-a)
    comp4 = (a-1)*(h0*(s_hat*((str_rate/A)*np.exp(Q/(R*T)))**n)**(-a))*strain
    stress = comp1 * (comp2 - (comp3 + comp4)**(1/(1-a)))
    return stress


str_rate = 0.00001
T = 125+273.15
strain_array = np.arange(0, 0.02, 0.0001)
stress_array = []

for strain in strain_array:
    anand_stress = stress_strain_response(str_rate, strain, T, 4, 4000, 11900*8.314, 0.47, 5, 0.059, 5.5, 1.6, 30000)
    stress_array.append(anand_stress)

stress_array = np.array(stress_array)
plt.plot(strain_array, stress_array)
plt.grid()
plt.ylim(0, 25)
plt.title(f"T = {T-273.15} C, rate = {str_rate}")
plt.show()
