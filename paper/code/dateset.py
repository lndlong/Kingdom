import numpy
import matplotlib.pyplot as plt
from pandas import read_csv

dataframe = read_csv('../Data/tfotj_1c.csv')
dataset = dataframe.values
dataset = dataset.astype('float32')
######### shift one clom

#dataset = dataframe.

plt.plot(dataset)
plt.xlabel('Month')
plt.ylabel('Flow')
plt.show()
