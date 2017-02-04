import smtplib
import sys
from email.mime.text import MIMEText

if len(sys.argv) == 5:
    mailto_list = sys.argv[1].split("|")
    mail_host = sys.argv[2]
    mail_user = sys.argv[3]
    mail_pass = sys.argv[4]
else:
    print "usage: sudo python smtp.py mail1|mail2|mail3.. smtpserver hostmail password"
    sys.exit(1)

#mailto_list=["qmao@linkernetworks.com"]
#mail_host="smtp.qiye.163.com"		#smtp server
#mail_user="qmao@linkernetworks.com"	#username
#mail_pass="Mao940715"			#password
  
def send_mail(to_list, subject, content):
  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)
        server.login(mail_user,mail_pass)  
        server.sendmail(mail_user, to_list, msg.as_string())  
        server.close()
        return True
    except Exception, e:  
        print str(e)  
        return False

if __name__ == '__main__':
    if send_mail(mailto_list,"warning","temp beyond threshold!!!"):
        print "sending mail succeeded"
    else:
        print "sending mail failed"
