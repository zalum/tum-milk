import logging

import sys

import sensor_input
import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd
from sklearn import tree
import numpy as np
import sklearn.metrics as met
from sklearn.neural_network import MLPClassifier
from sklearn import model_selection as ms

pd.options.display.max_columns=50
pd.options.display.width=1000

log = logging.getLogger("learn")
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(name)s [%(processName)s] [%(levelname)5s] %(message)s'))
log.addHandler(handler)



input_data = sensor_input.read_pandas_from_files([
    "../data2/frisch1/1.csv",
    "../data2/frisch1/2.csv",
    "../data2/frisch1/3.csv",
    "../data2/frisch1/4.csv",
    "../data2/frisch1/5.csv",
    "../data2/hmilch/1.csv",
    "../data2/hmilch/2.csv",
    "../data2/hmilch/3.csv",
    "../data2/hmilch/4.csv",
    "../data2/hmilch/5.csv",
    "../data2/leer/1.csv",
    "../data2/leer/2.csv",
    "../data2/leer/3.csv",
    "../data2/leer/4.csv",
    "../data2/leer/5.csv",
    "../data2/sauer/1.csv",
    "../data2/sauer/2.csv",
    "../data2/sauer/3.csv",
    "../data2/sauer/4.csv",
    "../data2/sauer/5.csv",
    "../data2/schale_morgen/1.csv",
    "../data2/schale_morgen/2.csv",
    "../data2/schale_morgen/3.csv",
    "../data2/schale_morgen/4.csv",
    "../data2/schale_morgen/5.csv",
])


data = [
    go.Trace(
        x=group.wavelength,
        y=group.power,
        name="{} - {}".format(key[0], key[1])
    )
    for key, group
    in input_data.groupby(["label", "reading"])
]

ply.plot(go.Figure(data=data))


sensor_data_avg = input_data\
    .drop("reading", axis=1)\
    .groupby(["label", "wavelength"])\
    .mean()\
    .reset_index()

data = [
    go.Trace(
        x=group.wavelength,
        y=group.power,
        name=key
    )
    for key, group
    in sensor_data_avg.groupby(["label"])
]

ply.plot(go.Figure(data=data))


np.random.seed(12345)
input = input_data.assign(label2=lambda df: df.label).loc[lambda df: df.label!="schale_morgen"]  #np.where(df.label=="leer", 0, 1))
train, test = ms.train_test_split(input)
clf = tree.DecisionTreeClassifier()
result = clf.fit(train[["wavelength", "power"]].values, train.label2.values)
prediction = clf.predict(test[["wavelength", "power"]].values)
print(test.assign(prediction=prediction))
#ms.cross_val_score(clf, test.power.values.reshape(7, 1), test.label2.values, scoring='accuracy')
met.confusion_matrix(test.label2.values, prediction)


# organize data per reading and features
data_reorganized = input_data.set_index(["label", "reading"]).pivot(columns="wavelength")
data_reorganized.columns = data_reorganized.columns.droplevel(level=0)
data_reorganized.columns.name = ""
data_reorganized = data_reorganized.reset_index()

np.random.seed(12345)
clf = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=10000)
train, test = ms.train_test_split(data_reorganized)
clf.fit(train.drop(["label", "reading"], axis=1), train["label"])
fitted = clf.predict(train.drop(["label", "reading"], axis=1))
predicted = clf.predict(test.drop(["label", "reading"], axis=1))

log.info("Train - confusion matrix")
print(met.confusion_matrix(train.label.values, fitted))
log.info("Train - accuracy")
print(met.accuracy_score(train.label.values, fitted))
log.info("Test - confusion matrix")
print(met.confusion_matrix(test.label.values, predicted))
log.info("Test - accuracy")
print(met.accuracy_score(test.label.values, predicted))