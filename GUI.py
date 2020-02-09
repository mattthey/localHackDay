from PyQt5 import Qt, QtWidgets, QtCore, QtGui
import sys
import winAct
import matplotlib.pyplot as plt
 
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.win_act = winAct.WinAction()
        self.resize(925, 598)
        self.setWindowIcon(QtGui.QIcon('window_icon.png'))
        self.setWindowTitle('AtomParser')

        self.label = Qt.QLabel(self)
        pixmap = QtGui.QPixmap('bgrnd.jpg')
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setPixmap(pixmap)

        self.add =  QtWidgets.QPushButton('', self)
        self.add.setIcon(QtGui.QIcon('plus.png'))
        self.add.resize(30, 30)
        self.add.setIconSize(QtCore.QSize(40, 40))
        self.add.move(270, 50)
        self.add.clicked.connect(self.add_file)
        
        upld = Qt.QLabel('Upload file', self)
        upld.resize(150, 30)
        upld.setStyleSheet('font: 28px fantasy')
        upld.move(50, 50)

        self.sensors = QtWidgets.QComboBox(self)
        self.sensors.resize(0,0)
        self.sensors.currentIndexChanged.connect(self.change_sensor)

        
    
    def change_sensor(self, i):
        self.win_act.get_plot_for_sensors(self.sensors.itemText(i))
        plt.show()
    
    def add_file(self):
        # name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\')[0]
        # self.win_act.name_of_file = name
        # short_name = self.win_act.get_short_name(name)
        # label = Qt.QLabel(f'{short_name}', self)
        # label.move(200, 50)
        # label.setStyleSheet('font: 14px italic')
        # label.adjustSize()
        sns = self.win_act.get_sensors()
        if sns:
            for e in sns:
                self.sensors.addItem(QtGui.QIcon('sensor.png'), e)
            self.sensors.move(50, 200)
            self.sensors.resize(250, 30)
            self.sensors.setStyleSheet('font: 16px fantasy')
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
