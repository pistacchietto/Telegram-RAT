# Import modules

from subprocess import Popen


# Opens a browser link

def OpenBrowser(URL):
 if not URL.startswith('http'):
     URL = 'http://' + URL
 Popen('start ' + URL, shell=True)