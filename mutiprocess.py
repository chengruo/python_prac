import os
import win32gui
import win32api
import win32con
import time
hwnd = win32gui.FindWindow(0,"我的Android手机")
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

title = win32gui.GetWindowText(hwnd)
clsname = win32gui.GetClassName(hwnd)

hwndChildList = []

win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd),  hwndChildList)

print(hwndChildList)

win32api.keybd_event(72,0,0,0)
win32api.keybd_event(32,0,0,0)
win32api.keybd_event(108,0,0,0)

def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList

#获取某个句柄的类名和标题
title = win32gui.GetWindowText(hwnd)
clsname = win32gui.GetClassName(hwnd)

#获取父句柄hwnd类名为clsname的子句柄
#hwnd1= win32gui.FindWindowEx(hwnd, None, clsname, None)
