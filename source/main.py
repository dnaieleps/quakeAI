'''
import numpy as np
import matplotlib as plt
import tensorflow as tf
import sklearn as sk
'''
import pandas as pd

# clean the .csv file on earthquake data found in the resources folder (pandas)
datafile = pd.read_csv('./resources/Significant_Earthquakes.csv')
print(datafile.head())

# turn cleaned file into np.array to be passed into the input layer of model (numpy + pandas)


# create the model architecture to be able for prediction forecasting  (tensorflow / pytorch)
# **research has shown that random forest is best for predicting WHEN, and LSTM is best for predicting magnitude


# train the model given the specific architecture (tensorflow, sklearn)


# do error analysis and construct graphs of training loss, cv loss, test loss, epochs, etc. (matplotlib + sklearn)


# predict (tensorflow)