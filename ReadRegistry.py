#coding:utf-8

import _winreg

def ReadRegistryValue(KeyName, ValueName):
    try:
        openKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, KeyName)
        path, type = _winreg.QueryValueEx(openKey, ValueName)
        # print path, type
        return path
    except WindowsError, ex:
        print "Read RegistryValue Failed " ,ex
        return 0

if __name__ == "__main__":
    ReadRegistryValue(r"Software\Valve1\Steam", "SteamPath")