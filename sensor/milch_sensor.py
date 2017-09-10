import statistics
import sensor_input
import json

good_milk_statistics = None

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

def cut_spectrum(spectrum):
    return spectrum["power"][100:]

def stats(spectrum,mean=None):
    return {"stdev":statistics.stdev(spectrum["power"][100:],xbar=mean),
    "mean":statistics.mean(spectrum["power"][100:])}

def stats_spectrums(spectrums):
    means = []
    stdevs = []
    for spectrum in spectrums:
        out = stats(spectrum)
        means.append(out["mean"])
        stdevs.append(out["stdev"])

    return {"mean":statistics.mean(means),"stddev":statistics.mean(stdevs),
            "min_mean": min(means),"max_mean":max(means)}

def is_milk_good(test_spectrum):
    if good_milk_statistics is None:
        load_good_milch_statistics()
    print("\n\n--------------------------------------------")
    print("Good milk="+json.dumps(good_milk_statistics))
    test_spectrum_stats = stats(test_spectrum)
    print("Test milk="+json.dumps(test_spectrum_stats))
    return test_spectrum_stats["mean"]>=good_milk_statistics["min_mean"] and test_spectrum_stats["mean"]<=good_milk_statistics["max_mean"]

def load_good_milch_statistics():
    global good_milk_statistics
    good_milk_statistics = stats_spectrums(sensor_input.read_spectrum_from_files([
        "../data2/frisch1/1.csv",
        "../data2/frisch1/2.csv",
        "../data2/frisch1/3.csv",
        "../data2/frisch1/4.csv",
        "../data2/frisch1/5.csv"]))

