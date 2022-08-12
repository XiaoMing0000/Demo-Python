import sys
import win32gui
import win32con
from time import sleep

if __name__ == "__main__":
    filePath = ''
    # #32770 -- 文件夹对话框，既外层这个窗口
    winHandle = '#32770'
    if sys.argv.__len__() == 2:
        filePath = sys.argv[1]
    elif sys.argv.__len__() == 3:
        filePath = sys.argv[1]
        winHandle = sys.argv[2]
    else: 
        raise '输入参数错误，第一个参数为文件路径，第二参数可选参数为文件夹句柄'
    dialog = win32gui.FindWindow(winHandle, '打开')
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    sleep(0.2)
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)
    sleep(0.2)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    sleep(0.5)


  