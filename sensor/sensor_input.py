import csv

def read_spectrum_from_file(file):
    spectrum = {}
    with open(file, 'r') as file:
        csvfile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvfile:
            if(len(line) == 0):
                continue
            if("wavelength" in line[0]):
                spectrum["wavelength"] = list(map(lambda x: float(x),line[1:]))
            if ("power" in line[0]):
                spectrum["power"] = list(map(lambda x: float(x),line[1:]))
    return spectrum

def read_spectrum_from_files(files):
    spectrums = []
    for file in files:
        spectrums.append(read_spectrum_from_file(file))
    return spectrums