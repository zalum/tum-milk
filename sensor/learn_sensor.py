import sensor_input
import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd
from sklearn import tree
import numpy as np
from sklearn.metrics import confusion_matrix

pd.options.display.max_columns=50


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

ply.plot(go.
         Figure(data=data))


np.random.seed(12345)
input = input_data.assign(label2=lambda df: df.label).loc[lambda df: df.label!="schale_morgen"]  #np.where(df.label=="leer", 0, 1))
train, test = ms.train_test_split(input)
clf = tree.DecisionTreeClassifier()
result = clf.fit(train[["wavelength", "power"]].values, train.label2.values)
prediction = clf.predict(test[["wavelength", "power"]].values)
print(test.assign(prediction=prediction))
#ms.cross_val_score(clf, test.power.values.reshape(7, 1), test.label2.values, scoring='accuracy')
confusion_matrix(test.label2.values, prediction)


# organize data per reading and features
input_data.set_index(["label","reading"]).pivot(columns="wavelength")
