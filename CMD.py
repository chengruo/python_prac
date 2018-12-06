import os
import time
import PIL

def closeprocess():
    str = os.popen("tasklist")
    str = str.read()
    print(str)
    if str.find("OUTLOOK.EXE") != -1:
        print("OUTLOOK is started,close it")
        os.popen("taskkill /im OUTLOOK.EXE /f")
    else :
        print("out look doesn't start")

    if str.find("Evernote.exe") != -1:
        print("Evernote is started,close it")
        os.popen("taskkill /im Evernote.exe /f")
        os.popen("taskkill /im EvernoteTray.exe /f")
    else:
        print("evernote doesn't start")


def task_close():
    while True:
        curtime = int(time.strftime("%H%M", time.localtime()))
        if curtime >= 2100:
            closeprocess()
            return
        sleeptime = (2100-curtime)*36
        print("current time is "+str(curtime)+" will sleep " +str(sleeptime/60)+" min!")
        time.sleep((2100-curtime)*36)


def task_startup():
    #os.popen("D:\常用软件\TeamViewe12\TVClientID.exe")
    task_close()

task_startup()
