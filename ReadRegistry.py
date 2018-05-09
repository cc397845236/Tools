#coding:utf-8

import winreg

def ReadRegistryValue(KeyName, ValueName):
    try:
        openKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KeyName)
        path, type = winreg.QueryValueEx(openKey, ValueName)
        # print path, type
        return path
    except WindowsError as ex:
        print ("Read RegistryValue Failed ", ex )
        return 0

if __name__ == "__main__":
    ReadRegistryValue(r"Software\Valve1\Steam", "SteamPath")
