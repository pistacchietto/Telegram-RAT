# Import modules

from subprocess import Popen
from ctypes.wintypes import DWORD
from ctypes import byref, c_bool, windll


# Puts the computer to sleep 

def Hibernate():
 Popen('shutdown -h /f', shell=True)

# Turns off the computer

def Shutdown():
 Popen('shutdown -s /t 0 /f', shell=True)


# Restarts computer

def Restart():
 Popen('shutdown -r /t 0 /f', shell=True)

# Ends user session

def Logoff():
 Popen('shutdown -l /f', shell=True)


# Blue screen of death

def BSoD():
 windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(c_bool()))
 windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(DWORD()))