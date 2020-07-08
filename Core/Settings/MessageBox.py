# Import modules

from ctypes import windll


# MessageBox Output

def MessageBox(Message):
 windll.user32.MessageBoxW(0, Message, u'', 0x10)