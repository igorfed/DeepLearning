import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import tensorflow as tf
import matplotlib.patches as mpatches
#plt.rcParams['figure.figsize'] = (10,6)
plt.figure()
X = np.arange(0.0, 5.0, 0.1)
a = 1
b = 0
Y = a * X + b
plt.plot(X, Y)
plt.grid(True)
plt.ylabel('Dependent Variable')
plt.xlabel('InDependent Variable')
plt.show()