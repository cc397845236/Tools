#coding:utf-8

import os
import sys
import shutil

def CopyFilesFunc(srcdir, dstdir):
    #函数内获取指定的文件目录
    srcDirPath = srcdir
    dstDirPath = dstdir
    if os.path.isfile(srcDirPath):
        copyFile(srcDirPath, dstDirPath)
    elif os.path.isdir(srcDirPath):
    #遍历源目录下所有文件或文件夹
        for file in os.listdir(srcDirPath):
            # 将文件目录路径和文件名组成绝对路径
            srcFile = os.path.join(srcDirPath, file)
            dstFile = os.path.join(dstDirPath, file)
            # 判断源路径为文件or文件夹
            if os.path.isfile(srcFile):
                copyFile(srcFile, dstFile)
            elif os.path.isdir(srcFile):
                copyDir(srcFile,dstFile)
            else:
                print "Path error, please check!"
                return False
    else:
        print "Path error, please check!"
        return False

def copyFile(srcFile, dstFile):
    if not os.path.exists(dstFile):
        shutil.copyfile(srcFile, dstFile)
    # 若文件存在，判断目的文件与源文件修改时间是否一致，若不同删除目的文件
    elif os.path.exists(dstFile) and (os.path.getmtime(dstFile) != os.path.getmtime(srcFile)):
        print srcFile + " was not latest!"
        os.remove(dstFile)
        print srcFile + " removed successfully!"
        shutil.copyfile(srcFile, dstFile)
    else:
        print "File already existed and was latest!"
    print srcFile + " copy completed!"

def copyDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        shutil.copytree(srcDir, dstDir)
    # 若文件夹存在，判断目的文件与源文件修改时间是否一致，若不同删除目的文件
    elif os.path.exists(dstDir) and (os.path.getmtime(dstDir) != os.path.getmtime(srcDir)):
        print srcDir + " was not latest!"
        shutil.rmtree(dstDir)
        print srcDir + " removed successfully!"
        shutil.copytree(srcDir, dstDir)
    else:
        print "Fold already existed and was latest!"
    print srcDir + " copy completed!"

if __name__ == '__main__':
    CopyFilesFunc(sys.argv[1], sys.argv[2])