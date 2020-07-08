# Import modules

import re
from json import loads
from urllib.request import urlopen
from subprocess import check_output, DEVNULL, STDOUT


# MAC address regex

macRegex = re.compile('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')


# Get router ip address

cmd = 'chcp 65001 && ipconfig | findstr /i \"Default Gateway\"'
check_output(cmd, shell=True, stderr=DEVNULL, stdin=DEVNULL)


# Get mac by local ip

def GetMacByIP():
 a = check_output('arp -a', shell=True, stderr=DEVNULL, stdin=DEVNULL)
 b = a.decode(encoding='cp866')
 c = b.find('')
 d = b[c:].split(' ')
 for b in d:
  if macRegex.match(b):
   return b.replace('-', ':')


# Locate by BSSID

def GetLocationByBSSID(BSSID):
 try:
  result = urlopen(f'http://api.mylnikov.org/geolocation/wifi?bssid={BSSID}').read().decode('utf8')
 except:
  return None
 else:
  result = loads(result)
  return result['data']
