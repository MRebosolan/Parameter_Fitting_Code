import numpy as np
import pandas as pd
from math import *

gr = np.array([8, 8, 7.5, 6.5, 7, 8, 9, 6.5, 8.5, 7.5, 9.5, 8.5, 8])
w = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5])
avg = sum(gr*w)/sum(w)
print(avg)