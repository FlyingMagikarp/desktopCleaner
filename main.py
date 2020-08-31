import os
import shutil
import datetime


def checkIfDesktopHasFiles(desktopPath):
    desktop = os.listdir(desktopPath)
    return True if len(desktop) > 0 else False


desktopPath = '/Users/magikarp/Desktop'
if checkIfDesktopHasFiles(desktopPath):
    dumpPath = '/Users/magikarp/Documents/desktopDump'
    timeFolder = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    dumpPath = dumpPath+'/'+timeFolder
    os.mkdir(dumpPath)
    counter = 0
    for file in os.listdir(desktopPath):
        shutil.move(desktopPath+'/'+file, dumpPath+'/'+file)
        counter += 1
    print("Moved " + str(counter) + " files")
    print("Your Desktop is now clean")
else:
    print("Desktop is already clean! :)")
