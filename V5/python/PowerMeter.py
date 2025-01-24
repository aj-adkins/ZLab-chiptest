from datetime import datetime
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time

class PowerMeter:
    def __init__(self):
        self.state = 'closed'
        
    def connect(self):
        if self.state != 'open':
            self.tlPM = TLPM()
            deviceCount = c_uint32()
            self.tlPM.findRsrc(byref(deviceCount))

            print("devices found: " + str(deviceCount.value))

            resourceName = create_string_buffer(1024)

            for i in range(0, deviceCount.value):
                self.tlPM.getRsrcName(c_int(i), resourceName)
                print(c_char_p(resourceName.raw).value)
                break

            self.tlPM.open(resourceName, c_bool(True), c_bool(True))

            message = create_string_buffer(1024)
            self.tlPM.getCalibrationMsg(message)
            #print(c_char_p(message.raw).value)

            self.state = 'open'
            time.sleep(2)
        else:
            pass

    def get_power(self):
        power =  c_double()
        self.tlPM.measPower(byref(power))
        return power.value

    def close(self):
        self.tlPM.close()
        self.state = 'closed'

    def get_wavelength(self):
        return self.tlPM.getWavelength()

    def set_wavelength(self, wavelength):
        self.tlPM.setWavelength(c_double(wavelength))
        
