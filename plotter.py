import matplotlib.pyplot as plt
from data import Data
import numpy as np

class Plotter:
    def _plot_sensor(self, sensor, values, alarms):
        print(sensor)
        X = [x[0].split(' ')[1] for x in values]
        Y = [float(x[1]) for x in values]

        X2 = [x[0].split()[1] for x  in alarms]

        #X = list(range(0, len(X)))
        #Y[2] = -49
        #Y[3] = -52
        # Y = list(range(0, len(Y)))


        plt.xticks(np.arange(0, len(X) + 1, 130.0))
        plt.title(sensor)
        return plt.plot(X, Y)

    def plot_graph(self, sensor_name, data=None):
        # data = Data('log.txt')
        alarms = data.get_alarms()

        self._plot_sensor(sensor_name, data.get_sensor_values(sensor_name), alarms)


