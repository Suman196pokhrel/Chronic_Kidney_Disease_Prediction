import glob
from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import keras as k


class ChronicClass:

    def __init__(self, column_list=['sg', 'al', 'sc', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'classification'],
                 to_drop_list=['id', "age", "bp", "su", "rbc", "pc", "pcc",
                               "ba", "bgr", "bu", "sod", "pot",
                               "dm", "cad", "appet",
                               "pe", "ane"], test_size_split=0.2, number_of_epochs=500, activation_fun='relu'):
        print('The Logic FIle is running')
        self.df = pd.read_csv("kidney_disease.csv")
        self.columns_to_retain = column_list
        self.df = self.df.drop(to_drop_list, axis=1)
        self.df = self.df.dropna(axis=0)
        self.number_of_epochs = number_of_epochs
        self.history = None

        # Transform the non-numeric data in the columns
        for column in self.df.columns:
            if self.df[column].dtype == np.number:
                continue
            self.df[column] = LabelEncoder().fit_transform(self.df[column])

        # split the data into independent (x) dataset(the features) and dependent (y) dataset(the target)
        self.X = self.df.drop(["classification"], axis=1)
        self.y = self.df["classification"]

        # Feature Scaling
        # min-max scaler method scales the data set so that all the input lie between 0 and 1
        self.x_scaler = MinMaxScaler()
        self.x_scaler.fit(self.X)
        column_names = self.X.columns
        self.X[column_names] = self.x_scaler.transform(self.X)

        # split data into 80% training and 20% testing
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size=test_size_split, shuffle=True)

        # Build the model
        self.model = Sequential()
        self.model.add(
            Dense(256, input_dim=len(self.X.columns), kernel_initializer=k.initializers.random_normal(seed=13),
                  activation=activation_fun))
        self.model.add(Dense(1, activation='hard_sigmoid'))

        # Compile the model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        print('The model is being trained')
        # train the model
        self.history = self.model.fit(self.X_train, self.y_train, epochs=self.number_of_epochs,
                                      batch_size=self.X_train.shape[0])

        # save the model
        self.model.save('ckd.model')

    # def train_and_save_model(self):
    #     print('The model is being trained')
    #     # train the model
    #     self.history = self.model.fit(self.X_train, self.y_train, epochs=self.number_of_epochs,
    #                                   batch_size=self.X_train.shape[0])
    #
    #     # save the model
    #     self.model.save('ckd.model')
    #     # print(self.model.predict())

    def visualize_model(self):
        print('Visualization started')
        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['loss'])
        plt.title('model accuracy & loss')
        plt.ylabel('accuracy & loss')
        plt.xlabel('epoch')
        plt.show()

    def predict_fun(self, feature_list):
        print('Accessing predicting Function')
        predicted_value = self.model.predict(feature_list)
        return predicted_value


columns_list1 = ['sg', 'al', 'sc', 'hemo', 'pcv', 'wcc', 'rbc', 'htn', 'classification']
to_drop_list1 = ['id', "age", "bp", "su", "rbc", "pc", "pcc",
                 "ba", "bgr", "bu", "sod", "pot",
                 "dm", "cad", "appet",
                 "pe", "ane"]
test_size_split1 = 0.2
number_of_epochs1 = 100
activation_fun1 = 'relu'
if __name__ == '__main__':

    mainobj = ChronicClass(columns_list1, to_drop_list1, test_size_split1, number_of_epochs1, activation_fun1)

    mainobj.train_and_save_model()
    mainobj.visualize_model()
