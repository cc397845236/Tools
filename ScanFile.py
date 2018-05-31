import os
import psutil

def FullScan(filename):
    filepath = []
    for dir in getdisks():
        print ("Begin to scan " + dir + " , Please wait!")
        for a,b,c in os.walk(dir):
            # print (a,b,c)
            if filename in c:
                filepath.append(a)
    print("Scan results: ", filepath)
    return filepath

def getdisks():
    disklist = []
    getdisks = psutil.disk_partitions()
    for i in getdisks:
        disklist.append(i[0])
    return disklist

if __name__ == "__main__":
    s=FullScan("csgo.exe")
    print (s)


