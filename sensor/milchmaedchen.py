import sys
import csv
import ctypes
sys.path.append("../wrappers/python")
import sys
import csv
import ctypes
sys.path.append("../wrappers/python")

from wrapper_python3 import *
from wrapper_python3.core import *
from wrapper_python3.device import *
from wrapper_python3.color import *

import milch_sensor
import gpio

def main_loop(pSpecCore, pSpecDevice, newSS):
    filterData = get_filter_data(pSpecDevice,20)

    specSize = get_spectrum_length(pSpecCore)
    (ret, specData,wavelengthdata) = calculate_spectrum(pSpecCore,filterData,newSS)

    (Start_Wavelength, End_Wavelength, Interval_Wavelength) = get_wavelength_information(pSpecCore)

    # resolution = get_resolution(pSpecCore)

    # colorData = calculate_color_data(pSpecCore,specData, wavelengthdata,specSize)

    # cleanData = []
    # for v in specData:
    #     cleanData.append(v.value)

    data = []
    for i in range(get_spectrum_length(pSpecCore)):
       data.append(specData[i])

    # print("specData: " + str(specData.value))

    milch_sensor.analyze(data, Start_Wavelength.value);

    #fileName = (b"SpecrtumData3_" + sensorID + b".csv");
    #data = []
    #for i in range(get_spectrum_length(pSpecCore)):
    #    data.append(str(specData[i]).split(","))

    #with open(fileName, 'w', newline='') as csvfile:
     #   filewriter = csv.writer(csvfile, delimiter=',',
      #              quotechar='|', quoting=csv.QUOTE_MINIMAL)
       # for line in data:
        #    filewriter.writerow(line)
    #csvfile.close()

def init():
    initialize("../Libs/libCrystalBase_RPi.so")
    pSpecCore      = initialize_core_api("../Libs/libCrystalCore_RPi.so")
    pSpecDevice    = initialize_device_api("../Libs/libCrystalPort_RPi.so")

    initialize_color_api(pSpecCore)


    connectReturn   = connect_device(pSpecDevice)   # return total num of devices connected with system

    if connectReturn > 0:

        (ret, sensorID) = get_sensor_id_device(pSpecDevice)

        create_core_object(pSpecCore)

        if sys.platform == 'win32':
            csInit_Return = load_sensor_file(pSpecCore, b"..\config\sensor_" + sensorID + b".dat")
        else:
            csInit_Return = load_sensor_file(pSpecCore, b"../config/sensor_" + sensorID + b".dat")

        (ret, sensorID) = get_sensor_id_file(pSpecCore)

        get_sensor_parameters_from_device(pSpecDevice)

        (adcGain,adcRange) = get_sensor_parameters_from_calibration_file(pSpecCore)

        settingReturn = set_sensor_parameters_to_device(pSpecDevice,adcGain,adcRange)

        total_num_of_sensors = total_sensors_connected(pSpecDevice)

        get_capacity_sensor_data_list(pSpecCore)

        for index in range(total_num_of_sensors):

            #activate a specific device(sensor)
            activatingReturn = index_activation(pSpecDevice,index)

            #get sensor id of currently activated device(sensor)
            (ret, sensorID) = get_sensor_id_device(pSpecDevice)

            #get and set shutter speed of device(sensor)
            get_shutter_speed(pSpecDevice)
            set_shutter_speed(pSpecDevice,1)

            #get one filter output (sensor data)
            filterData = get_filter_data(pSpecDevice,20)

            #set background data
            set_background_data(pSpecCore,filterData)

            #get and set shutter speed of device(sensor)
            get_shutter_speed(pSpecDevice)

            valid_filters_num = get_num_of_valid_filters(pSpecCore)
            valid_filters = get_valid_filters(pSpecCore)

            #Get shutter speed with AE
            # newSS = get_optimal_shutter_speed(pSpecDevice,valid_filters_num,valid_filters)
            # print ("newSS" + str(newSS))

            # Fix shutter speed at 100
            newSS = 100
            set_shutter_speed(pSpecDevice, newSS)

            #convert shutter speed to exposure time (ms) for your reference
            ss_to_exposure_time(pSpecDevice,5,newSS)

            gpio.init();
            while(True):
                main_loop(pSpecCore, pSpecDevice, newSS);
            # main_loop(pSpecCore, pSpecDevice, newSS);
    else:
        print ("**********************************************************************")
        print ("[PrismError]Device Not Connected. Please connect Device and try again.")
        print ("**********************************************************************")
    close_color_api(pSpecCore)
    close_core_object(pSpecCore)
    disconnect_device(pSpecDevice)

init();
