import plotly.offline as py
import plotly.graph_objs as go
import sensor_input
import random
from pandas import Series


def plot_spectrum_from_files(name,files):
    spectrums = []
    for file in files:
        spectrums.append(sensor_input.read_spectrum_from_file(file))
    plot_spectrums(name,spectrums)

def plot_data_from_pandas(pandas):
    data = []
    for panda in pandas:
        data.append(go.Scatter(
            x=panda,
            y=spectrum["power"],
            marker = dict(
                color = 'rgba(10, 10, 240, .9)'
            )))
    return data

def get_plot_data(name, spectrums):
    data = []
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    for spectrum in spectrums:
        data.append(go.Scatter(
            x=spectrum["wavelength"],
            y=spectrum["power"],
            name=name,
            marker = dict(
                color = 'rgba(%s, %s, %s, .9)'%(r,g,b)
            )
        ))
    return data

def read_plot_data_from_files(name,files):
    spectrums = []
    for file in files:
        spectrums.append(sensor_input.read_spectrum_from_file(file))
    return get_plot_data(name,spectrums)

def plot_spectrum_from_files_group(file_groups):
    data = []
    for key in file_groups.keys():
        for plot_data in read_plot_data_from_files(key,file_groups[key]):
            data.append(plot_data)

    py.plot(data, filename="all_ploted")


def plot_spectrums(name,spectrums):
    data = get_plot_data(name,spectrums)
    py.plot(data, filename=name)