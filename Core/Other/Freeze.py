# Import modules

from ctypes import windll
from time import sleep, localtime


# Blocks mouse and keyboard movements

def Block(Seconds):
 windll.user32.BlockInput(True)
 sleep(Seconds)
 windll.user32.BlockInput(False)