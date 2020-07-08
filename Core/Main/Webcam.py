# Import modules

import os
from subprocess import call
from urllib.request import urlretrieve


CommandCamPath =  os.path.join(os.getenv('Temp'), 'CommandCam.exe')
CommandCamLink = 'https://raw.githubusercontent.com/tedburke/CommandCam/master/CommandCam.exe'


# Create screenshot from webcam

def WebcamScreenshot(File, Delay=2500, Camera=1):
 if not os.path.exists(CommandCamPath):
  urlretrieve(CommandCamLink, CommandCamPath)

 Command = f'@{CommandCamPath} /filename \"{File}\" /delay {Delay} /devnum {Camera} > NUL'
 call(Command, shell=True)