import numpy as np
import matplotlib.pyplot as plt
from math import *
from sklearn.linear_model import LinearRegression


def find_slope(x_array, y_array):
    slopes = (y_array-y_array[0])/(x_array-x_array[0])
    E_mod = slopes[1]
    line02 = E_mod*(x_array-0.0002)
    return slopes, line02

def yield2percent(x_array, y_array):
    diff = np.abs(y_array-x_array)
    minimum = np.min(diff)
    condition = (diff == minimum)
    location = np.where(condition)[0]
    return float(y_array[location])


