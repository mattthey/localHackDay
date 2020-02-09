from data import Data

import numpy
import pylab

# Импортируем класс кнопки
from matplotlib.widgets import Button

# Начальные параметры графиков
current_sigma = 0.2
current_mu = 0.0
graph_axes = 1

# выдает значения по порядку
def gauss(sigma, mu, x):
    '''Отображаемая фукнция'''
    return (1.0 / (sigma * numpy.sqrt(2.0 * numpy.pi)) *
            numpy.exp(-((x - mu) ** 2) / (2 * sigma * sigma)))


def addPlot(graph_axes, sigma, mu):
    '''Добавить график к осям'''
    x = numpy.arange(-5.0, 5.0, 0.01)
    y = gauss(sigma, mu, x)
    graph_axes.plot(x, y)

    # !!! Нужно для обновления графика
    pylab.draw()


'''' !!! Обработчик события для кнопки "Добавить" '''
def onButtonAddClicked(event):
    global current_sigma
    global current_mu
    global graph_axes

    current_sigma *= 2
    addPlot(graph_axes, current_sigma, current_mu)


def main():
    global current_sigma
    global current_mu
    global graph_axes

    # Создадим окно с графиком
    fig, graph_axes = pylab.subplots()
    graph_axes.grid()

    # Оставим снизу от графика место для виджетов
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)

    # Создадим ось для кнопки
    # отступ справа, отступ снизу, ширина, высота
    axes_button_add = pylab.axes([0.7, 0.05, 0.25, 0.075])
    axes_button_add_2 = pylab.axes([0.05, 0.05, 0.1, 0.05])

    # Создание кнопки
    # button_add = Button(axes_button_add, 'Добавить')

    # !!! Подпишемся на событие обработки нажатия кнопки
    # button_add.on_clicked(onButtonAddClicked)

    pylab.show()

    # Добавить график
    # addPlot(graph_axes, current_sigma, current_mu)

if __name__ == '__main__':
    main()