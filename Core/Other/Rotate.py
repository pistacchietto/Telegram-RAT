# Import modules

from win32api import EnumDisplayDevices, EnumDisplaySettings, ChangeDisplaySettingsEx
from win32con import ENUM_CURRENT_SETTINGS, DMDO_DEFAULT, DMDO_90, DMDO_180, DMDO_270


# Variables

Rotations = {
    '0': DMDO_DEFAULT,
    '90': DMDO_90,
    '180': DMDO_180,
    '270': DMDO_270
}


# Monitor position control

def DisplayRotate(Degrees='0'):
 try:
  RotationValue = Rotations[Degrees]
 except KeyError:
  RotationValue = DMDO_DEFAULT
 Device = EnumDisplayDevices(None, 0)
 dm = EnumDisplaySettings(Device.DeviceName, ENUM_CURRENT_SETTINGS)
 if (dm.DisplayOrientation + RotationValue) % 2 == 1:
  dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
 dm.DisplayOrientation = RotationValue
 ChangeDisplaySettingsEx(Device.DeviceName, dm)
