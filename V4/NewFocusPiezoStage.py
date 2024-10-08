from pylablib.devices import Newport
# from pylablib.core.devio import comm_backend
import os

# os.add_dll_directory('C:/Users/Zlab/anaconda3/envs/chiptest3.10/Lib/site-packages/libusb/_platform/_windows/x64')

# print(Newport.get_usb_devices_number_picomotor())
stage1 = Newport.Picomotor8742()
stage1.move_by(axis=2, steps=50)