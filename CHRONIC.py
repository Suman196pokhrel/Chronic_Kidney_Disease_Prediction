import glob
from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import keras as k

df = pd.read_csv("kidney_disease.csv")
columns_to_retain = ['sg', 'al', 'sc', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'classification']
df = df.drop([col for col in df.columns if not col in columns_to_retain], axis=1)
df = df.dropna(axis=0)
# Transform the non-numeric data in the columns
for column in df.columns:
    if df[column].dtype == np.number:
        continue
    df[column] = LabelEncoder().fit_transform(df[column])
# split the data into independent (x) dataset(the features) and dependent (y) dataset(the target)
X = df.drop(["classification"], axis=1)
print(X)
y = df["classification"]
# Feature Scaling
# min-max scaler method scales the data set so that all the input lie between 0 and 1
x_scaler = MinMaxScaler()
x_scaler.fit(X)
column_names = X.columns
X[column_names] = x_scaler.transform(X)
# split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
# Build the model
model = Sequential()
model.add(
    Dense(256, input_dim=len(X.columns), kernel_initializer=k.initializers.random_normal(seed=13), activation='relu'))
model.add(Dense(1, activation='hard_sigmoid'))
# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# train the model
history = model.fit(X_train, y_train, epochs=500, batch_size=X_train.shape[0])
# save the model
# model.save('ckd.model')
# # visualize the model loss and accuracy
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['loss'])
# plt.title('model accuracy & loss')
# plt.ylabel('accuracy & loss')
# plt.xlabel('epoch')
# plt.show()

print('shape of train data', X_train.shape)
print('shape of test data', X_test.shape)

a = [[1.005, 4, 3.8, 11.1, 32, 6700, 3.9, 1],]
b = [[1.02, 0, 0.7, 14, 46, 9100, 5.8, 0],]
pred = model.predict(a)
print(pred)
print('actual', '1')
# pred = [1 if y >= 0.5 else 0 for y in pred]
# print('Original : {0}'.format(", ".join(str(x) for x in y_test)))
# print('Predicted: {0}'.format(", ".join(str(x) for x in pred)))
# print()
