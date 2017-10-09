import csv
import logging

import pandas as pd
import sys

from df_utils import log_df

pd.options.display.max_rows = 20
pd.options.display.width = 1000


log = logging.getLogger("sensor_input")
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(name)s [%(processName)s] [%(levelname)5s] %(message)s'))
log.addHandler(handler)


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


def read_pandas_from_files(files):
    return pd.concat(
        [
            pd
                .DataFrame(
                    [
                        line.split(",")[1:]
                        for line
                        in open(file, 'r')
                        if 'wavelength' in line or 'power' in line
                    ],
                    index=["wavelength", "power"]
                )
                .T
                .assign(
                    wavelength=lambda df: df.wavelength.astype('int'),
                    power=lambda df: df.power.astype('float'),
                    label=(file.split("/")[2]),
                    reading=int(file.split("/")[3].strip(".csv"))
                )
                .pipe(log_df, log, file)
            for file
            in files
        ]
    )
