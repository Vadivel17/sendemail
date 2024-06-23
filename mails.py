import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
hostname = "***" + socket.gethostname() + " Server Rebooted***"
msg = MIMEMultipart('alternative')
msg['Subject'] = hostname
msg['From'] = "test@mail.com"
msg['To'] = "test2@mail.com"
str = open('file.html', 'r').read()
part2 = MIMEText(str, 'html')
msg.attach(part2)
s = smtplib.SMTP('smtp_server')
s.sendmail("from", "to", msg.as_string())
s.quit()
