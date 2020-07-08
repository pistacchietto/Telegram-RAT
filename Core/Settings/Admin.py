# Import modules

from ctypes import windll


# Is user administrator

def Admin():
 return windll.shell32.IsUserAnAdmin() != 0