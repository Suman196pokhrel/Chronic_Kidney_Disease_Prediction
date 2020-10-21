from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import keras as k
import pickle


def predict_fun(feature_list):

    with open(r'C:\Imp softwares\Pycharm\Pycharm projects\Chronic kidney disease\ckd.model\saved_model.pb','rb') as f:
        model = pickle.load(f)

        print(model.prdict(feature_list))



a = [[1.005, 4, 3.8, 11.1, 32, 6700, 3.9, 1]]

predict_fun(a)