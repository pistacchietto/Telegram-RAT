# Import modules

try:
 from mss import mss
except ImportError:
 raise SystemExit('Please run › pip install mss')


# Takes a screenshot

def Screenshot(File):
 with mss() as sct:
  sct.shot(output=File)