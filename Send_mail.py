import smtplib, socket
from email.mime.text import MIMEText
from datetime import datetime

def sendMail(ip, time):
    host = 'smtp.naver.com'
    sender = 'sender_mail'
    receiver = 'receiver_mail'
    contents = str(time) + '-' + ip
    ID = ''
    PW = ''

    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = 'Windows Login - ' + ip
    msg['From'] = sender
    msg['To'] = receiver

    s = smtplib.SMTP_SSL(host, 465)
    s.login(ID, PW)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

get_ip = socket.gethostbyname(socket.gethostname())
get_time = datetime.now()
get_time = get_time.strftime("%Y.%m.%d %H:%M:%S")

sendMail(get_ip, get_time)
