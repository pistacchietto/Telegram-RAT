# Import modules

from subprocess import Popen, PIPE


# Gets a list of active processes

def ProcessList():
 Calling = Popen('tasklist', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE).stdout.readlines()
 Process = [Calling[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] for i in range(3,len(Calling))]
 strProcess = '\n'.join(Process)

 return strProcess