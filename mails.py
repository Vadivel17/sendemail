import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
hostname = "***" + socket.gethostname() + " Server Rebooted***"
msg = MIMEMultipart('alternative')
msg['Subject'] = hostname
msg['From'] = "EMEA.Non.Prod.App.Support.BB@fisglobal.com"
msg['To'] = "FIS.EMEA.Non.Prod.App.Support@fisglobal.com"
str = open('/websphere/scr/system_check/out.html', 'r').read()
part2 = MIMEText(str, 'html')
msg.attach(part2)
s = smtplib.SMTP('UKSMARTHOST1.FISGLOBAL.COM')
s.sendmail("EMEA.Non.Prod.App.Support.BB@fisglobal.com", "FIS.EMEA.Non.Prod.App.Support@fisglobal.com", msg.as_string())
s.quit()
