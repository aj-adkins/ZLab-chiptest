import sys
from PyQt6 import QtCore, QtWidgets, uic 
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QFileDialog, QColorDialog
import serial.tools.list_ports
from PiezoStage import PiezoStage
from PowerMeter import PowerMeter
from OSA import OSA
import numpy as np
import pyqtgraph as pg
import math
import time
import random
import datetime
import copy

from MainWindow import Ui_MainWindow
from SweepLoading import Ui_sweepLoading
from OSASettings import Ui_OSASettings
from PiezoSettings import Ui_PiezoSettings

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.Stage_A = PiezoStage()
        self.Stage_B = PiezoStage()
        self.Meter = PowerMeter()
        self.OSA = OSA()

        self.current_OSA_measurement = np.zeros((2,2))
        self.piezo_ports = []

        self.plots_dict = {}

    def setupSignals(self):
        # self.actionOption.triggered.connect(self.`v`oltage_init)

        # # Timer for continuous update of power readout
        self.power_timer=QTimer()
        self.power_timer.timeout.connect(self.display_power)
        
        # Timer for displaying voltages
        self.voltage_timer=QTimer()
        self.voltage_timer.timeout.connect(self.update_voltages)

        # Timers for grounding
        self.x_timer_a=QTimer()
        self.y_timer_a=QTimer()
        self.z_timer_a=QTimer()
        self.x_timer_b=QTimer()
        self.y_timer_b=QTimer()
        self.z_timer_b=QTimer()

        # Connecting grounding buttons
        self.groundAll_a.clicked.connect(self.ground_all_a)
        self.xGround_a.clicked.connect(lambda: self.x_timer_a.start(1000))
        self.yGround_a.clicked.connect(lambda: self.y_timer_a.start(1000))
        self.zGround_a.clicked.connect(lambda: self.z_timer_a.start(1000))
        self.groundAll_b.clicked.connect(self.ground_all_b)
        self.xGround_b.clicked.connect(lambda: self.x_timer_b.start(1000))
        self.yGround_b.clicked.connect(lambda: self.y_timer_b.start(1000))
        self.zGround_b.clicked.connect(lambda: self.z_timer_b.start(1000))
        
        # # OSA sweep timer
        self.sweep_timer=QTimer()
        self.sweep_timer.timeout.connect(self.osa_measure)

        # # Connect power meter button
        self.connectPower.clicked.connect(self.Meter.connect)

        # Connect piezo stage button
        self.connectA.clicked.connect(lambda: self.stage_connect(self.Stage_A, self.piezo_ports[0]['port']))
        self.connectB.clicked.connect(lambda: self.stage_connect(self.Stage_B, self.piezo_ports[1]['port']))
        
        self.actionview_COM_ports.triggered.connect(piezoSettingsScreen.show)

        # Connect OSA 
        self.osaConnectButton.clicked.connect(self.osa_connect)
        self.osaSweepButton.clicked.connect(self.osa_sweep)
        self.osaRepeatButton.clicked.connect(self.osa_repeat)
        self.osaSetLinButton.clicked.connect(self.set_linear)
        self.osaSetLogButton.clicked.connect(self.set_log)
        self.osaSaveButton.clicked.connect(lambda: self.save_osa_data(self.current_OSA_measurement))
        self.printButton.clicked.connect(self.osa_print)
        self.connectPower.clicked.connect(self.connect_meter)

        self.actionOSA_settings.triggered.connect(osaSettingsScreen.show)

        self.windowStartButton.clicked.connect(self.osa_window)

        # Connect spectrum view buttons
        self.addPlotButton.clicked.connect(self.add_plot)
        self.removePlotButton.clicked.connect(self.remove_plot)
        self.clearPlotButton.clicked.connect(self.clear_plot)
        self.colorButton.clicked.connect(self.set_plot_color)

    def stage_connect(self, controller, port):
        try:
            controller.connect(port)
            self.voltage_timer.start(250)

            if controller is self.Stage_A:
                self.connectA.setText('Disconnect')
                self.connectLabel_a.setText('A: connected')
                self.connectA.disconnect()
                self.connectA.clicked.connect(lambda: self.stage_disconnect(controller))

                self.xDisplay_a.setText(f'X: {controller.get_voltage("x")} V')
                self.xChange_a.setValue(controller.get_voltage('x'))

                self.yDisplay_a.setText(f'Y: {controller.get_voltage("y")} V')
                self.yChange_a.setValue(controller.get_voltage('y'))

                self.zDisplay_a.setText(f'Z: {controller.get_voltage("z")} V')
                self.zChange_a.setValue(controller.get_voltage('z'))
                
                self.xChange_a.valueChanged.connect(lambda: controller.set_voltage('x', self.xChange_a.value()))
                self.yChange_a.valueChanged.connect(lambda: controller.set_voltage('y', self.yChange_a.value()))
                self.zChange_a.valueChanged.connect(lambda: controller.set_voltage('z', self.zChange_a.value()))

                self.x_timer_a.timeout.connect(lambda: self.ground_voltage(controller, self.x_timer_a, 'x', self.xChange_a))
                self.y_timer_a.timeout.connect(lambda: self.ground_voltage(controller, self.y_timer_a, 'y', self.yChange_a))
                self.z_timer_a.timeout.connect(lambda: self.ground_voltage(controller, self.z_timer_a, 'z', self.zChange_a))

            if controller is self.Stage_B:
                self.connectB.setText('Disconnect')
                self.connectLabel_b.setText('B: connected')
                self.connectB.disconnect()
                self.connectB.clicked.connect(lambda: self.stage_disconnect(controller))

                self.xDisplay_b.setText(f'X: {controller.get_voltage("x")} V')
                self.xChange_b.setValue(controller.get_voltage('x'))

                self.yDisplay_b.setText(f'Y: {controller.get_voltage("y")} V')
                self.yChange_b.setValue(controller.get_voltage('y'))

                self.zDisplay_b.setText(f'Z: {controller.get_voltage("z")} V')
                self.zChange_b.setValue(controller.get_voltage('z'))
                
                self.xChange_b.valueChanged.connect(lambda: controller.set_voltage('x', self.xChange_b.value()))
                self.yChange_b.valueChanged.connect(lambda: controller.set_voltage('y', self.yChange_b.value()))
                self.zChange_b.valueChanged.connect(lambda: controller.set_voltage('z', self.zChange_b.value()))

                self.x_timer_b.timeout.connect(lambda: self.ground_voltage(controller, self.x_timer_b, 'x', self.xChange_b))
                self.y_timer_b.timeout.connect(lambda: self.ground_voltage(controller, self.y_timer_b, 'y', self.yChange_b))
                self.z_timer_b.timeout.connect(lambda: self.ground_voltage(controller, self.z_timer_b, 'z', self.zChange_b))

        except:
            print(f'Unable to find device in {port}')
    
    def stage_disconnect(self, controller, port):
        if controller is self.Stage_A:
            self.connectA.setText('Connect')
            self.connectLabel_a.setText('A: not connected')
            self.xDisplay_a.setText(f'X: 0.0 V')
            self.yDisplay_a.setText(f'Y: 0.0 V')
            self.zDisplay_a.setText(f'Z: 0.0 V')
            self.connectA.disconnect()
            self.connectA.clicked.connect(lambda: self.stage_connect(controller, port))

        if controller is self.Stage_B:
            self.connectB.setText('Connect')
            self.connectLabel_b.setText('B: not connected')
            self.xDisplay_b.setText(f'X: 0.0 V')
            self.yDisplay_b.setText(f'Y: 0.0 V')
            self.zDisplay_b.setText(f'Z: 0.0 V')
            self.connectB.disconnect()
            self.connectB.clicked.connect(lambda: self.stage_connect(controller, port))

    def update_voltages(self):
        if self.connectLabel_a.text() == 'A: connected':
            try:
                self.xDisplay_a.setText(f'X: {self.Stage_A.get_voltage("x")} V')
                self.yDisplay_a.setText(f'Y: {self.Stage_A.get_voltage("y")} V')
                self.zDisplay_a.setText(f'Z: {self.Stage_A.get_voltage("z")} V')
            except Exception as e:
                self.voltage_timer.stop()
                self.errorMessageBox.setWindowTitle('STAGE A')
                self.errorMessageBox.setText(f'ERROR: STAGE A NOT RESPONDING \n {e}')
                self.errorMessageBox.exec_()
                # self.stage_disconnect_a()

        if self.connectLabel_b.text() == 'B: connected':
            try:
                self.xDisplay_b.setText(f'X: {self.Stage_B.get_voltage("x")} V')
                self.yDisplay_b.setText(f'Y: {self.Stage_B.get_voltage("y")} V')
                self.zDisplay_b.setText(f'Z: {self.Stage_B.get_voltage("z")} V')
            except Exception as e:
                self.voltage_timer.stop()
                self.errorMessageBox.setWindowTitle('STAGE B')
                self.errorMessageBox.setText(f'ERROR: STAGE B NOT RESPONDING \n {e}')
                self.errorMessageBox.exec_()
                # self.stage_disconnect_a()

    def ground_voltage(self, controller, timer, dim, spinbox):
        v = controller.get_voltage(dim)
        if v <= 1 and v >= 0:
            controller.set_voltage(dim, 0)
            spinbox.setValue(0.0)
            timer.stop()
        else:
            controller.set_voltage(dim, v-1)

    def ground_all_a(self):
        self.x_timer_a.start(1000)
        self.y_timer_a.start(1000)
        self.z_timer_a.start(1000)

    def ground_all_b(self):
        self.x_timer_b.start(1000)
        self.y_timer_b.start(1000)
        self.z_timer_b.start(1000)


    def connect_meter(self):
        try:
            self.Meter.connect()
            self.wavelengthEdit.setText('1060')
            self.Meter.set_wavelength(1060)
            self.connectLabel_power.setText('Meter: connected')
            self.connectPower.setText('Disconnect')
            self.connectPower.disconnect()
            self.connectPower.clicked.connect(self.power_disconnect)
            self.power_timer.start(500)
        except:
            pass

    def disconnect_meter(self):
        print('disconnecting')
        self.connectLabel_power.setText('Meter: not connected')
        self.connectPower.setText('Connect')
        self.powerDisplay.setText('0.00')
        self.powerDisplay_unit.setText('nW')
        self.connectPower.disconnect()
        self.connectPower.clicked.connect(self.power_connect)
        self.power_timer.stop()
        self.Meter.close()

    def display_power(self):
        try:
            mag = math.floor(math.log(self.Meter.get_power(), 10))

            if abs(mag) >= 7:
                self.powerDisplay.setText(f'{self.Meter.get_power() * 10e8:.2f}')
                self.powerDisplay_unit.setText('nW')
            if abs(mag) in range(4, 7):
                self.powerDisplay.setText(f'{self.Meter.get_power() * 10e5:.2f}')
                self.powerDisplay_unit.setText('μW')
            if abs(mag) in range(0, 4):
                self.powerDisplay.setText(f'{self.Meter.get_power() * 10e2:.2f}')
                self.powerDisplay_unit.setText('mW')
        except:
            pass

    def osa_connect(self):
        try:
            self.OSA.connect()
            osaSettingsScreen.osaConnectedLabel.setText('OSA connected')
            self.osaConnectButton.setText('Disconnect')
            self.osaConnectButton.disconnect()
            self.osaConnectButton.clicked.connect(self.osa_disconnect)
            osaSettingsScreen.lambdaStartEdit.setText(str(self.OSA.get_wavelength_range()[0]))
            osaSettingsScreen.lambdaStopEdit.setText(str(self.OSA.get_wavelength_range()[1]))
            osaSettingsScreen.resolutionEdit.setText(str(self.OSA.get_resolution()))
            osaSettingsScreen.averagingEdit.setText(str(self.OSA.get_averaging()))

            if self.OSA.is_auto_ref():
                osaSettingsScreen.autoScalingCheck.setChecked(True)
            else:
                osaSettingsScreen.autoScalingCheck.setChecked(False)

        except Exception as e:
            print('OSA not found')

        
    def osa_disconnect(self):
        self.OSA.disconnect()
        print('OSA disconnected')
        self.osaConnectButton.setText('Connect')
        self.osaConnectButton.disconnect()
        self.osaConnectButton.clicked.connect(self.osa_connect)

    def osa_sweep(self):
        self.OSA.single_sweep()
        loadingScreen.show()
        loadingScreen.timer.start(750)

    def osa_repeat(self):
        self.osaRepeatButton.setText('Stop')
        self.osaRepeatButton.disconnect()
        self.osaRepeatButton.clicked.connect(self.osa_stop)
        self.sweep_timer.start(1000)
        self.OSA.repeat_sweep()

    def osa_stop(self):
        self.osaRepeatButton.setText('Repeat')
        self.osaRepeatButton.disconnect()
        self.osaRepeatButton.clicked.connect(self.osa_repeat)
        self.sweep_timer.stop()
        self.OSA.stop()

    def osa_print(self):
        # ;)
        self.OSA.copy()
        time.sleep(5)
        self.OSA.feed()
        

    def set_linear(self):
        self.OSA.set_linear()
        time.sleep(0.5)
        self.osa_measure()

    def set_log(self):
        self.OSA.set_log()
        time.sleep(0.5)
        self.osa_measure()

    def osa_measure(self):
        power = self.OSA.get_spectrum()
        wavelength_range = self.OSA.get_wavelength_range()
        wavelength = np.linspace(wavelength_range[0], wavelength_range[1], len(power))
        self.current_OSA_measurement = np.array([wavelength, power])
        self.plot_display(self.current_OSA_measurement)
        
    def plot_display(self, data):
        self.plotWidget.clear()
        self.plotWidget.showGrid(x=True, y=True, alpha=0.5)
        self.plotWidget.plot(data[0], data[1], pen='y')
        
    def save_osa_data(self, data):
        if self.OSA.connected:
            filename, _ = QFileDialog.getSaveFileName()
            with open(filename, 'a') as f:
                for i in range(len(data[0])):
                    f.write(f'{data[0][i]} {data[1][i]}\n')
        else:
            print('OSA not connected')

    def osa_window(self):
        num_windows = int(self.numWindowsSpin.value())

        if num_windows > 1:
            self.OSA.set_alarm(False)
            wavelength_range = self.OSA.get_wavelength_range()
            wavelength_span = wavelength_range[1] - wavelength_range[0]
            increment = wavelength_span/num_windows
            resolution = self.OSA.get_resolution()
            self.OSA.set_resolution(increment/1000)
            print(f'wavelength span: {wavelength_span}')
            print(f'increment: {increment}')
            print(f'resolution: {increment/1000}')

            data = []

            for i in range(num_windows):
                self.OSA.set_start_wavelength(wavelength_range[0] + i*increment)
                self.OSA.set_stop_wavelength(wavelength_range[0] + (i+1)*increment)
                self.OSA.single_sweep()

                time.sleep(1)

                loadingScreen.show()
                loadingScreen.timer.start(750)
                print(f'Running window sweep {i+1}')

                while self.OSA.is_sweeping():
                    time.sleep(1)
                
                power = self.OSA.get_spectrum()
                for val in power:
                    data.append(val)

            wavelength = np.linspace(wavelength_range[0], wavelength_range[1], len(data))
            self.plot_display(data=[wavelength, np.array(data)])

            if self.saveDataCheckbox.isChecked():
                filename, _ = QFileDialog.getSaveFileName()
                with open(filename, 'a') as f:
                    for i in range(len(data)):
                        f.write(f'{wavelength[i]} {data[i]}\n')

            time.sleep(1)
            self.OSA.set_start_wavelength(wavelength_range[0])
            self.OSA.set_stop_wavelength(wavelength_range[1])
            self.OSA.set_resolution(resolution)
            self.OSA.set_alarm(True)

        else:
            print('Number of windows must be greater than one')

    def add_plot(self):
        filename, _ = QFileDialog.getOpenFileName()
        try:
            wavelength = []
            power = []
            with open(filename, 'r') as f:
                for line in f.readlines():
                    data_point = line.split()
                    wavelength.append(float(data_point[0]))
                    power.append(float(data_point[1]))
                
            self.graphWidget.showGrid(x=True, y=True, alpha=0.5)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            plot = pg.PlotCurveItem(x=wavelength, y=power, pen=color)
            self.graphWidget.addItem(plot)
            plot_name = filename.split('/')[-1]
            item = self.listWidget.addItem(plot_name)
            self.plots_dict[plot_name] = plot

        except:
            print('Invalid')

    def remove_plot(self):
        current_item = self.listWidget.currentItem()
        self.graphWidget.removeItem(self.plots_dict[current_item.text()])
        self.listWidget.removeItemWidget(current_item)
        current_item.setHidden(True)
        
    def clear_plot(self):
        self.graphWidget.clear()
        self.listWidget.clear()

    def set_plot_color(self):
        color = QColorDialog.getColor()
        current_item = self.listWidget.currentItem()
        plot = self.plots_dict[current_item.text()]
        plot.setPen(color)


class SweepLoading(QtWidgets.QWidget, Ui_sweepLoading):
    def __init__(self, *args, obj=None, **kwargs):
        super(SweepLoading, self).__init__(*args, **kwargs)

        self.setupUi(self) 
        self.loading_state = 0
        self.timer=QTimer()
        self.timer.timeout.connect(self.loading)

    def loading(self):
            if self.loading_state == 3:
                self.label.setText('OSA sweeping ' + self.loading_state*'. ')
                self.loading_state = 0
            else:
                self.label.setText('OSA sweeping ' + self.loading_state*'. ')
                self.loading_state += 1

            if not window.OSA.is_sweeping():
                window.osa_measure()
                self.timer.stop()
                loadingScreen.hide()
                    
                
class OSASettings(QtWidgets.QWidget, Ui_OSASettings):
    def __init__(self, *args, obj=None, **kwargs):
        super(OSASettings, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.cancelButton.clicked.connect(self.close_window)
        self.applyButton.clicked.connect(self.apply_button)
        self.okButton.clicked.connect(self.ok_button)

    def ok_button(self):
        try:
            window.OSA.set_alarm(False)
            window.OSA.set_start_wavelength(float(self.lambdaStartEdit.text()))
            window.OSA.set_stop_wavelength(float(self.lambdaStopEdit.text()))
            window.OSA.set_resolution(float(self.resolutionEdit.text()))
            window.OSA.set_averaging(float(self.averagingEdit.text()))
            window.OSA.set_auto_ref(self.autoScalingCheck.isChecked())
            window.OSA.set_alarm(True)
            osaSettingsScreen.hide()
        except:
            osaSettingsScreen.hide()


    def apply_button(self):
        try:
            window.OSA.set_alarm(False)
            window.OSA.set_start_wavelength(float(self.lambdaStartEdit.text()))
            window.OSA.set_stop_wavelength(float(self.lambdaStopEdit.text()))
            window.OSA.set_resolution(float(self.resolutionEdit.text()))
            window.OSA.set_averaging(float(self.averagingEdit.text()))
            window.OSA.set_auto_ref(self.autoScalingCheck.isChecked())
            window.OSA.set_alarm(True)
        except:
           pass


    def close_window(self):
        osaSettingsScreen.hide()

class PiezoSettings(QtWidgets.QWidget, Ui_PiezoSettings):
    def __init__(self, *args, obj=None, **kwargs):
        super(PiezoSettings, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        comports_config = open('comports.txt', 'r')
        for port in comports_config.readlines():
            line = port.split(' ')
            window.piezo_ports.append({'port': line[0].strip(), 'desc': 'default'})
        comports_config.close()
        self.com_ports = serial.tools.list_ports.comports()
        self.com_options = copy.deepcopy(window.piezo_ports)
        for port, desc, hwid in sorted(self.com_ports):
            self.com_options.append({'port': port, 'desc': desc})

        if len(self.com_options) > 1:
            for option in self.com_options:
                self.StageAcombo.addItem(f'{option["port"]}: {option["desc"]}')
                self.StageBcombo.addItem(f'{option["port"]}: {option["desc"]}')

            self.StageAcombo.setCurrentIndex(0)
            self.StageBcombo.setCurrentIndex(1)

        self.cancelButton.clicked.connect(self.close_window)
        self.refreshPortsButton.clicked.connect(self.refresh_ports)
        self.applyButton.clicked.connect(self.apply_button)
        self.okButton.clicked.connect(self.ok_button)

    def refresh_ports(self):
        self.com_ports = serial.tools.list_ports.comports()
        print([f'{port}' for port in self.com_options])
        if len(self.com_options) > 1:
            self.StageAcombo.addItems(self.com_options)
            self.StageBcombo.addItems(self.com_options)


    def ok_button(self):
        try:
            stageA_port = self.com_options[self.StageAcombo.currentIndex()]
            stageB_port = self.com_options[self.StageBcombo.currentIndex()]

            window.piezo_ports = [stageA_port, stageB_port]
            comports_config = open('V3/comports.config', 'w')
            comports_config.write(f'{stageA_port["port"]}\n')
            comports_config.write(f'{stageB_port["port"]}\n')
            comports_config.close()
            piezoSettingsScreen.hide()
        except:
            piezoSettingsScreen.hide()


    def apply_button(self):
        try:
            
            stageA_port = self.com_options[self.StageAcombo.currentIndex()]
            stageB_port = self.com_options[self.StageBcombo.currentIndex()]

            window.piezo_ports = [stageA_port, stageB_port]
            comports_config = open('V3/comports.config', 'w')
            comports_config.write(f'{stageA_port["port"]}\n')
            comports_config.write(f'{stageB_port["port"]}\n')
            comports_config.close()

        except:
           pass


    def close_window(self):
        piezoSettingsScreen.hide()

app = QtWidgets.QApplication(sys.argv)


window = MainWindow()
loadingScreen = SweepLoading()
osaSettingsScreen = OSASettings()
piezoSettingsScreen = PiezoSettings()
window.setupSignals()
window.show()
