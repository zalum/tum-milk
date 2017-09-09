import statistics


def is_milk_H(wavelength, wavelength_interval=(100,200), threshold_down=200):
    cut_wavelength = wavelength[wavelength_interval[0]:wavelength_interval[1]]
    mean = statistics.mean(cut_wavelength)
    return {"mean":mean,
            "is":statistics.mean(cut_wavelength)<threshold_down}

def is_milk_fresh(wavelength,wavelength_interval=(100,200), threshold_up=100):
    cut_wavelength = wavelength[wavelength_interval[0]:wavelength_interval[1]]
    mean = statistics.mean(cut_wavelength)
    return {"mean":mean,
            "is":statistics.mean(cut_wavelength)>threshold_up}

