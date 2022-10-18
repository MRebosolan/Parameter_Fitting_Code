import numpy as np
import pandas as pd
from math import *
from scipy import stats
import matplotlib.pyplot as plt
from Functions import *

grades = np.array([8, 8, 7.5, 6.5, 7, 8, 6, 6.5, 8.5, 7.5, 9.5, 8.5, 8])
weights = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5])
gpa = sum(weights*grades)/sum(weights)

print(gpa)