from data import Data
from plotter import Plotter
import re

SHORT_NAME_REG = re.compile(r'(?<=\\)\w+\..+')
# name_of_file - полный путь
class WinAction():

    def __init__(self):
        self.data = None
        self.name_of_file = 'log.txt'

    def get_sensors(self):
        if self.name_of_file != '':
            self.data = Data(self.name_of_file)
            if self.data.get_file_correctness():
                return self.data.get_sensor_names()
        return []

    def get_plot_for_sensors(self, name_of_sns):
        plot = Plotter()
        plot.plot_graph(name_of_sns, self.data)

    def get_short_name(self, full_name):
        return ''
