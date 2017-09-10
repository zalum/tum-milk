import milch_sensor
import sensor_input
import unittest

class TestRealMilk(unittest.TestCase):
    def run_test_on_file(self, is_milk_good, file):
        test_spectrum = sensor_input.read_spectrum_from_file(file)
        self.assertEqual(is_milk_good,milch_sensor.is_milk_good(test_spectrum))


    def test_good_milk_data(self):
        self.run_test_on_file(True, "../data2/frisch1/1.csv")
        self.run_test_on_file(True, "../data2/frisch1/2.csv")
        self.run_test_on_file(True, "../data2/frisch1/3.csv")
        self.run_test_on_file(True, "../data2/frisch1/4.csv")
        self.run_test_on_file(True, "../data2/frisch1/5.csv")

    def test_sauer_milk_data(self):
        self.run_test_on_file(False, "../data2/sauer/1.csv")
        self.run_test_on_file(False, "../data2/sauer/2.csv")
        self.run_test_on_file(False, "../data2/sauer/3.csv")
        self.run_test_on_file(False, "../data2/sauer/4.csv")
        self.run_test_on_file(False, "../data2/sauer/5.csv")

    def test_schale_morgen_data(self):
        self.run_test_on_file(False, "../data2/schale_morgen/1.csv")
        self.run_test_on_file(False, "../data2/schale_morgen/2.csv")
        self.run_test_on_file(False, "../data2/schale_morgen/3.csv")
        self.run_test_on_file(False, "../data2/schale_morgen/4.csv")
        self.run_test_on_file(False, "../data2/schale_morgen/5.csv")