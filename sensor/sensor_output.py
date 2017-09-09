import plotly.plotly as py
import plotly.graph_objs as go
import csv


def plot_spectrum_from_files(name,files):
    spectrums = []
    for file in files:
        spectrums.append(read_spectrum_from_file(file))
    plot_spectrums(name,spectrums)

def read_spectrum_from_file(file):
    spectrum = {}
    with open(file, 'r') as file:
        csvfile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvfile:
                if(len(line) == 0):
                    continue
                if("wavelength" in line[0]):
                    spectrum["wavelength"] = line[1:]
                if ("power" in line[0]):
                    spectrum["power"] = line[1:]
    return spectrum

def plot_spectrums(name,spectrums):
    data = []
    for spectrum in spectrums:
        data.append(go.Scatter(
            x=spectrum["wavelength"],
            y=spectrum["power"]
        ))

    py.plot(data, filename=name)