# Import modules

from ctypes import windll


# Displays a message on the screen

def SendMessageBox(Message):
 windll.user32.MessageBoxW(0, Message, u'', 0x40)