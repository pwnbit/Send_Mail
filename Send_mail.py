from email.mime.text import MIMEText

def sendMail(ip):
    host = 'smtp.naver.com'
    contents = ip
    ID = ''
    PW = ''

    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = 'Windows Login - ' + ip

    s = smtplib.SMTP_SSL(host, 465)
    s.login(ID, PW)
    s.sendmail(me, you, msg.as_string())
    s.quit()

get_ip = socket.gethostbyname(socket.gethostname())

sendMail(get_ip)
