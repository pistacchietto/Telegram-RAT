# Import modules

from json import loads
from urllib.request import urlopen
from datetime import datetime, date
try:
 from wmi import WMI
except ImportError:
 raise SystemExit('Please run › pip install wmi')


# System Information

c = WMI()    
system = c.Win32_ComputerSystem()[0]
os = c.Win32_OperatingSystem()[0]
cpu = c.Win32_Processor()[0]
gpu = c.Win32_VideoController()[0]

os_version = ' '.join([os.Version, os.BuildNumber])
system_ram = float(os.TotalVisibleMemorySize) / 1048576

SystemVersion = os.Caption
ComputerName = system.Name
Manufacturer = system.Manufacturer
Model = system.Model
CPU = cpu.Name
GPU = gpu.Name
RAM = system_ram
ARM = os.osarchitecture


# Getting the version of Windows

def Windows():
 if SystemVersion.find('7') != -1 :
  return 'Windows 7'

 if SystemVersion.find('8') != -1 :
  return 'Windows 8'

 if SystemVersion.find('10') != -1 :
  return 'Windows 10'


# Getting the set computer time

def SystemTime():
 SystemTime = str(datetime.today().hour) + ':'+str(datetime.today().minute) + ':' + str(datetime.today().second)
 return SystemTime


# Getting location via IP Address

def Geolocation(Value, Ip=''):
 try:
  result = urlopen(f'http://ip-api.com/json/{Ip}').read().decode('utf-8')
 except:
  return None
 else:
  result = loads(result)
  return result[Value]